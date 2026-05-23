from kurs5.models import Habits, Rewards
from users import serializers


class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = "__all__"


class HabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = "__all__"
