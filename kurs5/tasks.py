from celery import shared_task

from kurs5.services import send_telegram_message


@shared_task
def send_telegram_bot_message():
    send_telegram_message()
