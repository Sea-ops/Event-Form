from django.forms import ModelForm
from .models import List 

class List_FORM(ModelForm):
    class Meta:
        model = List
        fields = '__all__' # if not select '__all__' columns / ['column1', 'column2'] to choose columns
