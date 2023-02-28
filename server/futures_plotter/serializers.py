from rest_framework.serializers import ModelSerializer
from futures_plotter.models import FuturesDay

class FuturesDaySerializer(ModelSerializer):
    class Meta:
        model = FuturesDay
        fields = "__all__"
