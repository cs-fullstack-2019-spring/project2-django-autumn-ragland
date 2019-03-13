from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# user model
class UserModel(models.Model):
    name = models.CharField(max_length=500, default='')
    password = models.CharField(max_length=500, default='')
    email = models.EmailField(default='')
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


# entry model
class EnrtyModel(models.Model):
    title = models.CharField(max_length=500, default='')
    text = models.TextField(default='')
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images')
    user_model_fk = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


# related item model
class RelatedItemModel(models.Model):
    title = models.CharField(max_length=500, default='')
    text = models.TextField(default='')
    image = models.ImageField(upload_to='wiki_app/static/wiki_app/images')
    entry_model_fk = models.ForeignKey(EnrtyModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
