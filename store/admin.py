from django.contrib import admin
from .models import Category, Tutorial, Student


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'total_price']
    prepopulated_fields = {'slug': ('name',)}
    
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass