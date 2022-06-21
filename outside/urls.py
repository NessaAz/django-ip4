from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name='main'),
    path('explore/', views.explore, name='explore'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('hoods/', views.hoods, name='hoods'),
    path('business/', views.business, name='business'),
    path('business/<businessname>', views.businessdetail, name='businessdetail'),
    # path('<int:pk>/', views.business, name='businessdetail'),
    path('profile/<username>', views.profile, name='profile'),
    path('post/', views.post, name='post'),




]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
