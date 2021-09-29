from django.core.checks import messages
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from countries.models import Countries
from countries.serializers import countriesSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def countries_list(request):
    if(request.method == 'GET'):
        countries = Countries.objects.all()

        name = request.GET.get('name',None)
        if( name is not None):
            countries = countries.filter(name__icontains=name)
        
        countries_serializer = countriesSerializer(countries, many=True)
        return JsonResponse(countries_serializer.data,safe=False)

    elif (request.method == 'POST'):
        countries_data = JSONParser().parse(request)
        countries_serializer = countriesSerializer(data=countries_data)
        if(countries_serializer.is_valid()):
            countries_serializer.save()
            return JsonResponse(countries_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def countries_detail(request, pk):
    try:
        countries = Countries.objects.get(pk=pk)
    except Countries.DoesNotExist:
        return JsonResponse({'message': 'The country dose not exist'}, status=status.HTTP_404_NOT_FOUND)

    if(request.method == 'GET'):
        countries_serializer = countriesSerializer(countries)
        return JsonResponse(countries_serializer.data)

    elif(request.method == 'PUT'):
        countries_data = JSONParser().parse(request)
        countries_serializer = countriesSerializer(countries,data=countries_data)
        if(countries_serializer.is_valid()):
            countries_serializer.save()
            return JsonResponse(countries_serializer.data)
        return JsonResponse(countries_serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif(request.method == 'DELETE'):
        countries.delete()
        return JsonResponse({'message': 'Country was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)