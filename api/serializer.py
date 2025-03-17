from rest_framework import serializers
from store.models import User,Product



class signup(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        read_only_fields = ["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)  


class login(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"    
        
