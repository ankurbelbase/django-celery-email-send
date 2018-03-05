from celery import shared_task
from celery.schedules import crontab
from celery.decorators import periodic_task

from .emails import send_feedback_email


@shared_task()
def send_feedback_email_task(name, email, message):
    return send_feedback_email(name, email, message)


# this will trigger this task in every 1 minute
@periodic_task(
    run_every=(crontab()),
    name='send_test_email',
    ignore_result=True
)
def send_test_email():
    send_feedback_email()
    return 'SENT'


# this will run in every 5 second
# @periodic_task(run_every=timedelta(seconds=5))
# def every_5_seconds():
#     print("Running periodic task!")

# we can also define schedule time in crontab like this

# @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week=1))
# def every_monday_morning():
#     print("Execute every Monday at 7:30AM.")
