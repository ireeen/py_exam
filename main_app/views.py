from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as AuthUser

from main_app.serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductVersionSerializer,
    UserSerializer,
    CartSerializer,
    OrderSerializer,
)

from main_app.models import (
    Category,
    Product,
    ProductVersion,
    User,
    Cart,
    Order,
)


class CategoryView(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductVersionView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,):
    serializer_class = ProductVersionSerializer
    queryset = ProductVersion.objects.all()


class UserView(GenericViewSet,
               mixins.ListModelMixin,  # TODO: remove after tests are completed
                ):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.user
        queryset = User.objects.filter(username=username)
        return queryset


class CartView(GenericViewSet,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.CreateModelMixin,):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer

    def get_queryset(self):
        if self.request.user is not None:
            queryset = Cart.objects.filter(user_id=self.request.user)
            return queryset
        else:
            queryset = Cart.objects.all()
            return queryset


class OrderView(GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)