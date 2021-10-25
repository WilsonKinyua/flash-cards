from django.forms import ModelForm
from .models import Subject,Notes

class EntryForm(ModelForm):
    class Meta:
        model = Notes
        fields = ('user','title','description','subject' )
        exclude = ['created_at','updated_at']