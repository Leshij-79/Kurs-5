from django.contrib import admin

from kurs5.models import Habits, Rewards


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "habit",
        "place",
        "time_habit",
        "time_complete",
        "periodicity",
        "is_public",
        "related_habit",
        "owner",
    )

    search_fields = (
        "habit",
        "place",
    )
    list_filter = (
        "habit",
        "place",
    )


@admin.register(Rewards)
class RewardsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "action",
        "is_habit",
    )

    search_fields = (
        "action",
    )

    list_filter = (
        "action",
    )
