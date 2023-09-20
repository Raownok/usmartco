from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from usmartco import settings

from home import views

urlpatterns = [
    path("product/<int:pk>/",views.viewProduct , name = 'viewProduct'),
    path("<int:pk>/",views.viewFeaturedProduct , name = 'viewFeaturedProduct'),
    path("result/",views.searchResult , name = 'searchResult'),
    path("skinCare/",views.skinCare , name = 'skinCare'),
    path("hairCare/",views.hairCare , name = 'hairCare'),
    path("makeup/",views.makeup , name = 'makeup'),
    path("perfume/",views.perfume , name = 'perfume'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)