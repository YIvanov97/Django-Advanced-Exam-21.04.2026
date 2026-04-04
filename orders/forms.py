from django import forms
from orders.models import Order

class OrderBaseForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'city', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter address'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        }
        error_messages = {
            'first_name': {
                'required': 'Please enter your first name.',
            },
            'last_name': {
                'required': 'Please enter your last name.',
            },
            'address': {
                'required': 'Please enter your address.',
            },
            'city': {
                'required': 'Please enter your city.',
            },
            'phone_number': {
                'required': 'Please enter your phone number.',
            },
        }

class OrderCreateForm(OrderBaseForm):
    pass

class OrderEditForm(OrderBaseForm):
    pass

class OrderDeleteForm(OrderBaseForm):
    pass

class OrderStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']