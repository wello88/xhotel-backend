
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookings.urls')), 
    path('api/', include('accounts.urls')), 
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/', include('media.urls')), 
    path('api/', include('review.urls')), 
    path('api/', include('contactus.urls')),
    path('api/', include('event.urls')),

]