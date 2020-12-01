from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'accounts'

api_urls = [
	path('token-auth/', obtain_auth_token),
]

urlpatterns = [
	path('register/', views.UserRegister.as_view(), name='register'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.UserLogout.as_view(), name='logout'),
	path('dashboard/<str:username>/', views.UserDashboard.as_view(), name='dashboard'),
	path('api/', include(api_urls))
]