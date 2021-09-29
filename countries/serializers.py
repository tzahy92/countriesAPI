from django.db.models import fields
from rest_framework import serializers
from countries.models import Countries

class countriesSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Countries
        fields = ('id','name','capital')