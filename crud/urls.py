from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<str:activity>', views.detail, name='detail'),
    path('update/<str:activity>', views.update, name='update'),
    path('delete/<str:activity>', views.delete, name='delete'),
    path('done/<str:activity>', views.done, name='done'),
    path('search', views.search, name='search'),
    path('api', views.crudApi, name='api'),
]