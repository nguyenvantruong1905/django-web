from django.db import models

# Create your models here.

class Author(models.Model):
    firt_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country_region = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    email = models.EmailField()
    corresponding_author = models.CharField(max_length=200)
    
class KeyWords(models.Model):
    keywords = models.CharField(max_length=200)



class PaperInFo(models.Model):
    author_info = models.ForeignKey(Author, on_delete=models.CASCADE)
    submission_type = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=200)
    keywords = models.ForeignKey(KeyWords, on_delete=models.CASCADE)
    file = models.FileField(upload_to=None, max_length=254)

