from django.urls import path
from . import views



app_name = 'core'
urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('bucket/', views.BucketHome.as_view(), name='bucket_home'),
]