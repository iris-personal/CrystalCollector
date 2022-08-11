from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crystals/', views.crystals_index, name='index'),
    path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),
    path('crystals/create/', views.CrystalCreate.as_view(), name='crystals_create'),
    path('crystals/<int:pk>/update/', views.CrystalUpdate.as_view(), name='crystals_update'),
    path('crystals/<int:pk>/delete/', views.CrystalDelete.as_view(), name='crystals_delete'),
    path('crystals/<int:crystal_id>/add_cleansing/', views.add_cleansing, name='add_cleansing'),
    path('crystals/<int:crystal_id>/assoc_cut/<int:cut_id>/', views.assoc_cut, name='assoc_cut'),
    path('crystals/<int:crystal_id>/unassoc_cut/<int:cut_id>/', views.unassoc_cut, name='unassoc_cut'),
    path('cuts/', views.CutList.as_view(), name='cuts_index'),
    path('cuts/<int:pk>/', views.CutDetail.as_view(), name='cuts_detail'),
    path('cuts/create/', views.CutCreate.as_view(), name='cuts_create'),
    path('cuts/<int:pk>/update/', views.CutUpdate.as_view(), name='cuts_update'),
    path('cuts/<int:pk>/delete/', views.CutDelete.as_view(), name='cuts_delete'),
]