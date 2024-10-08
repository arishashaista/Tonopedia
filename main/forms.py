from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            name = strip_tags(name)
            return name
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description:
            description = strip_tags(description)
            return description
        return description
