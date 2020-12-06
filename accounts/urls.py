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
	path('api/', include(api_urls))
]


# {
# 	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwNzMzNzMyMywianRpIjoiMWM3ZDU5NDAzNWM5NGFiN2JhZGEzNWEzYjhkMmJmMzAiLCJ1c2VyX2lkIjoxfQ.Mx0TTz-ubdPpC5hMALjxZH0OugR_GUjM64owlZTECMY",
# 	"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA3MjUxMjIzLCJqdGkiOiI3ZTNiNDFkYmRlM2M0ZWM1YmM0NmI2ZTJhNTI4NTgyOCIsInVzZXJfaWQiOjF9.gNOd6ILBheGtgVHfjeDoP-LkbXHtloMUZ0DYXrKE4h0"
# }