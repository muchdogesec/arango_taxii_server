from datetime import timedelta, timezone, datetime
import os
import subprocess
import tempfile
from . import models
from celery import shared_task, group
import logging
import json
from . import arango_helper
from stix2arango.stix2arango import Stix2Arango

@shared_task
def upload_all(task_id, username, password, objects):
    task = models.UploadTask.objects.get(id=task_id)
    bundle_id = f"bundle--{task_id}"
    
    db = Stix2Arango(task.db, task.collection, file=None, stix2arango_note=f"arango_taxii_status_id={task_id}", bundle_id=bundle_id, username=username, password=password, host_url=os.environ["ARANGODB_HOST_URL"])

    try:
        db.run(dict(type="bundle", id=bundle_id, objects=objects))
        task.uploads.update(status=models.Status.COMPLETE)
    except Exception as e:
        logging.info(e, exc_info=True)
        task.uploads.update(status=models.Status.FAILED, message=str(e))
    schedule_removal.s(task_id)


@shared_task
def schedule_removal(_, task_id):
    # automatically remove task after 24 hours
    tomorrow = datetime.now(timezone.utc) + timedelta(days=1)
    logging.info(
        f"Scheduling removal of task with status-id: `{task_id}` at {tomorrow}"
    )
    remove_completed_task.apply_async((task_id,), eta=tomorrow)


@shared_task
def remove_completed_task(task_id):
    logging.info(f"Removing task with status-id: `{task_id}`")
    task = models.UploadTask.objects.get(pk=task_id)
    task.delete()
