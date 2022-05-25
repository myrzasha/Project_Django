from django.db import models

class FeedBack(models.Model):
    pass

class Product(models.Model):
    file = models.FileField(
        upload_to='image/%Y/%m/%d',
        blank=True
    )
    shapka = models.CharField(
        max_length=255,
        blank=True,
        db_index=True
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True
    )
    description = models.TextField(
        blank=True
    )
    description_2 = models.TextField(
        blank=True
    )
    description_3 = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.title

class Image(models.Model):
    image_1 = models.FileField()
    image_2 = models.FileField()
    image_3 = models.FileField()
    image_5 = models.FileField()
    image_6 = models.FileField()
    image_7 = models.FileField()

class Post(models.Model):
    file = models.FileField(
        upload_to='image/%Y/%m/%d',
        blank=True
    )
    shapka = models.CharField(
        max_length=255,
        blank=True,
        db_index=True
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True
    )
    description = models.TextField(
        blank=True
    )

class Post_2(models.Model):
    file = models.FileField(
        upload_to='image/%Y/%m/%d',
        blank=True
    )
    shapka = models.CharField(
        max_length=255,
        blank=True,
        db_index=True
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True
    )
    description = models.TextField(
        blank=True
    )

class Post_3(models.Model):
    file = models.FileField(
        upload_to='image/%Y/%m/%d',
        blank=True
    )
    shapka = models.CharField(
        max_length=255,
        blank=True,
        db_index=True
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True
    )
    description = models.TextField(
        blank=True
    )