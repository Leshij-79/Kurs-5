from rest_framework.routers import SimpleRouter

from kurs5.apps import Kurs5Config
from kurs5.views import RewardsViewSet

app_name = Kurs5Config.name

rewards_router = SimpleRouter()
rewards_router.register("rewards", RewardsViewSet)

urlpatterns = [
]

urlpatterns += rewards_router.urls