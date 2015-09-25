from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from carts.views import (
        CartAPIView,
        CartView, 
        CheckoutAPIView,
        CheckoutFinalizeAPIView,
        CheckoutView, 
        CheckoutFinalView,
        ItemCountView, 
        )
from orders.views import (
                    AddressSelectFormView, 
                    UserAddressCreateView,
                    UserAddressCreateAPIView,
                    UserAddressListAPIView,
                    UserCheckoutAPI,
                    OrderList,
                    OrderListAPIView, 
                    OrderDetail,
                    OrderRetrieveAPIView,
                    )

from products.views import (
        APIHomeView,
        CategoryListAPIView,
        CategoryRetrieveAPIView,
        ProductListAPIView,
        ProductRetrieveAPIView,

    )

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'ecommerce2.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('products.urls_categories')),
    url(r'^orders/$', OrderList.as_view(), name='orders'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^checkout/address/$', AddressSelectFormView.as_view(), name='order_address'),
    url(r'^checkout/address/add/$', UserAddressCreateView.as_view(), name='user_address_create'),
    url(r'^checkout/final/$', CheckoutFinalView.as_view(), name='checkout_final'),

]


#API Patterns
urlpatterns += [
    url(r'^api/$', APIHomeView.as_view(), name='home_api'),

    url(r'^api/cart/$', CartAPIView.as_view(), name='cart_api'),
    url(r'^api/checkout/$', CheckoutAPIView.as_view(), name='checkout_api'),
    url(r'^api/checkout/finalize/$', CheckoutFinalizeAPIView.as_view(), name='checkout_finalize_api'),
    url(r'^api/auth/token/$', 'rest_framework_jwt.views.obtain_jwt_token', name='auth_login_api'),
    url(r'^api/auth/token/refresh/$', 'rest_framework_jwt.views.refresh_jwt_token', name='refresh_token_api'),
    url(r'^api/user/address/$', UserAddressListAPIView.as_view(), name='user_address_list_api'),
    url(r'^api/user/address/create/$', UserAddressCreateAPIView.as_view(), name='user_address_create_api'),
    url(r'^api/user/checkout/$', UserCheckoutAPI.as_view(), name='user_checkout_api'),
    url(r'^api/categories/$', CategoryListAPIView.as_view(), name='categories_api'),
    url(r'^api/categories/(?P<pk>\d+)/$', CategoryRetrieveAPIView.as_view(), name='category_detail_api'),
    url(r'^api/orders/$', OrderListAPIView.as_view(), name='orders_api'),
    url(r'^api/orders/(?P<pk>\d+)/$', OrderRetrieveAPIView.as_view(), name='order_detail_api'),
    url(r'^api/products/$', ProductListAPIView.as_view(), name='products_api'),
    url(r'^api/products/(?P<pk>\d+)/$', ProductRetrieveAPIView.as_view(), name='products_detail_api'),
]



if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)