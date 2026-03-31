from django import forms

from products.choices.category_choices import CategoryChoices
from products.models import Product, Review, Computer, Headphones, Keyboard, Laptop, Mouse, Speakers


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
        exclude = ['slug']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter product name',
                }
            ),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter product description',
                'rows': 3,
                'cols': 30,
            }),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter product price',
                }
            ),
            'category': forms.Select()
        }
        error_messages = {
            'image': {
                'required': 'Please select the product image.'
            },
            'name': {
                'required': 'Please enter the product name.'
            },
            'description': {
                'required': 'Please enter the product description.'
            },
            'price': {
                'required': 'Please enter the product price.'
            },
            'category': {
                'required': 'Please select a category.'
            }
        }

class LaptopDetailsForm(forms.ModelForm):
    class Meta:
        model = Laptop
        exclude = ['product']
        widgets = {
            "processor": forms.TextInput(attrs={
                'placeholder': 'Enter processor'
            }),
            "ram": forms.Select(),
            "storage": forms.Select(),
            "screen_size": forms.Select(),
            "gpu": forms.TextInput(attrs={
                'placeholder': 'Enter GPU'
            })
        }
        error_messages = {
            'processor': {
                'required': 'Please enter the processor.'
            },
            'ram': {
                'required': 'Please select the amount of RAM.'
            },
            'storage': {
                'required': 'Please select the storage capacity.'
            },
            'screen_size': {
                'required': 'Please select the size of the screen.'
            },
            'gpu': {
                'required': 'Please enter the GPU.'
            }
        }

class ComputerDetailsForm(forms.ModelForm):
    class Meta:
        model = Computer
        exclude = ['product']
        widgets = {
            "processor": forms.TextInput(attrs={
                'placeholder': 'Enter processor'
            }),
            "ram": forms.Select(),
            "storage": forms.Select(),
            "gpu": forms.TextInput(attrs={
                'placeholder': 'Enter GPU'
            })
        }
        error_messages = {
            'processor': {
                'required': 'Please enter the processor.'
            },
            'ram': {
                'required': 'Please select the amount of RAM.'
            },
            'storage': {
                'required': 'Please select the storage capacity.'
            },
            'gpu': {
                'required': 'Please enter the GPU.'
            }
        }

class KeyboardDetailsForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        exclude = ['product']
        widgets = {
            "switch_type": forms.TextInput(attrs={
                "placeholder": "Enter switch type"
            }),
            "keyboard_layout": forms.TextInput(attrs={
                "placeholder": "Enter keyboard layout"
            }),
        }
        error_messages = {
            'switch_type': {
                'required': 'Please enter the switch type.'
            },
            'keyboard_layout': {
                'required': 'Please enter the keyboard layout'
            }
        }

class MouseDetailsForm(forms.ModelForm):
    class Meta:
        model = Mouse
        exclude = ['product']
        widgets = {
            "dpi": forms.NumberInput(attrs={
                'placeholder': 'Enter DPI'
            })
        },
        error_messages = {
            'dpi': {
                'required': 'Please enter the DPI.'
            }
        }

class HeadphonesDetailsForm(forms.ModelForm):
    class Meta:
        model = Headphones
        exclude = ['product']
        widgets = {
            "battery_life": forms.TextInput(attrs={
                'placeholder': 'Enter battery life'
            })
        },
        error_messages = {
            'battery_life': {
                'required': 'Please enter the battery life.'
            }
        }

class SpeakersDetailsForm(forms.ModelForm):
    class Meta:
        model = Speakers
        exclude = ['product']
        widgets = {
            "power_output": forms.NumberInput(attrs={
                'placeholder': 'Enter power output'
            })
        },
        error_messages = {
            'power_output': {
                'required': 'Please enter the power output'
            }
        }

class ProductCreateForm(ProductBaseForm):
    pass

class ProductEditForm(ProductBaseForm):
    pass

class ProductDeleteForm(ProductBaseForm):
    pass

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        labels = {
            'content': 'Add Review'
        }
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your review',
                }
            )
        }

class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        labels = {
            'content': 'Edit Review'
        }