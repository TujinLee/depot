from django import forms
from models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
