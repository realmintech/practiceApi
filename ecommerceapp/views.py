from django.shortcuts import render
from django.http import JsonResponse
from .models import Info
# Create your views here.

def home(request,*args, **kwargs) -> JsonResponse:
    full_info = Info.objects.all()
    infomation =[
        {
            "name": info.name,
            "age": info.age,
            "created":info.date_created,
            "updated":info.updated_at
        }
        for info in full_info
    ]
    #name = "Mariam"
    # info = [
    #     {
    #     "name" : "Mariam",
    #     "age" : 12,
    #     "school" : "futminna"
    # }
    # ]
    return JsonResponse(data=infomation, safe=False)


