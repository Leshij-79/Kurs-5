from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import CustomUser
from users.paginators import UserPagePagination
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    pagination_class = UserPagePagination

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class UsersViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #
    #     if user.groups.filter(name="Moderator").exists():
    #         return CustomUser.objects.all()
    #
    #     return CustomUser.objects.filter(email=user)
