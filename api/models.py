from django.db import models

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="postimages",null=True)
    user=models.CharField(max_length=25)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title