
from asyncore import read
import json
from multiprocessing import context
from sre_constants import SUCCESS
from urllib import request
from xml.etree.ElementTree import Comment
from django.forms import EmailInput
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse 
import email
from django.core.serializers import serialize

from django.views import View
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .serializers import LogoutSerializer
from Accounts.models import *
from Admin_dasboard.models import *

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response 
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as dj_login ,logout
# Create your views here.

#Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistration(APIView):
    
    def post(self, request, format=None):
        
        user = User.objects.filter(email = request.data['email'], phone_number=request.data['phone_number'])
        if user.exists():
            return Response({'msg':' Invaild email  or Phone number already registered !','success':"false"}, status=status.HTTP_200_OK)
            
        user = User.objects.filter(email = request.data['email'])
        if user.exists():
            return Response({'msg':' Invaild email already registered !','success':"false"}, status=status.HTTP_200_OK)
            
        user1 = User.objects.filter(phone_number=request.data['phone_number'])
        if user1.exists():
            return Response({'msg':' Invaild Phone number user already registered !','success':"false"}, status=status.HTTP_200_OK)
       
        else:
            serializer = UserRegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        
        return Response({'msg':'User Registration  Successfully!','success':"true"}, status=status.HTTP_200_OK)


############## 

class UserLoginView(APIView):
    
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        users = authenticate(email=email, password=password) 
        
        
        if users is not None:
           
            
            
            token = get_tokens_for_user(users)
        
            return Response({'token':token,'msg':'User Login Succesfully','success':"true", "user_id":users.id, "username":users.username,"email":email,"phone_number":users.phone_number, "image":users.image.url }, status=status.HTTP_200_OK)
        else:
            return Response({"success":"false", "msg":"invalid email or password"}, status=status.HTTP_200_OK)
        
class UserChangePasswordView(APIView):
    
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'User Password Changed Successfully','success':"true"}, status=status.HTTP_200_OK)
        else:
            return Response({'msg':'User  Password Not Changed !','success':"false"}, status=status.HTTP_200_OK)
            
class ResetUserPassword(APIView):
   
    
    def post(self, request, format=None):
        
     
        user = User.objects.filter(phone_number=request.data['phone_number'],pk=request.user.pk).exists()
        
        if user.exists():
            user=user.first()
            data = user.set_password(request.data['new_password'])
            serializer = UserChangePasswordSerializer(data)
            
            serializer.save()
            
            return Response({'msg':'password reset successfully!' , "success":"true"}, status=status.HTTP_200_OK) 
        else: 
            return Response({'msg':' User phone number Invalid', "success":"false" }, status=status.HTTP_200_OK) 
class VerifyUserPhoneNumberView(APIView):
    def post(self, request ,format=None):
        serializer = CheckUserPhoneNumberSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data['phone']
        
        user = User.objects.filter(phone_number=phone)
        if  user.exists():
            return Response({'msg':' User Phone Verified ' , "success":"true"}, status=status.HTTP_200_OK) 
        else:
            return Response({'msg':' User Phone Number Invalid ', "success":"false" }, status=status.HTTP_200_OK) 

################# 



#=============LOGOUT=============    

class UserLogoutView(generics.GenericAPIView):
   
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'User Logout Successfully!', 'success':"true"},status=status.HTTP_200_OK)


#=============END================


class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UpdateUserProfileSerializer(instance=request.user)
        return Response({'success':'true', 'msg':'User  Profile Details', "data": serializer.data}) 
    def put(self, request, format=None):
        serializer = UpdateUserProfileSerializer(instance=request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'true', 'message':'User Profile Update Succesfully'},status=status.HTTP_200_OK)
        return Response({'success':'False', 'message':'User Profile Not Updated'}, status=status.HTTP_200_OK)



# =========== Events show Views ======#
class EventsDetailsView(APIView):
    
  
    def get(self, request, format=None):
        events_data = EventsModel.objects.all()
      
        serializer = EventModelSerializer(events_data,many=True)
        return Response({'msg':'event Details get Successfully!', 'success':"true", 'data':serializer.data,}, status=status.HTTP_200_OK)
    
#======= Contact Inquiry Views =====#
class ContactInquiryView(APIView):
    def post(self,  request, format=None):
  
        serializer = ContactInquiryModelSerializers(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
       
            return Response({'msg':'User Contact Inquiry Forms Successfully','success':"true"}, status=status.HTTP_200_OK)

        else:
            return Response({'msg':"Please Enter Valid Details", 'success':"false"}, status=status.HTTP_200_OK)


        
    
    # =========== Events show Views ======#
class TeamMembersDeatils(APIView):
    
    def get(self, request, format=None):
        team_data = AboutsTeamModel.objects.all()

        serializer = TeamMembersDeatilsSerializers(team_data,many=True)
        return Response( {"data":serializer.data, 'success':"true"} , status=status.HTTP_200_OK)
    

class CommunityDiscussionsDeatilsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        community_data = CommunityDiscussionsModel.objects.all()

        serializer = CommunityDiscussionsSerializer(community_data,many=True, context={'user':request.user.id})
       
        return Response({"data":serializer.data,'success':"true"}, status=status.HTTP_200_OK)
    


#==== Like View ======#
class EventLikeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,):
        id = request.data['community']
        liked = request.data['liked']
       
        if liked == "True":
            user_id = request.user.id
           
            created = CommunityLikeModel.objects.get_or_create(user=request.user, community_id=id, liked=liked)
        
            like_count = CommunityLikeModel.objects.filter( liked=True ).count()
            
            likes_serializer = EventLikeModelSerializers(like_count,many=True,context={"community_id":id, "user_id":request.user.id})
          
            
            return Response({'msg':"Event Like Successfully!", 'success':"true",}, status=status.HTTP_200_OK)    
        elif liked == "False":
            disliked = request.data['liked'] 
            id = request.data['community']
            data = CommunityLikeModel.objects.filter(user_id=request.user.id, community_id=id,).delete()
            
            like_count = CommunityLikeModel.objects.filter( liked=True ).count()
           
            
       
            return Response({'msg':"Event DisLiked Successfully!", 'success':"true"}, status=status.HTTP_200_OK)
            
class CommunityCommentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        comments_msg = request.data['comment']
        user_id = request.user.id
        print(user_id) 
        
        serializers = CommunityCommentModelSerializers(data=request.data)
    
        serializers.is_valid(raise_exception=True)
        serializers.save()
        
    
       
        id = request.data['community_post']
       
       
        post_list = CommunityDiscussionsModel.objects.all()
        comment_count = CommunityCommentModel.objects.filter(community_post = id ).count()
        
        post_serializer = CommunityCommentModelSerializers(post_list,many=True,context={"comment_count":comment_count})
        
        
        return Response({'msg':"Community Comment Add  Successfully!", 'success':"true"}, status=status.HTTP_200_OK)
    
    def put(self, request, format=None):
        id = request.data['id']
        user_id =request.data['user']
        comment = request.data['comment']
        community_post = request.data['community_post']
        data = CommunityCommentModel.objects.filter(id=id, user_id=user_id, community_post_id=community_post)
        
        data.update(comment=comment)
        
        return Response({'success':'true', 'message':'User Comment Message Updated Successfully!'})
 

class CommunityListCommentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        id = request.data['id']
      

        
        community_id = CommunityDiscussionsModel.objects.filter(pk=id).first()
   
        
        total_comment = CommunityCommentModel.objects.filter(community_post =id)

        
        serializer = TotalCommentSerializer(total_comment, many=True)
       
            
        return Response({"success":"true","msg":"total Comment","data":serializer.data})

class CommentDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        comment_id = request.data['id']
        community_id = request.data['community_post'] 
        data = CommunityCommentModel.objects.filter(pk=comment_id, community_post_id=community_id)
        data.delete()
        return Response({"success":"true","msg":"Comment delete successfully! " })
                                  
               

    
class FormsUrlsListView(APIView):
    def get(self, request):
        fomrs_url =[
                     {  
                    "link":"personal-information/forms",
                    "name":"Personal Information Forms"},
                    { 
                    "link":"education-information/forms",
                    "name":"Education Information Form"},
            
                    {
                    "link:":"employment-information/forms",
                    "name":"Emlpoyement Informations",
                    },
                    {
                    "link":"special-needs-details/forms",
                    "name":"Special Needs Information Forms"
                                         
                    },
                    {
                    "link":"volunteer-information/forms",
                    "name":"Volunter Information"
                     },
                    {
                    "link":"member-declaration/forms",
                    "name":"Member Declaration"
                    },
                    {
                    "link":"membership-determination/forms",
                    "name":"Membership Determination"
                    },
                    {
                    "link":"red-forces-service-information/forms",
                    "name":"Red Army Services"
                    },
                    {
                    "link":"armed-forces-service-information/forms'",
                    "name":"Armed Forces Services"
                    },
                    
                    {
                    "link":"sspdf-commendation/forms",
                    "name":"Commendation Informations"},
                    {
                    "link":"red-army-martyrs-record/forms",
                    "name":"Martyrs Recoard"
                             
                },
            
            
        ]  
     
    
        return Response({ "success":"true", "msg":"This is Alahmar forms list urls", "data":fomrs_url,}, status=status.HTTP_200_OK)
    
    
    
class UserGetNotificationView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request  ):
        id = request.user.id
        data = AdminSendNotifications.objects.filter(user_receiver=id,read=False).all()
        data.update(read=True)
        
        data = AdminSendNotifications.objects.filter(user_receiver=id,read=True).order_by('-id')
        serializer = GetNotificationSerializers(data, many=True )

        return Response({ "success":"true", "msg":" User Notifications Message ", "data":serializer.data}, status=status.HTTP_200_OK)   

class TotalNotificationView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id = request.user.id
        data = AdminSendNotifications.objects.filter(user_receiver=user_id,read=False).all()
        
        Total_notifications = AdminSendNotifications.objects.filter(user_receiver=user_id, read=False).count()
        
     
        return Response({ "success":"true", "msg":" User Total Notifications  ","total_notification":Total_notifications}, status=status.HTTP_200_OK)   

        

#========= Delete single Notifications ==========#
class UserDeleteNotificationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        id = request.data['id']
        
        id = AdminSendNotifications.objects.get(id=id)
        id.delete()
        return Response({'success':"true", 'msg':"Notifications Delete Successfully!"}, status=status.HTTP_200_OK)


class UserClearAllNotificationsView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_reciver_id = request.user.id

  
       
        notification_ids =AdminSendNotifications.objects.filter(user_receiver = user_reciver_id ).all()
        notification_ids.delete()
        return Response({'success':"true", 'msg':"User Clear All Notifications  Successfully!"}, status=status.HTTP_200_OK)
    
    
