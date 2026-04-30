from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Etudiant, Cours, Inscription


# ------------------ Page d'accueil ------------------
def home(request):
    return render(request, 'contacts/home.html')


# ------------------ CRUD pour Etudiant ------------------
class EtudiantListView(LoginRequiredMixin, ListView):
    model = Etudiant
    template_name = 'contacts/etudiant_list.html'
    context_object_name = 'etudiants'

class EtudiantDetailView(LoginRequiredMixin, DetailView):
    model = Etudiant
    template_name = 'contacts/etudiant_detail.html'
    context_object_name = 'etudiant'

class EtudiantCreateView(LoginRequiredMixin, CreateView):
    model = Etudiant
    template_name = 'contacts/etudiant_form.html'
    fields = ['nom', 'email', 'cours']
    success_url = reverse_lazy('contacts:etudiant_list')

class EtudiantUpdateView(LoginRequiredMixin, UpdateView):
    model = Etudiant
    template_name = 'contacts/etudiant_form.html'
    fields = ['nom', 'email', 'cours']
    success_url = reverse_lazy('contacts:etudiant_list')

class EtudiantDeleteView(LoginRequiredMixin, DeleteView):
    model = Etudiant
    template_name = 'contacts/etudiant_confirm_delete.html'
    success_url = reverse_lazy('contacts:etudiant_list')


# ------------------ CRUD pour Cours ------------------
class CoursListView(LoginRequiredMixin, ListView):
    model = Cours
    template_name = 'contacts/cours_list.html'
    context_object_name = 'cours'

class CoursDetailView(LoginRequiredMixin, DetailView):
    model = Cours
    template_name = 'contacts/cours_detail.html'
    context_object_name = 'cours'

class CoursCreateView(LoginRequiredMixin, CreateView):
    model = Cours
    template_name = 'contacts/cours_form.html'
    fields = ['titre', 'description']
    success_url = reverse_lazy('contacts:cours_list')

class CoursUpdateView(LoginRequiredMixin, UpdateView):
    model = Cours
    template_name = 'contacts/cours_form.html'
    fields = ['titre', 'description']
    success_url = reverse_lazy('contacts:cours_list')

class CoursDeleteView(LoginRequiredMixin, DeleteView):
    model = Cours
    template_name = 'contacts/cours_confirm_delete.html'
    success_url = reverse_lazy('contacts:cours_list')


# ------------------ CRUD pour Inscription ------------------
class InscriptionListView(LoginRequiredMixin, ListView):
    model = Inscription
    template_name = 'contacts/inscription_list.html'
    context_object_name = 'inscriptions'

class InscriptionDetailView(LoginRequiredMixin, DetailView):
    model = Inscription
    template_name = 'contacts/inscription_detail.html'
    context_object_name = 'inscription'

class InscriptionCreateView(LoginRequiredMixin, CreateView):
    model = Inscription
    template_name = 'contacts/inscription_form.html'
    fields = ['etudiant', 'cours']
    success_url = reverse_lazy('contacts:inscription_list')

class InscriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = Inscription
    template_name = 'contacts/inscription_form.html'
    fields = ['etudiant', 'cours']
    success_url = reverse_lazy('contacts:inscription_list')

class InscriptionDeleteView(LoginRequiredMixin, DeleteView):
    model = Inscription
    template_name = 'contacts/inscription_confirm_delete.html'
    success_url = reverse_lazy('contacts:inscription_list')
