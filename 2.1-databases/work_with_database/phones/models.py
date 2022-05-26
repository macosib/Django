from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(default='', null=False)

    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} {self.price} {self.release_date} {self.slug}'


