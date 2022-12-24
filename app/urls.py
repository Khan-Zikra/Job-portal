
from django.urls import path, include
from app.views import UserRegistrationView, UserLoginView,UserPersonalInfoView ,UserEducationView, UserExperianceView, UserSkillsView,ProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('profileview/',ProfileView.as_view(),name='profileview' ),
    path('personalinfo/',UserPersonalInfoView.as_view(), name='personalinfo'),
    path('personalinfo/<int:id>',UserPersonalInfoView.as_view(), name='personalinfo'),
    path('education/',UserEducationView.as_view(), name='education'),
    path('education/<int:id>',UserEducationView.as_view(), name='education'),
    path('experiance/',UserExperianceView.as_view(), name='experiance'),
    path('experiance/<int:id>',UserExperianceView.as_view(), name='experiance'),
    path('skills/',UserSkillsView.as_view(), name='skills'),
     path('skills/<int:id>',UserSkillsView.as_view(), name='skills'),
    


    
]
