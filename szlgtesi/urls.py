from django.contrib import admin
from django.urls import path, include
from jelenletiv.views import foglalkozasview, indexview, alkalomview, alldeleteview, apiview

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('django.contrib.auth.urls')),
    path('', indexview, name="index"),
    path('mindentorles/', alldeleteview, name="alldelete"),
    path('<str:fog>/', foglalkozasview, name="foglalkozas"),
    path('<str:fog>/<int:alk>/', alkalomview, name="alkalom"),

    path('api/post/jelenlet/',apiview)
]