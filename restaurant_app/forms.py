# forms.py
from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'image_url', 'meal_type', 'price']

    name = forms.CharField(
        max_length=100,
        required=True,
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the menu item name',
                'class': 'form-control',
                'id': 'name'
            }
        )
    )
    description = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter the menu item description',
                'class': 'form-control',
                'id': 'description'
            }
        )
    )
    image_url = forms.URLField(
        required=True,
        label='Image URL',
        widget=forms.URLInput(
            attrs={
                'placeholder': 'Enter the image URL',
                'class': 'form-control',
                'id': 'image_url'
            }
        )
    )
    meal_type = forms.ChoiceField(
        choices=[
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ],  # Ensure your model defines MEAL_TYPES or adjust this accordingly
        required=True,
        label='Meal Type',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'meal_type'
            }
        )
    )
    price = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=True,
        label='Price',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter the price',
                'class': 'form-control',
                'id': 'price'
            }
        )
    )
