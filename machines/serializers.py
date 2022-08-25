from machines.models import CoinsAvailable, MachineUser, Product, VendingMachine, generate_random_code
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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'vending_machine']

    def validate(self, value):
        if self.context['user'] != value.get('vending_machine').manager:
            raise serializers.ValidationError(
                'You must be a manager to this vending machine')
        return value

    def create(self, validated_data):
        validated_data['code'] = generate_random_code()
        return Product.objects.create(**validated_data)


class FullProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
