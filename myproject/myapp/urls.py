# myapp/urls.py
from django.urls import path
from . import views

from .views import ProtectedView
from .views import oauth2_callback, post_logout_redirect


urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('callback/', oauth2_callback, name='callback'),
    path('post-logout/', post_logout_redirect, name='post_logout_redirect'),
    path('callback/', views.callback_view, name='callback'),  # Add the callback URL

]

