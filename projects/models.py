from django.db import models

# Create your models here.
# this is done to set up the database.
# we will be able to see this in the admin page

class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery')
    link_git = models.URLField(max_length=200, null=True)
    link_view = models.URLField(max_length=200, null=True)
    
