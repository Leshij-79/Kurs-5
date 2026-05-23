from rest_framework.viewsets import ModelViewSet

from kurs5.models import Rewards
from kurs5.paginators import PagePagination
from kurs5.serializers import RewardsSerializer


class RewardsViewSet(ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer
    pagination_class = PagePagination
