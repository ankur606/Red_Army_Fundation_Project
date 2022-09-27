from django.urls import path
from django.views import View
from . import views


urlpatterns = [
    path('admin-login/',views.login,name='admim-login'), 
    path('user-logout/', views.userlogout, name ='logouts'),
    path("admin-dashboard/",views.AdminDasboardView.as_view() , name='showdasboard' ),
        path('admin-dashboard/delete-user/<int:id>', views.deleteUser, name="deleteUser" ),
        path('admin-add-user', views.AddUser, name="addUser" ),
        path('admin-profile-user', views.profile, name="profileUser" ),

        
        path('update-user-profile/<int:id>', views.UpdateUserProfileView, name="editUser"),
        
        path('user-details/',views.ShowUserView.as_view(), name="showUser"),
    path("forget-password/",views.forgetPassword, name='forgetpassword'),
    path('events/',views.EventsView.as_view(), name="event"),
    path('event-list/',views.EventListView.as_view(), name="eventList"),
    path('event-delete/<int:id>', views.EventDeleteView.as_view(), name="eventDelete"),
    path('event-edit/<int:id>/', views.EventEditView.as_view(), name="eventEdit"),
    path('community-edit/<int:id>/', views.CommunityEditView.as_view(), name="communityEdit"),
    
    path('add-event-gellary-image/', views.EventGalleryView.as_view(), name="gallery"),
    path('show-event-gallery/', views.ShowEventGalleryView.as_view(), name="showGallery"),
    path('user-contact-details/', views.ShowContactInquiryDetailsView.as_view(), name="showContactDetails"),
    path('user-contact-details-delete/<int:id>', views.UserContactInquiryDetailsDelete.as_view(), name="deleteContact"),
    path('company-team-members/', views.AboutsTeamMemers.as_view(), name="teamMembers"),
    path('company-team-members-details/', views.TeamMemersDetailsView.as_view(), name="teamMembersdeatils"),
    path('team-memebers-delete/<int:id>', views.TeamMembersDeleteView.as_view(), name="teamMembersDelete"),
    path('edit-team-members-recaords/<int:id>', views.UpdateTeamMemersRecaord.as_view(), name="updateTeamRecaord"),
    path('community-discussions/', views.CommunityDiscussionsView.as_view(), name="communityDiscussions"),
    path('community-discussions-details', views.CommunityDiscussionsDetailsView.as_view(), name="communityDiscussionsDetails"),
    path('event-image-delete/<int:id>', views.EventImageDelete.as_view(), name="eventImageDelete"),
    path('add-home-content', views.HomePageContentView.as_view(), name="homePageContent"),
    path('home-page-edit/<int:id>/', views.EditHomePageContentView.as_view(), name="homeEdit"),
    path('send-notification', views.AddNotificationView.as_view(), name="sendNotifications"),
    path('content-details', views.HomePageContentDetailsView.as_view(), name="showcontent"),
    path('home-page-content-delete/<int:id>', views.HomePageContentDelete.as_view(), name="deletecontent"),
    path('community-liked-details', views.CommunityLikedDetailsView.as_view(), name="liked"),
    path('community-liked-delete/<int:id>', views.LikedDeleteView.as_view(), name="likedDelete"),
    
    path('community-comment-details', views.CommunityCommentDetailsView.as_view(), name="commentDetails"),
    path('community-comment-delete/<int:id>', views.CommentdDeleteView.as_view(), name="commentDelete"),
    
    path('notification-details', views.ShowNotification.as_view(), name="showNotification"), 
    path('community-delete/<int:id>', views.CommunityDeleteView.as_view(), name="communityDelete"),
    path('notification-delete/<int:id>', views.NotificationDelete.as_view(), name="notificationDelete"),
    path('ngo-abouts-add-content', views.AddAboutsPageContentView.as_view(), name="aboutsPage"),
    path('show-abouts-content', views.ShowAboutsPageContentView.as_view(), name="showAboutsPAge"),
    path('add-abouts-other-content', views.OtherAboutsPageContentView.as_view(), name="showotherAboutsData"),
    path('show-abouts-content-other', views.ShowOtherAboutsPageContentView.as_view(), name="showOtherAboutsPAge"),
    path('edit-abouts-contents/<int:id>', views.EditAboutsPageContentView.as_view(), name="editAboutsPage"),
    path('delete-abouts-contents/<int:id>', views.DeteteAboutsPageContent.as_view(), name="deleteAboutsPage"),
    path('employee-informations-forms-submit-list', views.EmploymentInformationFormsDetailsView.as_view(), name="employeeInformations"),
    path('personal-informations-Recoard-details-lists', views.PersonalInformationsSubmitListView.as_view(), name="personalFormsSubmits"),
    path('user-personal-information-forms-recoard-delete/<int:id>', views.PeronalInformationsFormsDeleteView.as_view(), name="deletePersonal"),
    path('user-personal-information-forms-more-details/<int:id>', views.PeronalInformationsFormsMoreDetailsView.as_view(), name="personal_Information_details"),
    path('educations-informations-recoard-details-lists', views.EducationInformationsSubmitFormsListView.as_view(), name="educationsFormsSubmits"),
    path('educations-information-forms-more-details/<int:id>', views.EducationsInformationsFormsMoreDetailsView.as_view(), name="educationsInformation_details"),
    path('volunteer-informations-details-lists', views.VolunteerInformationsSubmitFormsListView.as_view(), name="VolunteerInformationsSubmits"),
    path('volunteer-informations-recoard-details-lists/<int:id>', views.VolunteerInformationDetailsView.as_view(), name="VolunteerInformationDetails"),
    path('employee-informations-details/<int:id>', views.EmploymentInformationDetailsView.as_view(), name="emp_Details"),
    path('employee-informations-delete/<int:id>', views.EmploymentInformationDeleteRecoardView.as_view(), name="empDelete"),
    path('educations-informations-forms-delete/<int:id>', views.EducationsInformationsFormsDeleteView.as_view(), name="educationsDelete"),
    path('special-informations-forms-details-lists', views.SpecialneedsFormsListsView.as_view(), name="specailNeedsForms"),
    path('special-informations-forms-details/<int:id>', views.SpecialneedsDetailsView.as_view(), name="specailneedsDetailsForms"),
    path('special-informations-forms-delete/<int:id>', views.SpecialneedsDeleteView.as_view(), name="sndDelete"),
    path('volunteer-informations-recoard-delete/<int:id>', views.VolunteerInformationDeleteView.as_view(), name="volunteerDelete"),
    path('members-declarations-forms-details-lists', views.MemberDeclarationsFormsListView.as_view(), name="membersFormslist"),
    path('members-declarations-forms-details/<int:id>', views.MemberDeclarationsDetails.as_view(), name="membersformsDetails"),
    path('members-declarations-forms-delete/<int:id>', views.MemberDeclarationsDeleteview.as_view(), name="membersFormsdelete"),
    
    path('red-army-informations-forms-lists', views.RedArmyInformationsFormsListView.as_view(), name="redArmyFormsList"),
    path('red-army-informations-forms-details/<int:id>', views.RedArmyInformationsDetailsView.as_view(), name="redArmyDetailsForms"),
    path('red-army-informations-forms-delete/<int:id>', views.RedArmyInformationsDeleteView.as_view(), name="redArmyDelete"),
    path('armed-forces-forms-details-lists', views.ArmedforcesInformationsFormsListView.as_view(), name="armedFormslist"),
    path('armed-forces-forms-delete/<int:id>', views.ArmedforcesInformationsDeleteView.as_view(), name="armedDelete"),
    path('armed-forces-forms-details/<int:id>', views.ArmedforcesInformationsDetailsView.as_view(), name="armedDetails"),
     
    path('member-determinations-forms-details-lists', views.MembershipDeterminationsListView.as_view(), name="memberDeterminationslist"),
    path('membership-forms-delete/<int:id>', views.MembershipDeterminationsDeleteView.as_view(), name="memberDeterminationsDelete"),
    path('membership-determinations-forms-details/<int:id>', views.MembershipDeterminationsDetailsiew.as_view(), name="memberDeterminationsdetails"),
    path('ssdpf-commendations-forms-lists', views.CommerdationInformationFormsListView.as_view(), name="ssdpfFormslist"),
    path('ssdpf-commendations-forms-delete/<int:id>', views.CommerdationInformationFormsDeleteView.as_view(), name="ssdpfFormsdelete"),
    
    path('ssdpf-commendations-forms-details/<int:id>', views.CommerdationInformationFormsDetailsView.as_view(), name="sspdfDetails"),
    path('red-army-martyrs-forms-lists', views.RedArmyMartyrsRecordFormsListView.as_view(), name="martyrsFormsListsdetails"),
    path('red-army-martyrs-forms-details/<int:id>', views.RedArmyMartyrsRecordFormsdetailsView.as_view(), name="martyrsformsdetails"),
    path('red-army-martyrs-forms-delete/<int:id>', views.RedArmyMartyrsRecordFormsDeleteView.as_view(), name="martyrsFormsdelete"),
    
    
    
    
    
    
    
    
    
    
    
    
    
    # path('add-user-review', views.UserReviewView.as_view(), name="userReview"),
    # path('user-review-details', views.ReviewDetailsView.as_view(), 'reviewDetails')
    
    

    
]
