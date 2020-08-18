from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/user/reg
    path('reg',views.reg_view),
    # 127.0.0.1:8000/user/login
    path('login', views.login_view),
    # 127.0.0.1:8000/user/logout
    path('logout', views.logout_view),
]
