from distutils.command.upload import upload
from email import message
import uuid
from tabnanny import verbose
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from Accounts.models import*
# Create your models here.

######## Events Model #######
    

class EventsModel(models.Model):
    image = models.ImageField(null=True, blank=True, verbose_name = 'Event Image')
    headding = models.CharField(max_length=400 , null=True, blank=True , verbose_name = 'Event Headding')
    description = RichTextUploadingField( verbose_name = 'Event Description' )
    location = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'Event Location')
    date = models.DateTimeField(null=True, blank=True , auto_now_add= True)
    

    
class Gallery(models.Model):
    image = models.ImageField( null=True, blank=True , verbose_name = 'EventGallery')
    date = models.DateTimeField(null=True, blank=True , auto_now_add= True)
    event = models.ForeignKey(EventsModel, on_delete=models.CASCADE, null=True, blank=True ,related_name="gallery" )
        

#======= Contact Inquiry form ======= #

class ContactInquiryModel(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True )
    message = models.TextField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=15)
    email = models.EmailField(null=True, blank=True)
    
    
#========= About Team Model =======#

class AboutsTeamModel(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)    
    
    

class CommunityDiscussionsModel(models.Model):
    headdings = models.CharField(max_length=200 , null=True, blank=True)
    topic_description = models.TextField(blank=True, null=True)
    image = models.ImageField( upload_to="community_image",  blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    
#===== Event Comment Model =====# 
class  CommunityCommentModel(models.Model):
  
    comment = models.TextField(blank=True, null=True, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="users", blank=True, null=True)
    community_post = models.ForeignKey(CommunityDiscussionsModel,on_delete=models.CASCADE , related_name="community_post", blank=True, null=True)
  
    
#===== Event Like Models =======#

class CommunityLikeModel(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name="userLike", blank=True, null=True)
    community = models.ForeignKey(CommunityDiscussionsModel,on_delete=models.CASCADE , related_name="communityEvent", blank=True, null=True)
    liked = models.BooleanField(blank=True, null=True)
    class Meta:
      verbose_name = ('Community Like')
      verbose_name_plural = ('Community Like ')    
     
#========== Notifications Model ========#

class AdminSendNotifications(models.Model):

    user_receiver = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE,related_name='user_recive_notification')
    notification_message = models.TextField()
    notification_headding = models.CharField(max_length=250, blank=True, null=True)
    read = models.BooleanField(default=False)
    recieved_date = models.DateTimeField(auto_now_add=True)
                                                   
    def __str__(self):
        return self.notification_message


   