from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView

app_name = UsersConfig.name

# router = SimpleRouter()
# router.register("", UsersViewSet)

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    # path("payments/", UserPaymentListAPIView.as_view(), name="payments_list"),
    # path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    # path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
]