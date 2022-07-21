from django.db import models
from tabnanny import verbose

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="아이디어명")
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name="사진")
    description = models.TextField(verbose_name="아이디어 설명")
    interest = models.IntegerField(verbose_name="아이디어 관심도")
    expected_tool = models.CharField(max_length=50, verbose_name="예상 개발툴")