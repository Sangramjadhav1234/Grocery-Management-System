from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'class': 'form-control'
    }))
    mobile_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your mobile number',
        'class': 'form-control'
    }))