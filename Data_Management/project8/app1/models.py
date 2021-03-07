

from django.db import models


class Emp(models.Model):
    emp = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    mail = models.EmailField(max_length=40)
    objects: models.Manager()

    def __str__(self):
        return self.name


class Man(models.Model):
    emp = models.ForeignKey(Emp, on_delete=models.CASCADE)
    man = models.IntegerField(primary_key=True)
    objects: models.Manager()

    def __str__(self):
        return self.man
