from django.forms import ModelForm, forms
from .models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name:
            self.validate_forbidden_words(name, 'name')
        if description:
            self.validate_forbidden_words(description, 'description')
        return cleaned_data

    def validate_forbidden_words(self, value, field):
        for word in FORBIDDEN_WORDS:
            if word.lower() in value.lower():
                self.add_error(field, f"Слово '{word}' запрещено.")
