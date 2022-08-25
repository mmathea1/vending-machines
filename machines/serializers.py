from machines.models import CoinsAvailable, MachineUser, VendingMachine
from rest_framework import serializers


class VendingMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendingMachine
        fields = '__all__'


class MachineUserSerializer(serializers.Serializer):
    class Meta:
        model = MachineUser
        fields = '__all__'


class CoinsAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinsAvailable
        fields = '__all__'
