
from machines.models import CoinsAvailable, Product, VendingMachine
from machines.serializers import CoinsAvailableSerializer, FullProductSerializer, ProductSerializer, VendingMachineSerializer
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
        serializer = VendingMachineSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
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


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request):
        serializer = ProductSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Product.objects.filter(
            vending_machine__manager=request.user)
        serializer = FullProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
