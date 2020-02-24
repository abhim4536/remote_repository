from django.db import models


class DiaryData(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='images/', max_length=100, blank=True)
    img1 = models.ImageField(upload_to='images/', max_length=100, blank=True)
    img2 = models.ImageField(upload_to='images/', max_length=100, blank=True)
    img3 = models.ImageField(upload_to='images/', max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str('title')
