from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home,name='home'),
    path('index',views.index, name='home'),
    path('', views.profile, name='uprofile'),
    path('search/', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)