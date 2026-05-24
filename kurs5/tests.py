from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from kurs5.models import Habits, Rewards
from users.models import CustomUser


class Kurs5TestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="testuser", email="testuser@testuser.ru", password="123")

        self.rewards = Rewards.objects.create(action="Приятная привычка", is_habit=True, owner=self.user)

        self.habits = Habits.objects.create(
            habit="Полезная привычка",
            place="Место привычки",
            time_habit="2026-05-25T12:00",
            time_complete=120,
            periodicity=7,
            is_public=True,
            related_habit=self.rewards,
            owner=self.user,
        )

        self.client.force_authenticate(user=self.user)

    def test_rewards_create(self):
        url = reverse("kurs5:rewards-list")
        data = {
            "action": "Вознаграждение",
            "is_habit": False,
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rewards.objects.count(), 2)

    def test_rewards_list(self):
        url = reverse("kurs5:rewards-list")

        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {"id": self.rewards.pk, "action": "Приятная привычка", "is_habit": True, "owner": self.user.pk}
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 1)
        self.assertEqual(data, result)

    def test_habits_create(self):
        url = reverse("kurs5:habits-list")
        data = {
            "habit": "Полезная привычка 2",
            "place": "Место привычки",
            "time_habit": "2026-05-25T13:00",
            "time_complete": 120,
            "periodicity": 7,
            "is_public": True,
            "related_habit": self.rewards.pk,
        }

        response = self.client.post(url, data)
        created_habit = Habits.objects.get(habit="Полезная привычка 2")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.count(), 2)
        self.assertEqual(created_habit.owner, self.user)

    def test_habits_list(self):
        url = reverse("kurs5:habits-list")

        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "habit": "Полезная привычка",
                    "id": self.habits.pk,
                    "is_public": True,
                    "owner": self.user.pk,
                    "periodicity": 7,
                    "place": "Место привычки",
                    "related_habit": self.rewards.pk,
                    "time_complete": 120,
                    "time_habit": "2026-05-25T12:00:00+05:00",
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 1)
        self.assertEqual(data, result)

    def test_habits_list_returns_only_owner_habits(self):
        other_user = CustomUser.objects.create(username="otheruser", email="other@test.ru", password="456")

        related_habit = Rewards.objects.create(action="Чужая приятная привычка", is_habit=True, owner=other_user)

        Habits.objects.create(
            habit="Чужая полезная привычка",
            place="Другое место",
            time_habit="2026-05-25T14:00",
            time_complete=60,
            periodicity=1,
            is_public=False,
            related_habit=related_habit,
            owner=other_user,
        )

        url = reverse("kurs5:habits-list")
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["habit"], "Полезная привычка")
