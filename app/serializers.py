from dataclasses import fields
from rest_framework import serializers
from app.models import Experiance, Profile, User,PersonalInfo, Education, Experiance, Skills
from taggit.serializers import (TaggitSerializer,TagListSerializerField)




class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this becoze we need confirm password field in our Regietration Request 

    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
      model = User
      fields=['id','email', 'fname', 'lname', 'gender', 'password', 'password2']
      extra_kwargs={
        'password':{'write_only':True}
      }

    # Validating Password and Confirm password While Registration
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
 
class UserPersonalInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = PersonalInfo
    # fields = ['fname', 'contact', 'DOB', 'marital_status', 'address']
    fields='__all__'

class UserEducationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Education
    fields= '__all__'

class UserExperianceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Experiance
    fields = '__all__'

class UserSkillsSerializer(TaggitSerializer,serializers.ModelSerializer):
  tags = TagListSerializerField()  # for showing in frontend we write here 
  class Meta:
    model = Skills
    fields = '__all__'






