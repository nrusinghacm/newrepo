from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Book,Borrower,Reviewer
from  .forms import BookForm,BorrowerForm,ReviewerForm,UserRegisterForm,TransactionForm
from django.contrib.auth.decorators import login_required
#from testapp import forms

# def register(request):
#     form=UserCreationForm()
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('/')
#         else:
#             form=UserCreationForm()
#     return render(request, 'users/register.html', {'form':form})

def register(request):
    form=UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Your accounthas been created Successfully! ')
            return redirect('login')
        else:
            form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def book_view(request):
    #form =forms.BookForm()
    if request.method == "POST":
        #form = forms.BookForm(request.POST)
        form = BookForm(request.POST)
        if form.is_valid:
            book=form.save(commit=True)
            return redirect('/list/')
    else:
        form = BookForm()
    return render(request, 'testapp/book.html', {'form':form})

def borrower_view(request):
    #form =forms.BorrowerForm()
    if request.method == "POST":
        form = forms.BorrowerForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
    else:
        form = BorrowerForm()
    return render(request, 'testapp/borrower.html', {'form':form})

def reviewer_view(request):
    form =forms.ReviewerForm()
    if request.method == "POST":
        form = forms.ReviewerForm(request.POST)
        if form.is_valid:
            form.save(commit=True)

    return render(request, 'testapp/reviewer.html', {'form':form})
def book_list_view(request):
    book_list=Book.objects.all()
    return render(request, 'testapp/book_list.html', {'book_list':book_list})

@login_required
def profile(request):
    return render(request, 'users/profile.html')


def transaction_view(request):
    form=TransactionForm()
    if request.method == "POST":
        form=TransactionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'testapp/transaction.html', {'form':form})
