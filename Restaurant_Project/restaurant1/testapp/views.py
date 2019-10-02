from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from testapp.models import Restaurant
from  .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import *
import requests
import json


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
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch :
            match = Restaurant.objects.filter(Q(city__icontains=srch) | Q(locality__icontains=srch))
            paginator = Paginator(match, 12)
            page_number = request.GET.get('page')
            try:
                match = paginator.page(page_number)
            except PageNotAnInteger:
                match = paginator.page(1)
            except EmptyPage:
                match = paginator.page(paginator.num_pages)
            if match :
                return render(request,'testapp/search.html', {'sr':match})
            else:
                messages.error(request,'no results found')
        else:
            return HttpResponseRedirect('/home/')
    return render(request,'testapp/search.html')
@login_required
def data_save():
    cities=['Bengaluru','Hyderabad','Mumbai','Delhi','Chennai']
    headers = {
            "cache-control": "no-cache",
            "user-key": "17c5d22ee5ac8d2406d53afcde18a594"}
    for city in cities:
            url="https://developers.zomato.com/api/v2.1/cities?q="+city
            resp = requests.request("GET",url,headers=headers)
            txt = resp.text
            data = json.loads(txt)
            for item in data['location_suggestions']:
                myObj = Restaurant()
                myObj.res_id = item['id']
                myObj.address = item['address']
                myObj.locality = item['locality']
                myObj.city = item['city']
                myObj.name = item['name']
    return HttpResponse("<h1> Data Inserted Successfully</h1>")
    data_save()
