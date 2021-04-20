from django.contrib import admin
from .models import  Author, KeyWords, PaperInfo

# Register your models here.
@admin.register(KeyWords)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(PaperInfo)
class QuestionAdmin(admin.ModelAdmin):
    pass