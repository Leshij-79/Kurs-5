import requests
from django.utils import timezone

from config.settings import TELEGRAM_BOT_TOKEN
from kurs5.models import Habits


def send_telegram_message():
    habits = Habits.objects.filter(time_habit__gt=timezone.now()).all()

    for habit in habits:
        params = {
            "text": f"У вас {habit.habit} время выполнения {habit.time_habit}",
            "chat_id": habit.owner.tg_id,
        }

        requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", params=params)
