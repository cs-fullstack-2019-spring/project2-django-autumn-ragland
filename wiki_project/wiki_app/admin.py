from django.contrib import admin
from .models import UserModel, EnrtyModel, RelatedItemModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(EnrtyModel)
admin.site.register(RelatedItemModel)
