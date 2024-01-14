from django.db import models

# Create your models here.


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.song} by {self.singer}'


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.email
