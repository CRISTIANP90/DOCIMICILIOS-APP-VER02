from django import forms
from domiciliosapp.models import Productos

class ProductosForm(forms.ModelForm):
    DISTRIBUIDORES_CHOICES = [
        ('1', 'Jose'),
        ('2', 'Diana'),
        ('3', 'El Lider'),
        ('4', 'Fruver cruz'),
        ('5', 'Paquita la Del Barrio'),
    ]

    Cantidad_pro = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}))
    Precio_pro = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}))
    ID_distribu = forms.ChoiceField(choices=DISTRIBUIDORES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Productos
        fields = ['producto_ID', 'Nombre_pro', 'Cantidad_pro', 'Precio_pro', 'ID_distribu']
        widgets = {
            'producto_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombre_pro': forms.TextInput(attrs={'class': 'form-control'}),
        }