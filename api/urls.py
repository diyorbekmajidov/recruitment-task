from django.urls import path
from django.urls.conf import include
from .views import Register, UserLoginView, UserLogoutView
from .views import Invistor,InvestorUpdate
from .views import ProjectApiview

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),

    path('investor/', Invistor.as_view()),
    path('investor/<int:pk>/', InvestorUpdate.as_view()),

    path('project/', ProjectApiview.as_view())
]
    



