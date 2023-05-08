from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    path('register/', views.AccountRegisterView.as_view()),
    path('login/', views.LoginView.as_view()),

    path('my/account/', views.MyAccountApiView.as_view()),
    path('retrieve-update/<int:pk>/', views.AccountRetrieveUpdateView.as_view()),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
