from django.urls import path, include
from . import views
from . import api_views


app_name = 'core'

api_urls = [
	path('questions/', api_views.QuestionView.as_view()),
	path('questions/<int:pk>/', api_views.QuestionView.as_view())
]

urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('bucket/', views.BucketHome.as_view(), name='bucket_home'),
	path('bucket_delete/<str:key>/', views.BucketDelete.as_view(), name='bucket_delete'),
	path('bucket_download/<str:key>/', views.BucketDownload.as_view(), name='bucket_download'),
	path('api/', include(api_urls)),
]