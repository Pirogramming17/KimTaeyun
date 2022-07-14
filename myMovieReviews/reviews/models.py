from tabnanny import verbose
from django.db import models
from decimal import Decimal

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    release_yr = models.IntegerField(verbose_name="개봉년도")
    genre = models.CharField(max_length=50, verbose_name="장르")
    rating = models.DecimalField(max_digits=10, decimal_places=1, default=Decimal(0.0), verbose_name="별점")
    running_time = models.IntegerField(verbose_name="러닝타임")
    content = models.TextField(verbose_name="리뷰")
    director = models.CharField(max_length=100, verbose_name="감독")
    actors = models.CharField(max_length=100, verbose_name="배우")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)