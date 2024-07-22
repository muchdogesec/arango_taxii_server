from django.db import models

# Create your models here.

APP_NAME = "arango_taxii_server"


class Status(models.TextChoices):
    PENDING = "pending"
    COMPLETE = "complete"
    FAILED = "failed"


class UploadTask(models.Model):
    id = models.UUIDField(primary_key=True)
    request_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64, blank=True)
    db = models.CharField(max_length=64)
    collection = models.CharField(max_length=256)

    def get_total_count(self):
        return self.uploads.count()

    def get_pendings(self):
        return self.uploads.filter(status=Status.PENDING)

    def get_pending_count(self):
        return self.uploads.filter(status=Status.PENDING).count()

    def get_successes(self):
        return self.uploads.filter(status=Status.COMPLETE)

    def get_success_count(self):
        return self.uploads.filter(status=Status.COMPLETE).count()

    def get_failures(self):
        return self.uploads.filter(status=Status.FAILED)

    def get_failure_count(self):
        return self.uploads.filter(status=Status.FAILED).count()

    def get_status(self):
        if self.get_pending_count():
            return Status.PENDING
        return Status.COMPLETE


class ObjectStatus(models.Model):
    stix_id = models.CharField(blank=False, null=False, max_length=160)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)
    message = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(
        choices=Status.choices, max_length=12, default=Status.PENDING, null=False
    )
    task = models.ForeignKey(
        UploadTask, on_delete=models.CASCADE, related_name="uploads"
    )

    def get_version(self):
        return self.modified or self.created or self.task.request_timestamp
