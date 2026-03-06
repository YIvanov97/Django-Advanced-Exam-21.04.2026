from django import forms
from products.models import Product, Review


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