
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookings.urls')), 
    path('api/', include('accounts.urls')), 
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/', include('media.urls')), 
    path('api/', include('review.urls')), 
    path('api/', include('contactus.urls')),
    path('api/', include('event.urls')),
    path('api/', include('profiel.urls')),
    path('', include('payment.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('admin_user.urls')),
    path('auth/', include('djoser.urls.jwt')),



]


urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)