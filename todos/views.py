from django.shortcuts import render
from rest_framework import generics
from . models import Todo
from . serializers import TodoSerialize

# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerialize

class DetailTodo(generics.RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerialize
