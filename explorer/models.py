from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="UNKNOWN")
    author = models.CharField(max_length=200, default="UNKNOWN")
    img_link = models.CharField(max_length=200, default="UNKNOWN")
    category = models.CharField(max_length=200, default="UNKNOWN")
    short_desc = models.TextField(default="UNKNOWN")
    desc = models.TextField(default="UNKNOWN");
    website_link = models.CharField(max_length=200, default="UNKNOWN")
    collab = models.BooleanField(default=False)
    collab_link = models.CharField(max_length=200, default="", blank=True)
    country = models.CharField(max_length=200, default="UNKNOWN")
    on_wiki = models.BooleanField(default=False)
    wiki_link = models.CharField(max_length=200, default="", blank=True)
    
    def __str__(self):
        return "[" + str(self.id) + "] " + self.name
    