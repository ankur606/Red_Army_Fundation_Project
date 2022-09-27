from django.urls import path
from . import views

############ 
urlpatterns = [
    
    path('changepassword', views.UserChangePasswordView.as_view(), name='changepassword'),
    path('logout', views.UserLogoutView.as_view(), name ='logout'),  
    path("user-register", views.UserRegistration.as_view(), name='register'),
    path("user-update-profile", views.UserProfileUpdateView.as_view(), name='updateProfile'),
    
    path("login", views.UserLoginView.as_view(), name='login'),
    path('event-details', views.EventsDetailsView.as_view(), name="eventDeatils"),
    path('contact-inquiry', views.ContactInquiryView.as_view(), name="contactInquiry"),
    path('company-team-members-details', views.TeamMembersDeatils.as_view(), name="teamsDetails"),
    path('community-discussions-deatils', views.CommunityDiscussionsDeatilsView.as_view(), name="teamsDetails"),
    path('add-community-comment', views.CommunityCommentView.as_view(), name="addComment"),
    path('community-like', views.EventLikeView.as_view(), name="event_liked"),
    path('verify-phone-number', views.VerifyUserPhoneNumberView.as_view(), name="verifyNumber"),
    path('rest-password', views.ResetUserPassword.as_view(), name="restPassword"),
    path('total-comments', views.CommunityListCommentView.as_view(), name="totalComment"),
    path("forms-lists", views.FormsUrlsListView.as_view(), name="forms_url"),
    path('user-get-notifications', views.UserGetNotificationView.as_view(), name="usergetnotifications"),
    path('user-delete-notifications', views.UserDeleteNotificationView.as_view(), name="userDeletenotifications"),
    path('user-clear-all-notifications', views.UserClearAllNotificationsView.as_view(), name="userDeletenotifications"),
    path('delete-comment-message', views.CommentDeleteView.as_view(), name="DeleteComment"),
    path('total-user-notifications', views.TotalNotificationView.as_view(), name="totalNotifications")
    

    
    
    
    
  
]
