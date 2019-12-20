from django.contrib.auth.models import User, Group
from wallet.models import Wallet
from rest_framework import serializers

### Auto Serializer

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'first_name', 'last_name']

### Explicit serializer 

# class WalletSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField(max_length=30, style={'base_template': 'textarea.html'})
#     last_name = serializers.CharField(max_length=30)
    
#     def create(self, validated_data):
#         """
#         Create and return a new Wallet instance, given the validated data.
#         """
#         return Wallet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing Wallet instance, given the validated data.
#         """
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.save()
#         return instance
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']