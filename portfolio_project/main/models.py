from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField('nom',max_length=200,unique=True)
    description = models.TextField()
    picture = models.URLField()
    link = models.URLField()
    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField('nom',max_length=50,unique=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    def __str__(self):
        self.name