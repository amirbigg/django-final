from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,	TokenRefreshView


app_name = 'accounts'

api_urls = [
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
	path('register/', views.UserRegister.as_view(), name='register'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.UserLogout.as_view(), name='logout'),
	path('dashboard/<str:username>/', views.UserDashboard.as_view(), name='dashboard'),
	path('api/', include(api_urls)),
]
