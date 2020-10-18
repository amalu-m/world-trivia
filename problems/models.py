from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.TextField()
    country = models.ForeignKey(Country,related_name ='questions',on_delete = models.CASCADE)
    def __str__(self):
        return self.Title

class Answer(models.Model):
    option1 = models.CharField(max_length = 200)
    option2 = models.CharField(max_length = 200)
    option3 = models.CharField(max_length = 200)
    option4 = models.CharField(max_length = 200)
    correct = models.CharField(max_length = 200)
    question = models.ForeignKey(Question,related_name = 'answers',on_delete =models.CASCADE)
