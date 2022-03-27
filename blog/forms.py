from django import forms


class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.SlugField(max_length=50)
