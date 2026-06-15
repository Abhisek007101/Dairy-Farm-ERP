from django.forms import ModelForm
from .models import Milk

class MilkForm(ModelForm):
    class Meta:
        model = Milk
        fields = "__all__"