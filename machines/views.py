
from machines.models import CoinsAvailable, VendingMachine, MachineUser
from machines.serializers import CoinsAvailableSerializer, VendingMachineSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class VendingMachineViewSet(viewsets.ViewSet):
    queryset = VendingMachine.objects.all()
    serializer_class = VendingMachineSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        data = request.data.copy()
        serializer = VendingMachineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoinsAvailableViewSet(viewsets.ViewSet):
    queryset = CoinsAvailable.objects.all()
    serializer_class = CoinsAvailableSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = CoinsAvailableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = CoinsAvailable.objects.filter(
            vending_machine__manager=self.request.user)
        serializer = CoinsAvailableSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
