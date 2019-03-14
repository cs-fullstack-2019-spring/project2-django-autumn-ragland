from django import forms
from .models import UserModel, EnrtyModel, RelatedItemModel


# user form to add
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['user_fk']


# entry form to add or edit
class EntryForm(forms.ModelForm):
    class Meta:
        model = EnrtyModel
        exclude = ['user_model_fk', 'update_date', 'create_date']


# related item form to add or edit
class RelatedItemForm(forms.ModelForm):
    class Meta:
        model = RelatedItemModel
        exclude = ['entry_model_fk', 'update_date', 'create_date']
