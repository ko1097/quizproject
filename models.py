from django.db import models


class Socialquestion(models.Model):
    question = models.CharField(max_length=264)
    answer = models.CharField(max_length=264)
    optionone = models.CharField(max_length=264)
    optiontwo = models.CharField(max_length=264)
    optionthree = models.CharField(max_length=264)
    optionfour = models.CharField(max_length=264)
    duration = models.DurationField()

    def __str__(self):
        return self.question

class Mathsquestion(models.Model):
    question = models.CharField(max_length=264)
    answer = models.CharField(max_length=264)
    optionone = models.IntegerField()
    optiontwo = models.IntegerField()
    optionthree = models.IntegerField()
    optionfour = models.IntegerField()
    duration = models.DurationField()

    def __str__(self):
        return self.question

# Create your models here.
