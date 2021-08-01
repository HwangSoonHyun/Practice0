from django.forms import ModelForm


class ProfileCreationForm(ModelForm):
    class Meta:
        model = ProfileCreationFormfields = ['image', 'nickname', 'message']