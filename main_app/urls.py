from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from main_app.views import (
    CategoryView,
    ProductView,
    ProductVersionView,
    UserView,
    CartView,
    OrderView,
)


router = DefaultRouter()
router.register(r'categories', CategoryView)
router.register(r'products', ProductVersionView)
router.register(r'users', UserView, base_name='user')
router.register(r'cart', CartView, base_name='cart')
router.register(r'order', OrderView, base_name='cart')


urlpatterns = [
    # Auth:
    url(r'^auth/$', obtain_jwt_token),

    # Other endpoints:
    url(r'', include(router.urls))
]