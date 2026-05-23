from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "pk",
        "username",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "city",
        "tg_id",
        "is_staff",
        "is_active",
        "date_joined",
        "is_superuser",
    )

    search_fields = (
        "username",
        "email",
        "phone_number",
    )

    list_filter = ("email",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Дополнительная информация",
            {
                "fields": ("phone_number", "city", "tg_id"),
            },
        ),
    )
