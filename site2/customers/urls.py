from django.urls import path
from .views import signup, set_session, get_session, del_session, set_cookie, get_cookie, del_cookie
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('set-session/', set_session, name='set_session'),
    path('get-session/', get_session, name='get_session'),
    path('del-session/', del_session, name='del_session'),
    path('set-cookie/', set_cookie, name='set_cookie'),
    path('get-cookie/', get_cookie, name='get_cookie'),
    path('del-cookie/', del_cookie, name='del_cookie'),
]