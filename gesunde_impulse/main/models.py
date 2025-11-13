from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.level})"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    increment = models.IntegerField(default=1)  # how much this skill affects its attribute

    def __str__(self):
        return f"{self.name} ({self.level})"


class Task(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    increment = models.IntegerField(default=1)  # how much this task affects its skill

    def __str__(self):
        return self.name

