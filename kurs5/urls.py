from django.urls import path
from rest_framework.routers import SimpleRouter

from kurs5.apps import Kurs5Config
from kurs5.views import HabitsViewSet, PublicHabitDetailAPIView, PublicHabitsListAPIView, RewardsViewSet

app_name = Kurs5Config.name

rewards_router = SimpleRouter()
rewards_router.register("rewards", RewardsViewSet)

habits_router = SimpleRouter()
habits_router.register("", HabitsViewSet)

urlpatterns = [
    path("public/", PublicHabitsListAPIView.as_view(), name="public-list"),
    path("public/<int:pk>/", PublicHabitDetailAPIView.as_view(), name="public-detail"),
]

urlpatterns += rewards_router.urls
urlpatterns += habits_router.urls
