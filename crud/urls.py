from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.user_home, name='home'),
    path('detail/<str:activity>', views.detail, name='detail'),
    path('update/<str:activity>', views.update, name='update'),
    path('delete/<str:activity>', views.delete, name='delete'),
    path('done/<str:activity>', views.done, name='done'),
    path('search', views.search, name='search'),
    path('signup', views.sign_up, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('api', views.crudApi, name='api'),
    path('accounts/', include('allauth.urls'))
]