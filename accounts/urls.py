from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
urlpatterns = [
    path('register/', views.UserRegistrationView.as_view()),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'), #Obtain both Access & refresh tokens
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), #returns new refresh token and blacklist the previos refresh token 
    path('login/', views.UserLoginView.as_view()),
    path('logout/', views.BlacklistRefreshView.as_view()),
    path('profile/', views.UserProfileView_class.as_view()),

]