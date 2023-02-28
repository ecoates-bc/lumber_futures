from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from futures_plotter.models import FuturesDay
from futures_plotter.serializers import FuturesDaySerializer


class FuturesData(APIView):
    def get(self, *args):
        if not FuturesDay.objects.exists():
            return Response(
                "No futures data on server.",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        
        serializer = FuturesDaySerializer(
            FuturesDay.objects.all(),
            many=True
        )

        for elem in serializer.data:
            elem.pop("id")

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
