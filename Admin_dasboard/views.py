
from ast import Return
from platform import python_branch
import re
from urllib import request
from django.forms import EmailInput
from django.http import HttpResponseRedirect,HttpResponse 
import email
from django.views import View
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from rest_framework import status   
from Accounts.models import *
from Admin_dasboard.forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as dj_login ,logout
from web_app import views
from django.core.paginator import Paginator

from web_app.models import*
# Create your views here.

class AdminDasboardView(View):
        
    def get(self, request):
        user = User.objects.all()
        super_user = User.objects.filter(is_superuser=True)
        counter=0
        superuser=0
        staff=0
        active = 0
        for i in user:
            counter+=1
            if i.is_superuser == True:
                superuser+=1

            if i.is_staff == True:
                staff+=1
        
            if i.is_active == True:
                active+=1
        d = { "user":super_user,
          "counter_user":counter,
          "superuser":superuser,
          'staff':staff,
          'user':user,
          "active":active,
         
         
        }
        if request.user.is_superuser == True:
        
            return render(request,'dasboard/index.html',d)
        else:
            return HttpResponseRedirect('/')        




#=============LOGIN=============

def login(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        passwords = request.POST.get('password')
      
        user = authenticate(request=request, email=email_id, password=passwords)
      
        if user is not None:
            if User.objects.filter(email=email_id,is_superuser=True):
                dj_login(request, user)
                return redirect('showdasboard')
            else:
                messages.error(request, 'You Are Not Admin User')    
        else:
            messages.error(request, 'Invalid Email or Password')
        

    

    return render(request,'dasboard/samples/login.html')

#=============END LOGIN==
 

#=============delete User=============
@login_required(login_url='login')
def deleteUser(request,id):
    a = User.objects.get(id=id)
    a.delete()
    messages.success(request, 'User Deleted Successfully..!!')
    return redirect('showUser')
# =========== end ==================



@login_required(login_url='login')
def adminPanel(request):

    user1 = User.objects.filter(is_superuser=True)
    user = User.objects.all()
    # ===========user counter=======

    counter=0
    superuser=0
    staff=0
    active = 0
    for i in user:
        counter+=1
        if i.is_superuser == True:
            superuser+=1

        if i.is_staff == True:
            staff+=1
        
        if i.is_active == True:
            active+=1
   
    # =========== end =======
    d = { "user":user1,
          "counter_user":counter,
          "superuser":superuser,
          'staff':staff,
          "active":active,
     
        }
    if request.user.is_superuser == True:
        return render(request,'pages/index.html',d)
    else:
        return HttpResponseRedirect('/')

def profile(request):
    if request.method == "GET" :
        ob = User.objects.get(id=request.user.id)
        if request.user.is_superuser == True:
            return render(request,'dasboard/profile.html',{"all":ob})
        else:
            return HttpResponseRedirect('/')


   

#=============FORGET PASSWORD============= 

def forgetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
    
        if User.objects.filter(email=email).exists():   
            password = request.POST.get('password')
           
            v = User.objects.get(email=email)
            v.set_password(password)
            v.save()
           
            messages.success(request, 'Password Forget Successfully..!!')
            return redirect('admim-login')
        else:
            messages.error(request, 'Invalid Email..')
    return render(request,'dasboard/samples/forget-password.html')

#=============END================

#=============LOGOUT=============    

def userlogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully..!!')
    return redirect('admim-login')

#=============END================#
#========== Add Users============#
def AddUser(request):
    if request.method == 'POST':
        image = request.FILES.get('user_image')
        username = request.POST.get('username')
        
        email = request.POST.get('email')
        phone_number = request.POST.get('username')
        
        password = request.POST.get('password')
        con_password = request.POST.get('password2')
        if password == con_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User Email  Already Exist.. ')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,phone_number=phone_number,image=image)
               
                user.save()
                messages.success(request, 'User Added Successfully..!!')
                return redirect('showUser')
            messages.error(request, 'Password Not Match ..!!')
    if request.user.is_superuser == True:
        return render(request,'dasboard/add_user.html')

    else:
        return HttpResponseRedirect('/') 

#====== Edit User Profile =========#
def  UpdateUserProfileView(request, id):
    if request.method == 'POST':
        
        image = request.FILES.get('user_image')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
         
          
        super = request.POST.get('super')
        staff = request.POST.get('staff')
        active = request.POST.get('active')
        checklist = [False,False,False]
        
        if super=='True':
            checklist[0]=True
        if staff=='True':
            checklist[1]=True
        if active=='True':
            checklist[2]=True
        
        user = User.objects.get(id=id)
        if image is not None:
            user.image = image
            user.username = username
            user.email = email
            user.phone_number = phone_number
           
            user.is_superuser=checklist[0]
            user.is_admin=checklist[1]
            user.is_active=checklist[2]
            user.save()
            messages.success(request, 'User Edit Successfully..!!') 
            return  redirect('showUser')
        
        else:
          
            user.image = image
            user.username = username
            user.email = email
            user.phone_number = phone_number
       
            user.is_superuser=checklist[0]
            user.is_admin=checklist[1]
            user.is_active=checklist[2]
            user.save()
            messages.success(request, 'User Edit Successfully..!!') 
            return  redirect('showUser')
        
                
        
        
    if request.user.is_superuser == True:      
        return render(request,'dasboard/edit_user.html',{"user":User.objects.get(id=id)})
    else:
        return HttpResponseRedirect('/')
    
  
#=========== Show User =======#
class ShowUserView(View):
    def get(self, request):
        
        user_data = User.objects.all().order_by("-id") 
        user_total = User.objects.all().count()
        paginator = Paginator(user_data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)

        return render(request, 'dasboard/show_user_details.html',{'page_obj':page_object, 'user_total':user_total})

#============ Events View ============#

class EventsView(View):
    
    def get(self, request):
        event_forms = EventsForm()
        return render(request, 'dasboard/events.html')
    
    def post(self,request):
        event_model = EventsModel()
     
           
        image = request.FILES['event_image']  
        headding = request.POST.get('headding')
        description = request.POST.get('description')
        location = request.POST.get('location')
        
        event_model.image = image
        event_model.headding = headding
        event_model.description = description
        event_model.location = location
        event_model.save()
        return redirect('eventList')


#=========== End Event View ============#

#=========== Event List View ==========#

class EventListView(View):
    def get(self, request):
        event_list_data = EventsModel.objects.all().order_by("-id") 
        paginator = Paginator(event_list_data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request , 'dasboard/event-list.html',{'page_obj':page_object})        
        



class EventDeleteView(View):
  
    def get(self, request,id):
    
     
        a = EventsModel.objects.get(id=id)
        
      
        a.delete()
        messages.success(request, 'Event Deleted Successfully..!!')
        return redirect('eventList')
    
class CommunityDeleteView(View):
  
    def get(self, request,id):
    
     
        a = CommunityDiscussionsModel.objects.get(id=id)
        
      
        a.delete()
        messages.success(request, 'Community Deleted Successfully..!!')
        return redirect('communityDiscussionsDetails')
    
      
    
    

class EventEditView(View):
  
    def get(self, request,id):
      
     
        id = EventsModel.objects.filter(id=id).all().order_by("-id") 
        

        
        return render(request, 'dasboard/edit-event.html',{'data':id}) 
    def post(self, request, id):
        image = request.FILES.get('event_image')
        event_data = EventsModel.objects.filter(pk=id).all()
       
        headding = request.POST.get('headding')
        description = request.POST.get('description')
        location = request.POST.get('location')
        if image is not None:
            EventsModel(pk=id,image=image,headding=headding,description=description, location=location).save()
            messages.success(request, 'edit Successfully..!!')
            return redirect('eventList')
        else:
            for i in event_data:
           
                EventsModel(pk=id, image=i.image,  headding=headding,description=description, location=location).save()
        
            
            
            messages.success(request, 'edit Successfully..!!')
            return redirect('eventList')

  
class CommunityEditView(View):
  
    def get(self, request,id):
       
     
        data = CommunityDiscussionsModel.objects.filter(id=id).all().order_by("-id") 
    
        return render(request, 'dasboard/edit_community.html',{'data':data}) 
    def post(self, request, id):
        community_data = CommunityDiscussionsModel.objects.filter(pk=id).all()
        image = request.FILES.get('community_image')  
        headings = request.POST.get('community_headings')
        description = request.POST.get('description')
        if image is not None:
            
            CommunityDiscussionsModel(id=id,image=image, headdings=headings, topic_description=description).save()
            messages.success(request, 'Community edit Successfully..!!')
            return redirect('communityDiscussionsDetails')
        else:
            for img in community_data:
                CommunityDiscussionsModel(id=id,image=img.image, headdings=headings, topic_description=description).save()
            messages.success(request, 'Community edit Successfully..!!')
            return redirect('communityDiscussionsDetails')           
             
#=========== Add Event Gallery Images ===========#

class EventGalleryView(View):
    def get(self, request):
        event_id = EventsModel.objects.all().order_by("-id") 
        return render(request, 'dasboard/gallery/add_gallery_image.html',{'event_id':event_id}) 
        
    def post(self, request):
        data = Gallery()  
      
        event_id = request.POST.get('event_id')

       
        event_image = request.FILES['event_image']
       
        
        id = EventsModel.objects.filter(id=event_id).first()
       
        Gallery.objects.create( event =id, image=event_image)
      
        return redirect('showGallery')
            
    
    
    
        
#=========== Show Event Gallery Images ===========#

class ShowEventGalleryView(View):
    def get(self, request):
        data = Gallery.objects.all().order_by("-id") 
        paginator = Paginator(data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/gallery/event_gallery.html', {'page_obj':page_object}) 
            


#====== show Contact Inquiry details View ======#

class ShowContactInquiryDetailsView(View):
    def get(self, request):
        data = ContactInquiryModel.objects.all().order_by("-id") 
        paginator = Paginator(data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/show_company_contact.html', {'page_obj':page_object}) 
        
        
        
        
#====== Admin delete Contact Inquiry user  details View ======# 

class UserContactInquiryDetailsDelete(View):
      def get(self, request,id):
        
     
        id = ContactInquiryModel.objects.get(id=id)
        id.delete()
        messages.success(request, 'User contact inquiry Details  Deleted Successfully..!!')
        return redirect('showContactDetails')
    
    
#=========== Company About Team Members ======#

class AboutsTeamMemers(View):
    def get(self, request):
        return render(request , 'dasboard/add_team_members.html')
    def post(self, request):
        team_data = AboutsTeamModel()
        name = request.POST.get('name')
        desgination = request.POST.get('designation')    
        image = request.FILES['members_image']
        
        team_data.name = name
        team_data.designation = desgination
        team_data.image = image
        team_data.save()
        
        return redirect('teamMembersdeatils') 

class TeamMemersDetailsView(View):
    def get(self, request):
        team_data = AboutsTeamModel.objects.all().order_by("-id") 
        paginator = Paginator(team_data, per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/team_members_list.html', {'page_obj':page_object})    
    
 
#======= Team Memers Delete View ======#
class TeamMembersDeleteView(View):
    def get(self, request, id):
        id = AboutsTeamModel.objects.get(id=id)
        id.delete()
        messages.success(request, 'Team Members Deleted Successfully..!!')
        return redirect('teamMembersdeatils')
        
        
    
    
#====== Update Team Members Recoards =========#

class UpdateTeamMemersRecaord(View):
    def post(self, request,id):
        team_data = AboutsTeamModel.objects.filter(pk=id)
      
        name = request.POST.get('name')
        desgination = request.POST.get('designation')    
        image = request.FILES.get('members_image')
       
        team_data.name = name
        team_data.designation = desgination
        team_data.image = image
        
        team_data.save()
        
        return redirect('teamMembersdeatils')    
    
    

class CommunityDiscussionsView(View):
    def get(self, request):
        return render(request , 'dasboard/add_new_Community.html')
    
    def post(self, request):
        community_data = CommunityDiscussionsModel()
        
        community_image = request.FILES['community_image']
        heading = request.POST.get('heading')
     
        description = request.POST.get('description')    
        
        community_data.image = community_image
        community_data.topic_description = description
        community_data.headdings = heading
        community_data.save()
        
        
        return redirect('communityDiscussionsDetails')     
    
    

class CommunityDiscussionsDetailsView(View):
    def get(self, request):
        community_data = CommunityDiscussionsModel.objects.all().order_by("-id") 
        paginator = Paginator(community_data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/show_list_Community_details.html', {'page_obj':page_object})    
    

    
    
#===== Event Image Delete View =======#

class EventImageDelete(View):
    def get(self, request ,id):
        id = Gallery.objects.get(id=id)
        id.delete()
        messages.success(request, 'Event Image Delete Successfully..!!')
        return redirect('showGallery')
        
        
        
        


#==== Home Page Content ======#

class HomePageContentView(View):
    def get(self, request):
        return render(request, 'dasboard/web_templates/add_home_page_content.html')        
    
    def post(self, request):
        data = HomePageContents()
        
        images = request.FILES.get('apna_image')
        
        headding = request.POST.get('headding')
        descriptions = request.POST.get('description')     
        contents = request.POST.get('content')

        data.image = images
        data.headdings = headding
        data.description = descriptions
        data.content = contents 
        data.save()
     
        return redirect('showcontent')
    
    
class HomePageContentDetailsView(View):
    def get(self, request):
        data = HomePageContents.objects.all().order_by("-id") 
        paginator = Paginator(data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/web_templates/home_page_content_details.html',{'page_obj':page_object})        

   
class EditHomePageContentView(View):
    def get(self, request,id):
        data = HomePageContents.objects.filter(pk=id).all()
    
        return render(request, 'dasboard/edit_home_page_content.html',{'home_page_data':data})        
    permission_classes = [IsAuthenticated]
    def post(self, request,id):
        data = HomePageContents.objects.filter(pk=id).all()
        
        image = request.FILES.get('image')
        headding = request.POST.get('headding')
        descriptions = request.POST.get('description')     
        contents = request.POST.get('content')
        if image is not None:
            HomePageContents(id=id,image=image, description = descriptions, headdings=headding, content = contents  ).save()
            messages.success(request, 'Home Page edit Successfully..!!')
            return redirect('showcontent')
        else:
            for img in data:
                
                HomePageContents(id=id,image=img.image, description = descriptions, headdings=headding, content = contents  ).save()
            messages.success(request, 'Home Page edit Successfully..!!')
            return redirect('showcontent')
            
class HomePageContentDelete(View):
    def get(self, request ,id):
        id = HomePageContents.objects.get(id=id)
        id.delete()
        messages.success(request, 'Home Page Content Delete Successfully..!!')
        return redirect('showcontent')
                   
 
class CommunityLikedDetailsView(View):
    def get(self, request):
        data = CommunityLikeModel.objects.all().order_by("-id") 
        paginator = Paginator(data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/community_liked_details.html',{'page_obj':page_object})    
    
class LikedDeleteView(View):    
    def get(self, request, id):
        data = CommunityLikeModel.objects.filter(id=id)
        data.delete()
        return redirect('liked')
            
class CommunityCommentDetailsView(View):
    def get(self, request):
        data = CommunityCommentModel.objects.all().order_by("-id") 
        paginator = Paginator(data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/community_comments_details.html',{'page_obj':page_object})        

class CommentdDeleteView(View):    
    def get(self, request, id):
        data = CommunityCommentModel.objects.filter(id=id)
        data.delete()
        return redirect('commentDetails')
class AddNotificationView(View):
    def get(self, request):
        user =  User.objects.all()
     
       
        return render(request, 'dasboard/add_notifications.html', {'user':user})
    
    def post(self, request,):
        user_receiver = request.POST['user_id']
        if user_receiver =="":
            
            notification_message = request.POST['notification_message']
            notification_headding = request.POST['notification_headding']
            # superusers = User.objects.filter(is_superuser=True)
            # for id in superusers:
            #     return  id.id
        
            for user in User.objects.all():
          
                
                all_user = AdminSendNotifications(
                    notification_message = notification_message,
                    notification_headding  =notification_headding, 
                    user_receiver = user
                   )
                all_user.save()
                
        else:
            user_receiver = request.POST['user_id']
            notification_message = request.POST['notification_message']
            notification_headding = request.POST['notification_headding']
          
            users = User.objects.get(id=user_receiver)
         
            instance = AdminSendNotifications(notification_message=notification_message, notification_headding=notification_headding, user_receiver=users )
            instance.save()
        return redirect('showNotification')


class NotificationDelete(View):
    def get(self, request, id):
        id = AdminSendNotifications.objects.get(id=id)
        id.delete()
        messages.success(request, ' Delete User Notifications Successfully..!!')
        return redirect('showNotification')         




class ShowNotification(View):
    def get(self, request):
        s = AdminSendNotifications()
        data = AdminSendNotifications.objects.all().order_by("-id")      
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/show_notification.html', {'page_obj':page_object})



class AddAboutsPageContentView(View):
    

    def get(self, request):
        return render(request, 'dasboard/about_us_add.html')

    def post(self, request):
        about = AboutModel()
        image = request.FILES['image'] 
        headings  = request.POST.get('headings')
        description = request.POST.get('description')
       
        AboutModel.objects.create(headding=headings, description=description , image = image)
      
      
        return redirect('showAboutsPAge')
class EditAboutsPageContentView(View):
    

    def get(self, request,id):
        data = AboutModel.objects.filter(pk=id)
        return render(request,'dasboard/edit-abouts-page.html',   {"data":data})
    
    def post(self, request,id):
        data = AboutModel.objects.filter(pk=id)
        image = request.FILES.get('image')
        headings  = request.POST.get('headings')
        print(headings)
        description = request.POST.get('description')
        if image is not None:
            AboutModel(id=id, image=image, headding=headings, description=description ).save()
            messages.success(request, ' Abouts Page Content Edit Successfully..!!')
            
            return redirect('showAboutsPAge') 
        else:
            for img in data:
                AboutModel(id=id, image=img.image, headding=headings, description=description ).save()
            messages.success(request, ' Abouts Page Content Edit Successfully..!!')
            
            return redirect('showAboutsPAge') 
      
       
    
class DeteteAboutsPageContent(View):
    def get(self, request, id):
        data = AboutModel.objects.get(id=id)
        data.delete()
        messages.success(request, ' Abouts Page Content Delete Successfully..!!')
        
        return redirect('showAboutsPAge')   
class OtherAboutsPageContentView(View):
    

    def get(self, request):
        return render(request, 'dasboard/abouts_other_content_add.html')

    def post(self, request):
        about = OtherAboutsPageData()
        
        headings  = request.POST.get('headings')
     
        description = request.POST.get('description')
      
        OtherAboutsPageData.objects.create(headdings=headings, description=description )
       
        
      
        return redirect('showOtherAboutsPAge')
class ShowAboutsPageContentView(View):
    def get(self, request):
        data = AboutModel.objects.all().order_by("-id") 
        paginator = Paginator(data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/show-abouts-page.html',{"page_obj":page_object})
class ShowOtherAboutsPageContentView(View):
    def get(self, request):
        data = OtherAboutsPageData.objects.all().order_by("-id") 
        paginator = Paginator(data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)
        return render(request, 'dasboard/show_other_abouts_page_data.html',{"page_obj":page_object})    
    
class EmploymentInformationFormsDetailsView(View):
    def get(self, request):
        data = Employment_information.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/employe-informations-forms-list.html',{"page_obj":page_object}) 
    
    
class EmploymentInformationDetailsView(View):
    def get(self, request, id):
        data = Employment_information.objects.filter(id=id)
        return render(request, 'dasboard/employee-forms-recoard-details.html',{"data":data}) 
        

class EmploymentInformationDeleteRecoardView(View):
    def get(self, request, id):
        data = Employment_information.objects.filter(id=id)
        data.delete()
        messages.success(request, ' Employee Informations Forms Delete Successfully..!!')
        
        return redirect('employeeInformations') 
        
  
class PersonalInformationsSubmitListView(View):
    def get(self, request):
        data = PersonalInformation.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/personal-informations-submit-recoard-lists.html', {'page_obj':page_object})
    
    
    
class PeronalInformationsFormsDeleteView(View):
    def get(self, request, id):
        data = PersonalInformation.objects.get(pk=id)
        data.delete()
        messages.success(request, 'User Personal Information Recoard Delete Successfully..!!')
        return redirect('personalFormsSubmits')
        

class PeronalInformationsFormsMoreDetailsView(View):
    def get(self, request, id):
        data = PersonalInformation.objects.filter(pk=id)
     
        
        return render(request, 'dasboard/personal-informations-recoard-details.html', {'data':data})
        
class EducationInformationsSubmitFormsListView(View):
    def get(self, request):
        data = EducationInformation.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/education-submit-recoard-lists.html', {'page_obj':page_object})
    
class EducationsInformationsFormsMoreDetailsView(View):
    def get(self, request, id):
        data = EducationInformation.objects.filter(pk=id)
     
        
        return render(request, 'dasboard/educations-forms-recoard-details.html', {'data':data})
           
class EducationsInformationsFormsDeleteView(View):
    def get(self, request, id):
        data = EducationInformation.objects.filter(pk=id)
     
        data.delete()
        messages.success(request, ' Educations Informations Forms Delete Successfully..!!')
        
        return redirect('educationsFormsSubmits')
           
             
class VolunteerInformationsSubmitFormsListView(View):
    def get(self, request):
        data = Volunteer_informations.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/volunteer-informations-forms-lists.html', {'page_obj':page_object})
              

class VolunteerInformationDetailsView(View):
    def get(self, request, id):
        data = Volunteer_informations.objects.filter(pk=id)
     
        
        return render(request, 'dasboard/volunteer-details.html', {'data':data})


class VolunteerInformationDeleteView(View):
    def get(self, request, id):
        data = Volunteer_informations.objects.filter(pk=id)
     
        data.delete()
        return redirect('VolunteerInformationsSubmits')
 
 
class SpecialneedsFormsListsView(View):
    def get(self, request):
        data = Specialneedsdetails.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/special-needs-forms-lists.html', {'page_obj':page_object})
                      
                       

class SpecialneedsDetailsView(View):
    def get(self, request, id):
        data = Specialneedsdetails.objects.filter(id=id)
        return render(request, 'dasboard/specail-needs-details.html', {'data':data})
                      

class SpecialneedsDeleteView(View):
    def get(self, request, id):
        data = Specialneedsdetails.objects.filter(id=id)
        data.delete()
        messages.success(request, ' Specail Needs Informations Forms Delete Successfully..!!')
        
        return redirect('specailNeedsForms')
              

class MemberDeclarationsFormsListView(View):
    def get(self, request):
        data = MemberDeclaration.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/member-declaration-forms-lists.html', {'page_obj':page_object})


class MemberDeclarationsDetails(View):
    def get(self, request, id):
        data = MemberDeclaration.objects.filter(id=id)
        return render(request, 'dasboard/member-declarations-recoard-details.html', {'data':data})


class MemberDeclarationsDeleteview(View):
    def get(self, request, id):
        data = MemberDeclaration.objects.filter(id=id)
        data.delete()
        return redirect('membersFormslist')

class RedArmyInformationsFormsListView(View):
    def get(self, request):
        data = RedArmyServicesInformations.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/red-army-services-froms-lists.html', {'page_obj':page_object})


class RedArmyInformationsDetailsView(View):
    def get(self, request, id):
        data = RedArmyServicesInformations.objects.filter(id=id)
        return render(request, 'dasboard/red-army-informations-forms-details.html', {'data':data})

class RedArmyInformationsDeleteView(View):
    def get(self, request, id):
        data = RedArmyServicesInformations.objects.filter(id=id)
        data.delete()
        
        return redirect('redArmyFormsList')

class ArmedforcesInformationsFormsListView(View):
    def get(self, request):
        data = ArmedForcesServiceInformations.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/armed-forces-forms-lists.html', {'page_obj':page_object})

class ArmedforcesInformationsDeleteView(View):
    def get(self, request, id):
        data = ArmedForcesServiceInformations.objects.filter(id=id)
        data.delete()
        
        return redirect('armedFormslist')
   

class ArmedforcesInformationsDetailsView(View):
    def get(self, request, id):
        data = ArmedForcesServiceInformations.objects.filter(id=id)
        return render(request, 'dasboard/armed-forces-details-page.html', {'data':data})
    




class MembershipDeterminationsListView(View):
    def get(self, request):
        data = MembershipDeterminationsModel.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/member-determinations-forms-lists.html', {'page_obj':page_object})

class MembershipDeterminationsDeleteView(View):
    def get(self, request, id):
        data = MembershipDeterminationsModel.objects.filter(id=id)
        data.delete()
        
        return redirect('memberDeterminationslist')
   

class MembershipDeterminationsDetailsiew(View):
    def get(self, request, id):
        data = MembershipDeterminationsModel.objects.filter(id=id)
        return render(request, 'dasboard/determinations-forms-details.html', {'data':data})
    

class CommerdationInformationFormsListView(View):
    def get(self, request):
        data = CommerdationInformationForms.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/commendations-request-forms-lists-page.html', {'page_obj':page_object})

class CommerdationInformationFormsDetailsView(View):
    def get(self, request, id):
        data = CommerdationInformationForms.objects.filter(id=id)
        return render(request, 'dasboard/commendations-forms-details-page.html', {'data':data})
    

class CommerdationInformationFormsDeleteView(View):
    def get(self, request, id):
        data = CommerdationInformationForms.objects.filter(id=id)
        data.delete()
        return redirect('ssdpfFormslist')

class RedArmyMartyrsRecordFormsListView(View):
    def get(self, request):
        data = MartyrsInformationModel.objects.all().order_by("-id") 
        paginator = Paginator(data, per_page=10) 
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request, 'dasboard/martyrs-informations-forms-list.html', {'page_obj':page_object})


class RedArmyMartyrsRecordFormsdetailsView(View):
    def get(self, request, id):
        data = MartyrsInformationModel.objects.filter(id=id)
        return render(request, 'dasboard/martyrs-informations-forms-details.html', {'data':data})


class RedArmyMartyrsRecordFormsDeleteView(View):
    def get(self, request, id):
        data = MartyrsInformationModel.objects.filter(id=id)
        data.delete()
        return redirect('martyrsFormsListsdetails')

    
    

    
# class UserReviewView(View):    
# class UserReviewView(View):
#     def get(self, request):
#         return render(request, 'dasboard/add_user_review.html')     
#     def post(self, request):
#         review_data = UserReviewModel()
#         name = request.POST['name']
#         review_description = request.POST['review_description']  
#         review_data.name = name
#         review_data.review_description  = review_description
#         review_data.save()
#         return redirect('reviewDetails') 


# class ReviewDetailsView(View):
#     def get(self, request):
#         data = UserReviewModel.objects.all()
#         return render(request, 'dasboard/user_review_details.html')            
class Comment(View):
    pass