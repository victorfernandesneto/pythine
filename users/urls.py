from django.urls import path
from .views import IndexView, LoginFormView, CreateUserView, logout_view


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('logout/', logout_view, name='logout')    
]
