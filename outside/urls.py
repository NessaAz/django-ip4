from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name='main'),
    path('explore/', views.explore, name='explore'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),


]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
