from django import forms

from .models import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name': ''}
        
class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
#Go back to the models page and see if I can fix the text feild to appear in the new_topping page
