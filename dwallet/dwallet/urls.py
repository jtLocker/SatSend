from django.contrib import admin
from django.urls import path, include
from apiChug import views as apiViews
from wallet import views as walletViews
from social import views as socialViews
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', apiViews.UserViewSet)
router.register(r'groups', apiViews.GroupViewSet)
router.register(r'wallet', apiViews.WalletViewSet)

urlpatterns = [
    path('', walletViews.wallet, name = 'home'),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('wallets/', walletViews.wallet_list),
    path('wallets/<int:pk>/', walletViews.wallet_detail),
    path('friendship/', include('friendship.urls')), #testing
    path('social/', include('social.urls')),
    path('wallet/', include('wallet.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #django docs development solution for media
