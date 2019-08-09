from django import forms
from .models import Chat1, Chat2
class ChatForm1(forms.ModelForm):
    class Meta:
        model=Chat1
        fields="__all__"

class ChatForm2(forms.ModelForm):
    class Meta:
        model=Chat2
        fields="__all__"
