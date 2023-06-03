from django.urls import path
from .views import (LoginView, RegisterView, LogoutView)


urlpatterns = [
    path(
        route='login/',
        view=LoginView.as_view(),
        name='login_page',
    ),
    
    path(
        route='register/',
        view=RegisterView.as_view(),
        name='register_page',
    ),
    
    path(
        route='logout/',
        view=LogoutView.as_view(),
        name='logout_view'
    ),
]
