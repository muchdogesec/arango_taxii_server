from datetime import timedelta, timezone, datetime
import subprocess
import tempfile
from .import models
from celery import shared_task, group
import logging
import json
from . import arango_helper


@shared_task
def start_task(task_id):
    task_group = []
    for object in models.ObjectStatus.objects.filter(task_id=task_id):
        task_group.append(insert_one_object.s(object.pk))
    job = group(task_group) | schedule_removal.s(task_id)
    job.apply_async()
    

@shared_task
def insert_one_object(pk):
    obj = models.ObjectStatus.objects.get(pk=pk)
    db = arango_helper.ArangoSession((obj.task.username, obj.task.password))
    object_dict = json.loads(obj.stix_data_json)

    bundle = {
            'type': 'bundle',
            'id': f'bundle--{obj.task.id}',
            'objects': [object_dict],
        }
    status = models.Status.COMPLETE
    message = None
    with tempfile.NamedTemporaryFile('w', delete=True) as f:
        try:
            json.dump(bundle, f)
            f.flush()
            db.stix2arango(obj.task.db, obj.task.collection, f.name, obj.task.id)
        except subprocess.CalledProcessError as e:
            status = models.Status.FAILED
            message = f"stix2arango failed with return code: {e.returncode}"
        except Exception as e:
            status = models.Status.FAILED
            message = f"{e}"
    
    obj.message = message
    obj.status = status
    obj.save()

@shared_task
def schedule_removal(_, task_id):
    #automatically remove task after 24 hours
    tomorrow = datetime.now(timezone.utc) + timedelta(days=1)
    logging.info(f"Scheduling removal of task with status-id: `{task_id}` at {tomorrow}")
    remove_completed_task.apply_async((task_id,), eta=tomorrow)

@shared_task
def remove_completed_task(task_id):
    logging.info(f"Removing task with status-id: `{task_id}`")
    task = models.UploadTask.objects.get(pk=task_id)
    task.delete()

