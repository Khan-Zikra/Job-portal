from django.contrib import admin
from app.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app.models import Profile, PersonalInfo, Education, Experiance, Skills


class UserModelAdmin(BaseUserAdmin):
    

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.


    # How you can want to show your page when click on id
    list_display = ('id','email', 'fname', 'lname', 'gender', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('fname', 'lname', 'gender')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute.UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.


    # this is showing Add user page 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fname', 'lname', 'gender', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'id')
    ordering = ('email', 'id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(Profile)
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Experiance)
admin.site.register(Skills)

