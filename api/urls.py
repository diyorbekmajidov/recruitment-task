from django.urls import path
from django.urls.conf import include
from .views import Register, UserLoginView, UserLogoutView
from .views import InvestorGet,InvistorApiview,InvestorUpdate
from .views import ProjectApiview, ProjectGet, ProjectUpdate

urlpatterns = [

    path('investor/<int:pk>/', InvestorGet.as_view()),
    path('invistorcreate/', InvistorApiview.as_view()),
    path('investorupdate/<int:pk>/', InvestorUpdate.as_view()),

    path('project/', ProjectApiview.as_view()),
    path('projectupdate/<int:pk>/', ProjectUpdate.as_view()),
    path('project/<int:pk>/', ProjectGet.as_view()),

    path('register/', Register.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]
    



