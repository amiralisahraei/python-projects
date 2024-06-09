from django.db import models
from django.utils.text import slugify


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    married = models.BooleanField(null=True, db_column='marriage')
    joined_date = models.DateField(null=True)
    user_image = models.ImageField(null=True, upload_to="images/")
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        # Automatically generate the slug when saving the object
        self.slug = slugify(f"{self.firstname} {self.lastname}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
