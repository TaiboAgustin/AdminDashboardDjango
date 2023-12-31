from django.urls import path
from .views import SignUpViews, ProfileUpdateView, EmailUpdateView

urlpatterns = [
    path('signup/', SignUpViews.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/email/', EmailUpdateView.as_view(), name='profile_email'),
]
