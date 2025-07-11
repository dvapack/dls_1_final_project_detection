from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import RegisterUserView, GetUserHistoryView, UploadVideoView, AnalyzeVideoView, \
                    ResultView, LogoutView

urlpatterns = [
    path('users/register/', RegisterUserView.as_view(), name='register'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/history/', GetUserHistoryView.as_view(), name='history'),
    path('users/logout/', LogoutView.as_view(), name='logout'),

    path('upload/', UploadVideoView.as_view(), name='upload'),
    path('analyze/', AnalyzeVideoView.as_view(), name='analyze'),
    path('result/', ResultView.as_view(), name='result')
]
