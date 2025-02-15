from django import forms
from site_app.models import Category, Product, Contact


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {
            'name': 'Название категории',
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'author', 'complexity']
        labels = {
            'name': 'Название статьи',
            'description': 'Описание товара',
            'category': 'Категории',
            'author': 'Автор',
            'complexity': 'Сложность освоения',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Имя',
            'email': 'E-mail',
            'message': 'Сообщение',
        }
