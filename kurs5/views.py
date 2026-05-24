from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from kurs5.models import Habits, Rewards
from kurs5.paginators import PagePagination
from kurs5.serializers import HabitsSerializer, RewardsSerializer


class RewardsViewSet(ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer
    pagination_class = PagePagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user

        return Rewards.objects.filter(owner=user)


class HabitsViewSet(ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = PagePagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user

        return Habits.objects.filter(owner=user)


class PublicHabitsListAPIView(ListAPIView):
    queryset = Habits.objects.filter(is_public=True)
    serializer_class = HabitsSerializer
    pagination_class = PagePagination


class PublicHabitDetailAPIView(RetrieveAPIView):
    queryset = Habits.objects.filter(is_public=True)
    serializer_class = HabitsSerializer
