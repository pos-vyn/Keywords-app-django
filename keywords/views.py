from .models import Keyword, User, UserManager
from django.shortcuts import render
from rest_framework import generics
from rest_framework import  viewsets
from .serializers import KeywordSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse


objects = UserManager()


class KeywordsView(viewsets.ModelViewSet):
    
    serializer_class = KeywordSerializer
    queryset = Keyword.objects.all()
       
          
    def create(self, request, *args, **kwargs):
        data = request.data
        data_p = (data['descKeywords'])
        data_w = (data["prodKeywords"])
        data_key = []
        for p in data_p:
            for w in data_w:
                    data_key.append([p,p+' '+w])
                    data_key.append([p,w+' '+p])

        keyword = Keyword.objects.create(data=(data_key))
        keyword.save()
        print(type(keyword))
        serializer = KeywordSerializer(keyword)
        return JsonResponse(data_key, safe=False)
       
class RegistrationView(viewsets.ModelViewSet):
    
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


    def create(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.create_user(username=data['username'],email=data['email'], password=data['password'])
        user.save()
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
     


