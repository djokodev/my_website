from django.forms import ModelForm
from my_site.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']