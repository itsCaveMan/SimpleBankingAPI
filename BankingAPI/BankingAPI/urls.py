from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('Main.urls')),
    path('', lambda r: redirect('api/v1/docs'))

]
