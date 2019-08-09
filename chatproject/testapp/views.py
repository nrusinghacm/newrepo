from django.shortcuts import render
from .models import Chat1, Chat2
from testapp import forms

def input(request):
    response2=''
    response1=''
    chat1form=forms.ChatForm1()
    chat2form=forms.ChatForm2()
    if request.method=="POST":
        chat1form=forms.ChatForm1(request.POST)
        chat2form=forms.ChatForm2(request.POST)
        # if chat1form.is_valid() or chat2form.is_valid():
        #     chat1form.save()
        #     chat2form.save()
        if chat1form.is_valid():
            chat1form.save()
            response1=chat1form.cleaned_data['text']
        if chat2form.is_valid():
            chat2form.save()
            response2=chat2form.cleaned_data['text']
    my_dict={'chat1form':chat1form,'chat2form':chat2form,'response1':response1,'response2':response2}

    return render(request, 'testapp/input.html',context=my_dict )
