from django import forms


class ContactForm(forms.Form):
    empid = forms.IntegerField()
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    # man = forms.IntegerField()
