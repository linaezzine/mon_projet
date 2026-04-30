from django.urls import path
from .views import (
    EtudiantListView, EtudiantDetailView, EtudiantCreateView, EtudiantUpdateView, EtudiantDeleteView,
    CoursListView, CoursDetailView, CoursCreateView, CoursUpdateView, CoursDeleteView,
    InscriptionListView, InscriptionDetailView, InscriptionCreateView, InscriptionUpdateView, InscriptionDeleteView
)
from django.contrib.auth import views as auth_views
app_name = 'contacts'

urlpatterns = [
    # Etudiant
    path('etudiants/', EtudiantListView.as_view(), name='etudiant_list'),
    path('etudiants/<int:pk>/', EtudiantDetailView.as_view(), name='etudiant_detail'),
    path('etudiants/ajouter/', EtudiantCreateView.as_view(), name='etudiant_add'),
    path('etudiants/modifier/<int:pk>/', EtudiantUpdateView.as_view(), name='etudiant_edit'),
    path('etudiants/supprimer/<int:pk>/', EtudiantDeleteView.as_view(), name='etudiant_delete'),

    # Cours
    path('cours/', CoursListView.as_view(), name='cours_list'),
    path('cours/<int:pk>/', CoursDetailView.as_view(), name='cours_detail'),
    path('cours/ajouter/', CoursCreateView.as_view(), name='cours_add'),
    path('cours/modifier/<int:pk>/', CoursUpdateView.as_view(), name='cours_edit'),
    path('cours/supprimer/<int:pk>/', CoursDeleteView.as_view(), name='cours_delete'),

    # Inscription
    path('inscriptions/', InscriptionListView.as_view(), name='inscription_list'),
    path('inscriptions/<int:pk>/', InscriptionDetailView.as_view(), name='inscription_detail'),
    path('inscriptions/ajouter/', InscriptionCreateView.as_view(), name='inscription_add'),
    path('inscriptions/modifier/<int:pk>/', InscriptionUpdateView.as_view(), name='inscription_edit'),
    path('inscriptions/supprimer/<int:pk>/', InscriptionDeleteView.as_view(), name='inscription_delete'),
]
