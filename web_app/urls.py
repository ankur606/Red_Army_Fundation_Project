from django.urls import path
from .import views


urlpatterns = [
    
    path('', views.HomePageView.as_view(), name="homePage"),
    path('show-forms-lists', views.ShowListsFormsView.as_view(), name="showForms"),
    path('ngo-abouts-page', views.AboutsViews.as_view(), name="aboutsPagedsd"),
    
    path('education-information/forms', views.EducationInformationView.as_view(), name="educationIformation"),
    path('personal-information/forms', views.PersonalInfomationView.as_view(), name="personalIformation"),
    path('member-declaration/forms', views.MembershipDeclarationViews.as_view(), name="memberDeclaration"),
    path('special-needs-details/forms', views.SpecialNeedsDdetailsViews.as_view(), name="special_needsDetails"),
    path('membership-determination/forms', views.MembershipDeterminationViews.as_view(), name="membershipDetermination"),
    path('volunteer-information/forms', views.VolunteerInformationViews.as_view(), name="volunteerInformation"),
    path('employment-information/forms', views.EmploymentInformationViews.as_view(), name="employmentInformation"),
    path('armed-forces-service-information/forms', views.ArmedForcesServicesInformationView.as_view(), name="armedForces"),
    path('red-forces-service-information/forms', views.RedArmyServiceInformationView.as_view(), name="armyServices"),
    
    path('sspdf-commendation/forms', views.CommendationInformationView.as_view(), name="sspdfCommendation"),
    path('red-army-martyrs-record/forms', views.RedArmyMartyrsRecordView.as_view(), name="army-martyrs"),
    
    
  
  
]

  
        