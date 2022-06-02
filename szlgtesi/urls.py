from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path, include
from jelenletiv.views import foglalkozasview, indexview, alkalomview, alldeleteview, apiview

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),

    path('admin/', admin.site.urls),

    path('', include('django.contrib.auth.urls')),
    path('', indexview, name="index"),
    path('mindentorles/', alldeleteview, name="alldelete"),
    path('<str:fog>/', foglalkozasview, name="foglalkozas"),
    path('<str:fog>/<int:alk>/', alkalomview, name="alkalom"),

    path('api/post/jelenlet/',apiview)
]