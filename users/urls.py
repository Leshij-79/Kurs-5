from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import UsersViewSet

app_name = UsersConfig.name

router_user = SimpleRouter()
router_user.register("", UsersViewSet)

urlpatterns = []

urlpatterns += router_user.urls
