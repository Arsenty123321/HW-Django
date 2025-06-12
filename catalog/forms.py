from django.forms import ModelForm, forms, BooleanField
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


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
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

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price
