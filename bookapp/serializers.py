from .models import *
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError


class AuthorSerializer(serializers.ModelSerializer):	
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Book
        fields = '__all__'
