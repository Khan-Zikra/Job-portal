from ast import Delete
from msilib.schema import ServiceInstall
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from app import serializers
from .models import Education, Experiance, User , Profile, PersonalInfo, Skills

from app.serializers import UserEducationSerializer, UserRegistrationSerializer, UserLoginSerializer, UserPersonalInfoSerializer,UserExperianceSerializer, UserSkillsSerializer,UserProfileSerializer

from django.contrib.auth import authenticate
from app.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token ,'msg':'Registration Successfull'},status= status.HTTP_201_CREATED)
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
          email = serializer.data.get('email')
          password = serializer.data.get('password')
          user = authenticate(email=email, password=password)
          if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'Login Successfull'},status= status.HTTP_200_OK)
          else:
            return Response({'errors':{'non_field_errors':['Email or Password is not valid']}},status= status.HTTP_404_NOT_FOUND)


  
class UserPersonalInfoView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserPersonalInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg' :'Information Field  Successfull'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request ,id, format=None):
        user =PersonalInfo.objects.get(user=id)
        serializer = UserPersonalInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' :'Personal information updated successfully'},status= status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id , format=None):
        user =PersonalInfo.objects.get(user=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class UserEducationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserEducationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg' :'Education Information  Field  Successfull'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request ,id, format=None):
        user =Education.objects.get(user=id)
        serializer = UserEducationSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' :'Education updated successfully'},status= status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id , format=None):
        user =Education.objects.get(user=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    

class UserExperianceView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserExperianceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg' :'Experiance  Field  Successfull'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id,format=None):
        user = Experiance.objects.get(user=id)
        serializer = UserExperianceSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg' :'Experiance updated successfully'},status= status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, id , format=None):
        user =Experiance.objects.get(user=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    



class UserSkillsView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserSkillsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg' :'Skills  Field  Successfull'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        user = Skills.objects.get(user=id)
        serializer = UserSkillsSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' :'Skills updated successfully'},status= status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, id , format=None):
        user =Skills.objects.get(user=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
  


class ProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes =[IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserRegistrationSerializer(request.user)
        data = serializer.data.get('id')
        print(data)

        profile = Profile.objects.get(user=data)
        serializer1= UserProfileSerializer(profile)
        

        personalinfo = PersonalInfo.objects.get(user=data)
        serializer2 = UserPersonalInfoSerializer(personalinfo)
        

        education = Education.objects.get(user=data)
        serializer3 = UserEducationSerializer(education)
        

        experiance = Experiance.objects.get(user=data)
        serializer4 = UserExperianceSerializer(experiance)
        

        skill = Skills.objects.get(user=data)
        serializer5 = UserSkillsSerializer(skill)
       

        return Response({"Profile":serializer1.data,
         "personalinfo":serializer2.data,
         "education":serializer3.data,
         "experiance":serializer4.data,
         "skills":serializer5.data
         })



      













    
            

            
