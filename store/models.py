from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.core.validators import FileExtensionValidator



class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-updated_at']


class Tutorial(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    teacher_name = models.CharField(max_length=150, blank=False, null=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_name")
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    description = models.TextField(blank=False, null=False)
    headings = models.TextField(blank=False, null=False)

    slug = models.SlugField(max_length=150, blank=False,
                            null=False, unique=True)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=0, blank=False, null=False)
    episode_price = models.DecimalField(
        max_digits=10, decimal_places=0, blank=False, null=False)
    total_price_online = models.DecimalField(
        max_digits=10, decimal_places=0, blank=False, null=False)
    episode_price_online = models.DecimalField(
        max_digits=10, decimal_places=0, blank=False, null=False)

    episode_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('store:product_details', args=[self.slug])

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-updated_at']


class Student(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    family = models.CharField(max_length=150, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    mobile = models.CharField(
        max_length=150, blank=False, null=False, unique=True)
    tutorial = models.CharField(max_length=150, blank=False, null=False)
    price_kharid = models.FloatField()
    def __str__(self) -> str:
        return self.name
