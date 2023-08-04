from django.urls import path
from django.urls.conf import include
from .views import Register, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view())
]
    