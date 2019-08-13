from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Borrower, Reviewer,Transaction

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    firstname=forms.CharField()
    lastname=forms.CharField()
    class Meta:
        model = User
        fields=['username','email','firstname','lastname','password1','password2']

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"

class BorrowerForm(forms.ModelForm):
    class Meta:
        model=Borrower
        fields="__all__"

class ReviewerForm(forms.ModelForm):
    class Meta:
        model=Reviewer
        fields="__all__"
class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"
