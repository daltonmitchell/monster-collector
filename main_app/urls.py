from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('monsters/', views.monsters_index, name='index'),
    path('monsters/<int:monster_id>/', views.monsters_detail, name='detail'),
    path('monsters/create/', views.MonsterCreate.as_view(), name='monsters_create'),
    path('monsters/<int:pk>/update/', views.MonsterUpdate.as_view(), name='monsters_update'),
    path('monsters/<int:pk>/delete/', views.MonsterDelete.as_view(), name='monsters_delete'),
    path('monsters/<int:monster_id>/add_stat/', views.add_stat, name='add_stat'),
    path('monsters/<int:monster_id>/assoc_env/<int:env_id>/', views.assoc_env, name='assoc_env'),
    path('env/', views.EnvList.as_view(), name='env_index'),
    path('env/<int:pk>/', views.EnvDetail.as_view(), name='env_detail'),
    path('env/create/', views.EnvCreate.as_view(), name='env_create'),
    path('env/<int:pk>/update', views.EnvUpdate.as_view(), name='env_update'),
    path('env/<int:pk>/delete', views.EnvDelete.as_view(), name='env_delete'),
]