from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class LegalService(models.Model):  # Работа с юр.лицами(выводить)
    service = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0)])
    objects = models.Manager()

    class Meta:
        verbose_name = u"Работы с юр.лицами"
        verbose_name_plural = u"Работы с юр.лицами"

    def __str__(self):
        return self.service


class CleanService(models.Model):  # Чистовая работа(выводить)
    service = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0)])
    objects = models.Manager()

    class Meta:
        verbose_name = u"Чистые работы"
        verbose_name_plural = u"Чистые работы"

    def __str__(self):
        return self.service


class DraftService(models.Model):  # Черновая работа(выводить)
    service = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0)])
    objects = models.Manager()

    class Meta:
        verbose_name = u"Грязные работы"
        verbose_name_plural = u"Грязные работы"

    def __str__(self):
        return self.service


class Review(models.Model):  # Отзывы(выводить)
    image_src = models.CharField(max_length=200)
    review = models.TextField()
    name_surname = models.CharField(max_length=50)
    objects = models.Manager()

    class Meta:
        verbose_name = u"Отзывы"
        verbose_name_plural = u"Отзывы"

    def __str__(self):
        return f'{self.name_surname}:  {self.review}'


class StageWork(models.Model):  # Стадии работ(не выводить)
    stage = models.CharField(max_length=30)
    description = models.TextField()
    number = models.IntegerField()
    objects = models.Manager()


class Advantages(models.Model):  # Преимущества(не выводить)
    image_src = models.CharField(max_length=200)
    text = models.CharField(max_length=50)
    objects = models.Manager()


class Navigate(models.Model):  # Меню(не выводить)
    link = models.CharField(max_length=150, null=True)
    menu_navigate = models.CharField(max_length=20)
    href = models.CharField(max_length=150, null=True)
    objects = models.Manager()
