from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import ContactWithMe, AboutMe, Blog

class ContactForm(ModelForm):
    class Meta:
        model = ContactWithMe
        fields = '__all__'


class FormFromSomeModel(ModelForm):
    class Meta:
        model = AboutMe
        widgets = {
            'text': SummernoteWidget(),
        }
        fields = '__all__'


class BlogModel(ModelForm):
    class Meta:
        model = Blog
        widgets = {
            'text': SummernoteWidget(),
        }
        fields = '__all__'