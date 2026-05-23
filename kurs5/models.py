from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import CustomUser


class Rewards(models.Model):
    action = models.CharField(
        max_length=100,
        verbose_name="Название привычки/вознаграждения",
        help_text="Введите название привычки/вознаграждения",
    )

    is_habit = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Укажите признак приятной привычки",
    )

    owner = models.ForeignKey(
        CustomUser,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Владелец вознаграждения",
        help_text="Укажите владельца вознаглаждения",
    )

    class Meta:
        verbose_name = "Вознаграждение"
        verbose_name_plural = "Вознаграждения"
        ordering = ["action"]

    def __str__(self):
        return self.action


class Habits(models.Model):
    habit = models.CharField(
        max_length=100,
        verbose_name="Название привычки",
        help_text="Введите название привычки",
    )

    place = models.CharField(
        max_length=100,
        verbose_name="Место привычки",
        help_text="Введите место привычки",
    )

    time_habit = models.DateTimeField(
        verbose_name="Время привычки",
        help_text="Введите время привычки",
    )

    time_complete = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="Значение не может быть меньше 1"),
            MaxValueValidator(120, message="Значение не может быть больше 100"),
        ],
        default=120,
        verbose_name="Время на выполнение привычки в секундах",
        help_text="Введите время на выполнение привычки в секундах",
    )

    periodicity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="Значение не может быть меньше 1"),
            MaxValueValidator(7, message="Значение не может быть больше 7"),
        ],
        default=1,
        verbose_name="Периодичность привычки в днях",
        help_text="Введите периодичность привычки в днях",
    )

    is_public = models.BooleanField(
        default=False,
        verbose_name="Публичность привычки",
        help_text="Укажите публичность привычки",
    )

    related_habit = models.ForeignKey(
        Rewards,
        on_delete=models.PROTECT,
        related_name="related_habit",
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
    )

    owner = models.ForeignKey(
        CustomUser,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="habits_owner",
        verbose_name="Владелец привычки",
        help_text="Владелец привычки",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["habit"]

    def __str__(self):
        return self.habit
