import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.config.settings")

app = Celery("tasks")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

print(">> Hi :)")


@app.task(bind=True)
def debug_task(self):
    print(f"Requet: {self.request!r}")
