from django.urls import path
from . import views



app_name = 'core'
urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('bucket/', views.BucketHome.as_view(), name='bucket_home'),
	path('bucket_delete/<str:key>/', views.BucketDelete.as_view(), name='bucket_delete'),
	path('bucket_download/<str:key>/', views.BucketDownload.as_view(), name='bucket_download'),
]