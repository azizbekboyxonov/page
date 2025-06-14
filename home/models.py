from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=20)
    subjects = models.ManyToManyField(Subject, related_name='student')

    def str(self):
        return self.full_name