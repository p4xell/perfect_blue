from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from perfect_blue import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls', namespace='orders')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('flowers.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
