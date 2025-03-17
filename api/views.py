from django.shortcuts import render
from rest_framework.views import APIView
from api.serializer import signup,login,Productserializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from store.models import Product
from rest_framework import status



class signupview(APIView):
    def post(self,request,*args,**kwargs):

        serializer=signup(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class taskviewset(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Product.objects.all()
        serilizers=Productserializer(qs,many=True)
        return Response(data=serilizers.data,status=status.HTTP_202_ACCEPTED)
    
    def create(self,request,*args,**kwargs):
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_402_PAYMENT_REQUIRED)
        

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serilaizer=Productserializer(qs)
        return Response(data=serilaizer.data,status=status.HTTP_202_ACCEPTED) 

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Product.objects.get(id=id).delete()
        return Response(status=status.HTTP_301_MOVED_PERMANENTLY)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serilalizer=Productserializer(data=request.data,instance=qs)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(data=serilalizer.data)
        else:
          return Response(data=serilalizer.errors)

