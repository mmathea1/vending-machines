from machines.models import CoinsAvailable, MachineUser, VendingMachine
from rest_framework import serializers


class MachineUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineUser
        fields = ['username', 'email', 'is_staff']


class VendingMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendingMachine
        fields = '__all__'

    def validate(self, value):
        manager = value.get('manager')
        if not manager.is_admin or not manager.is_superuser or not manager.is_staff:
            raise serializers.ValidationError(
                'A manager must be a superuser or staff')
        return value


class CoinsAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinsAvailable
        fields = '__all__'
