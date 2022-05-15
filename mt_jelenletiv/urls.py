from django.contrib import admin
from django.urls import path, include
from jelenletiv.views import indexview, alkalomview

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('django.contrib.auth.urls')),
    path('', indexview, name="index"),
    path('<str:fog>/<int:alk>/', alkalomview, name="alkalom"),
]
