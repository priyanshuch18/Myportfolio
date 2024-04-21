from django.db import models

# Create your models here.

class Myinfo(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    image = models.ImageField()
    cv = models.FileField(upload_to='resume', blank=True)    #remaining
    def __str__(self):
        return self.name
class About(models.Model):
    image = models.ImageField()
    experience = models.TextField()
    education = models.TextField()
    description = models.TextField()
class FrontendSkill(models.Model):
    name = models.CharField(max_length=30)
    level = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']
        

    def __str__(self):
        return self.name
class BackendSkill(models.Model):
    name = models.CharField(max_length=30)
    level = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']
        

    def __str__(self):
        return self.name
class Projects(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)
    github_link = models.URLField()
    live_link = models.URLField()
    def __str__(self):
        return self.name


class Contact(models.Model):
    gmail_link = models.URLField()

    linkedin_link= models.URLField()

    github_link = models.URLField()
    def __str__(self):
        return self.gmail_link()


    

