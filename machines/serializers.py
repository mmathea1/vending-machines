from email.policy import default
from machines.models import CoinsAvailable, MachineUser, Product, ProductOrder, VendingMachine, generate_random_code
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


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['product', 'amount_paid']

    def validate(self, value):
        user = self.context['user']
        try:
            product = Product.objects.get(code=value['product'].code)
            vm = product.vending_machine
            if value.get('amount_paid') < product.price:
                raise serializers.ValidationError(
                    'Amount paid is less than the price of the product.')
            if product.quantity < 1:
                raise serializers.ValidationError('Product is out of stock')
            if user != vm.manager:
                raise serializers.ValidationError(
                    'You cannot order from this vending machine')
        except Product.DoesNotExist:
            raise serializers.ValidationError('v Product does not exist.')
        return value

    def create(self, validated_data):
        amount_paid = validated_data['amount_paid']
        product = validated_data['product']
        change_given = amount_paid - product.price
        # TODO decrease coins available
        p_order = ProductOrder.objects.create(
            product=product,
            customer=self.context['user'],
            amount_paid=amount_paid,
            change_given=change_given
        )
        p_order.order_status = 'COMPLETE'
        p_order.save()
        product.quantity = product.quantity - 1
        product.save()
        return p_order


class FullProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'
