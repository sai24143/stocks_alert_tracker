from django_celery_beat.models import PeriodicTask, IntervalSchedule

# Create a schedule to run every 10 minutes
schedule, _ = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.MINUTES,
)

# Create the periodic task
PeriodicTask.objects.create(
    interval=schedule,
    name='Check Stock Alerts',
    task='tracker.tasks.check_stock_alerts_task',
)