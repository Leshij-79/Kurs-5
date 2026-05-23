from rest_framework.viewsets import ModelViewSet

from kurs5.models import Rewards
from kurs5.paginators import PagePagination
from kurs5.serializers import RewardsSerializer


class RewardsViewSet(ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer
    pagination_class = PagePagination

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_queryset(self):
        user = self.request.user

        return Rewards.objects.filter(owner=user)


