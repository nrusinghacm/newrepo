from django.shortcuts import render, get_object_or_404, redirect
from testapp.models import Gpsdata
# from testapp.serializers import GpsdataSerializer
# from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
import socket
# import time

def send(request):
    IP = "127.0.0.1"
    PORT = 9000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP,PORT))
    while True:
        myObj = Gpsdata()
        data = s.recv(1024)  # buffer size is 1024 bytes
        #print("received message:", data)
        cordinate = data[:].decode("utf-8")
        #print(cordinate)
        myObj.latitude = cordinate
        myObj.save()
        #return redirect('/list/')
    return HttpResponse("<h1> Data Inserted Successfully</h1>")


# def data_list_view(request):
#     data_list=Gpsdata.objects.all()
#     return render(request,"testapp/data.html", {'data_list':data_list} )


# class GpsdataCRUD(ModelViewSet):
#     queryset=Gpsdata.objects.all()
#     serializer_class=GpsdataSerializer
