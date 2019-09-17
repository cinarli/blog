from django.db import models
from blog_app.models import Blogs

# Create your models here.
class Comment(models.Model):
    full_name = models.CharField(max_length=255)
    email= models.EmailField()
    comment = models.TextField()
    blog_id = models.ForeignKey(Blogs,default="",on_delete=models.CASCADE)


    def __str__(self):
        return self.comment[:50] + "..."