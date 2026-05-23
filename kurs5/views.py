from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from kurs5.models import Habits, Rewards
from kurs5.paginators import PagePagination
from kurs5.serializers import HabitsSerializer, RewardsSerializer
from kurs5.services import send_telegram_message


class RewardsViewSet(ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer
    pagination_class = PagePagination

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

        send_telegram_message()

    def get_queryset(self):
        user = self.request.user

        return Rewards.objects.filter(owner=user)


class HabitsViewSet(ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = PagePagination

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

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
