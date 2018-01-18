from rest_framework import serializers
from main_app.models import (
    Category,
    Product,
    ProductVersion,
    User,
    Cart,
    Order,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at',
                   'updated_at',
                   )


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=Category.objects.all(),
    #     slug_field='name'
    # )

    class Meta:
        model = Product
        exclude = ()


class ProductVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVersion
        exclude = ('created_at',
                   'updated_at',
                   )


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'last_login',
            'date_joined',
            'is_active',
            'groups',
            'user_permissions',
        )



class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        exclude = ()

    def create(self, validated_data):
        order = Order(
            user=validated_data['user'],
            delivery_address=validated_data['delivery_address'],
            delivery_date=validated_data['delivery_date'],
            product=validated_data['product'],
        )
        order.save()
        return order