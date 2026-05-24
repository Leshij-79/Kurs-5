from kurs5.models import Habits, Rewards
from users import serializers


class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = "__all__"
        read_only_fields = ("owner",)


class HabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = "__all__"
        read_only_fields = ("owner",)
