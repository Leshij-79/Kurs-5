from kurs5.models import Rewards
from users import serializers


class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = '__all__'
