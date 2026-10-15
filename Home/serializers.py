from .models import Profile, Transaction
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        user = instance 
        if 'password' in validated_data:
            password = validated_data.pop('password')
            user.set_password(password)
            user.save()
            return user

    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name', 'email', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'full_name', 'email', 'address', 'phone_number', 'joined_date']

class TransactionSerializer(serializers.ModelSerializer):
    # user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = Transaction
        fields = ['id','amount', 'type', 'remarks', 'date']


    def validate_amount(self,data):
         if data <=0:
              raise serializers.ValidationError("Amount should be greater than 1")
         if data > 10000:
              raise serializers.ValidationError("Amount should be less than 10000")
         return data

    def validate_user(self,data):
        if not Profile.objects.filter(user=data).exists():
            raise serializers.ValidationError("User does not have a profile")



        

                                                          
                                                           
                                     
                                    
                           