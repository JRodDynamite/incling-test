from django.db import models


class School(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'school',)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, unique=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
