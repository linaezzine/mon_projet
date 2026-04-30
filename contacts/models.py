from django.db import models

from django.db import models

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.titre

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Relation ManyToMany : un étudiant peut suivre plusieurs cours
    cours = models.ManyToManyField("Cours", related_name="etudiants")

    def __str__(self):
        return self.nom


class Inscription(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant.nom} inscrit à {self.cours.titre}"
