from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.DO_NOTHING,)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)

class Users(models.Model):
    first_name = models.CharField(max_length=264,unique=False)
    last_name = models.CharField(max_length=264,unique=False)
    email = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
