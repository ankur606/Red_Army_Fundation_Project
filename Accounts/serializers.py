from dataclasses import fields
from statistics import mode
from urllib import request
from rest_framework import serializers
from setuptools import Require
from Accounts.models import *
from Admin_dasboard import *
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from Admin_dasboard.models import *
from Admin_dasboard.views import*

############  User Registration Serializer ####

class UserRegistrationSerializer(serializers.ModelSerializer):
   
    class Meta:
        
        
        model = User
        fields = ['username', 'email', 'phone_number', 'password','image']
        extra_kwargs = {
            'password':{'write_only':True,}
        }
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)     



class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
  
    class Meta:
        model = User
        fields = ['email', 'password',]


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True, required=True, style={'input_type':'password'},)
    new_password = serializers.CharField(max_length=128, write_only=True, required=True, style={'input_type':'password'},)
   

    # def validate_old_password(self, value):
    #     user = self.context.get('user')
    #     if not user.check_password(value):
    #         raise serializers.ValidationError(
    #             {"msg":'Your old password was entered incorrectly. Please enter it again.', "success":"false",},status=status.HTTP_200_OK
    #         )
    #     return value

    def validate(self, data):

        password = data.get('new_password')
        user = self.context.get('user')
        user.set_password(password)
        user.save()
        return data
class ResetUserPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20,write_only=True, required=True, style={'input_type':'number'})
    new_password = serializers.CharField(max_length=20, write_only=True, required=True, style={'input_type':'password'})
   
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')

    
    
#=========== Events show Serializers ============#
class GalleryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image']
class EventModelSerializer(serializers.ModelSerializer):
    gallery = GalleryModelSerializer(many=True)
    
    class Meta:
        model = EventsModel
        fields = ['id','image', 'headding', 'description', 'location',  'date' ,'gallery' ]
        
        

                    
#=========== Contact Inquiry Serializers ========#

class ContactInquiryModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiryModel
        fields = ['name', 'message','phone_number', 'email']
        extra_kwargs = {'name': {'required': True, 'allow_blank': False}, 'message':{'required': True, 'allow_blank': False}, 'phone_number':{'required': False, 'allow_blank': False},'email':{'required': True, 'allow_blank':True}}  


#========== Team memebers Details Serializers =======#
class TeamMembersDeatilsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutsTeamModel
        fields = ['name','designation', 'image']
        
        
class CommunityDiscussionsSerializer(serializers.ModelSerializer):
   
    likes = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    def get_likes(self,obj):
        total_like = obj.communityEvent.all().count()
        return total_like
    def get_comment(self,obj,):
        total_comment = obj.community_post.all().count()
        
        return total_comment
    def get_is_liked(self, obj):
        user = self.context.get('user')
        print(user)
  
        liked = CommunityLikeModel.objects.filter(community_id=obj, user_id = user)
        if liked:
            like = liked.last()
            return 1
        else:
            return 0
        
    class Meta:
        model = CommunityDiscussionsModel
        fields = ['id','image', 'topic_description', 'headdings',    'date', 'likes','comment', 'is_liked']
       
 
class CheckUserPhoneNumberSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True, allow_blank=True,allow_null=False)
    class Meta:
        model = User
        fields = ['phone_number']

class CommunityCommentModelSerializers(serializers.ModelSerializer):

    
    class Meta:
        model = CommunityCommentModel
        fields = ['comment', 'community_post', 'user']
        extra_kwargs = {'comment': {'required': True, 'allow_blank': False}, 'community_post': {'required': True}}  
       
class CommentUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommunityCommentModel
        fields = ['id','community_post','comment','user' ] 


#======= Event Like Serializers ====#
class EventLikeModelSerializers(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    is_liked  = serializers.SerializerMethodField()
    class Meta:
        model = CommunityLikeModel
       
        fields =['liked','user', 'community','likes', 'is_liked']
        extra_kwargs = {'liked': {'required': True}, 'community': {'required': True}, 'user': {'required': True},  } 
  
class CommunityDislikeModelSerializers(serializers.ModelSerializer):
    dislikes = serializers.SerializerMethodField()
    class Meta:
        model = CommunityLikeModel
       
        fields =['liked','user', 'community','dislikes']
        extra_kwargs = {'liked': {'required': True}, 'community': {'required': True}, 'user': {'required': True},  } 
  
class TotalCommentSerializer(serializers.ModelSerializer):
    
    username = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    
    def get_username(self,obj,):
        return obj.user.username
    
    def get_image(self,obj,):
        return obj.user.image.url
    
    class Meta:
        model = CommunityCommentModel
        fields = ['id','comment', 'community_post','user', 'username', 'image']
        extra_kwargs = {'id': {'required': True}} 

    
class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'image']      

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminSendNotifications
        fields = '__all__'        


class GetNotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminSendNotifications
        fields = ['id', 'user_receiver', 'notification_message', 'notification_headding', 'recieved_date', 'read']    
        
class UserDeleteNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminSendNotifications
        fields = ['id']        
class EditCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommunityCommentModel
        fields = ['id', 'user', 'comment']        


class DeleteCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommunityCommentModel
        fields = ['id']        
        extra_kwargs = {'id': {'required': True} } 
        