from django import forms

from products.category_choices import CategoryChoices
from products.models import Product, Review


class ProductCategoryFilterForm(forms.Form):
    category = forms.ChoiceField(
        choices=[('', 'Select category')] + CategoryChoices.choices,
        required=False,
        widget=forms.Select(attrs={'class': 'select__field'})
    )

class ProductSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'input__field',
                'placeholder': 'Enter product name'
            }
        ),
    )

class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 6, 'rows': 5}),
            'category': forms.Select()
        }

class ProductCreateForm(ProductBaseForm):
    pass

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']

        labels = {
            'content': ''
        }

        widgets = {
            'content': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your review',
                }
            )
        }