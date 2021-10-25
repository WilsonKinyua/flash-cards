from django.forms import ModelForm
from .models import Subject,Notes

class EntryForm(ModelForm):
    class Meta:
        model = Subject
        fields = ('title','description','subject' )