from django.db import models


class Article(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Statyua')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Добавить Анонс'


class Applications(models.Model):
    lastname = models.CharField('lastname', max_length=15)
    firstname = models.CharField('firstname', max_length=15)
    thirdname = models.CharField('thirdname', max_length=15)
    job = models.TextField('job')
    placejob = models.TextField('placejob')
    theme = models.TextField('theme')
    header = models.TextField('header')
    full_text = models.TextField('full_text')

    def __str__(self):
        return self.lastname
