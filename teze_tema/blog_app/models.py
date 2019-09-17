from django.db import models
from author_app.models import Author
# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    short_content = models.CharField(max_length=255)
    full_content = models.TextField()
    published_at=models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(Author,default="",on_delete=models.CASCADE)
    def __str__(self):
        return self.title
