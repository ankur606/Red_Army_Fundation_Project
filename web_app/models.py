
from contextlib import nullcontext
from pyexpat import model
from random import choices

from django.db import models
from django.views import View
from multiselectfield import MultiSelectField
from django.forms import CharField, MultipleChoiceField, model_to_dict, modelform_factory

from Accounts.models import User

# Create your models here.
class AboutModel(models.Model):
    headding = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
 
    
    

class HomePageContents(models.Model):
    image = models.ImageField(null=True, blank=True)
    headdings = models.TextField(max_length=100, null=True, blank=True)
    description = models.TextField( verbose_name = 'Description',null=True, blank=True )
    content = models.TextField( verbose_name = 'Content', null=True, blank=True )

class OtherAboutsPageData(models.Model):
    headdings = models.TextField(max_length=100, null=True, blank=True)
    description = models.TextField( verbose_name = 'Description',null=True, blank=True )
class UserReviewModel(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)    
    review_description = models.TextField(null=True, blank=True)
 


class MemberDeclaration(models.Model):
 
   declaration = models.TextField( null=True, blank=True)
   full_name = models.CharField(max_length=40, null=True, blank=True)
   date = models.DateField(null=True, blank=True)

   location = models.CharField(max_length=500, null=True, blank=True)
    
         

#==== Education Primary Information Model =======#

class EducationInformation(models.Model):

    
    primary_school_name = models.CharField(max_length=300, blank=True, null=True)  
    primary_country_study_name = models.CharField(max_length=300,  null=True, blank=True) 
    primary_year_of_commencement = models.CharField(max_length=300,  null=True, blank=True) 
    primary_year_of_completion  = models.CharField(max_length=300,  null=True, blank=True)
    primary_certification_attained = models.CharField(max_length=300, null=True, blank=True) 
   
    secondary_name_of_school = models.CharField(max_length=300, blank=True, null=True)  
    secondary_country_of_study = models.CharField(max_length=300, null=True, blank=True) 
    secondary_year_of_commencement = models.CharField(max_length=300,null=True, blank=True) 
    secondary_year_of_completion  = models.CharField(max_length=300,   null=True, blank=True)
    secondary_certification_attained = models.CharField(max_length=300, null=True, blank=True)   
    
    diploma_name_of_school = models.CharField(max_length=300,  blank=True, null=True)  
    diploma_country_of_study = models.CharField(max_length=300,  null=True, blank=True) 
    diploma_year_of_commencement = models.CharField(max_length=300, null=True, blank=True) 
    diploma_year_of_completion  = models.CharField(max_length=300,    null=True, blank=True)
    diploma_certification_attained = models.CharField(max_length=300, null=True, blank=True)        
    
    associate_name_of_school = models.CharField(max_length=300, blank=True, null=True)  
    associate_country_of_study = models.CharField(max_length=300, null=True, blank=True) 
    associate_year_of_commencement = models.CharField(max_length=300,  null=True, blank=True) 
    associate_year_of_completion  = models.CharField(max_length=300, null=True, blank=True)
    associate_certification_attained = models.CharField(max_length=300, null=True, blank=True)        
        
    bachelor_name_of_school = models.CharField(max_length=300, blank=True, null=True)  
    bachelor_country_of_study = models.CharField(max_length=300, null=True, blank=True) 
    bachelor_year_of_commencement = models.CharField(max_length=300, null=True, blank=True) 
    bachelor_year_of_completion  = models.CharField(max_length=300,  null=True, blank=True)
    bachelor_certification_attained = models.CharField(max_length=300, null=True, blank=True)        
           
    master_name_of_school = models.CharField(max_length=300, blank=True, null=True)  
    master_country_of_study = models.CharField(max_length=300,  null=True, blank=True) 
    master_year_of_commencement = models.CharField(max_length=300, null=True, blank=True) 
    master_year_of_completion  = models.CharField(max_length=300, null=True, blank=True)
    master_certification_attained = models.CharField(max_length=300, null=True, blank=True)        
           
    philosohy_name_of_school = models.CharField(max_length=300, blank=True, null=True)  
    philosohy_country_of_study = models.CharField(max_length=300, null=True, blank=True) 
    philosohy_year_of_commencement = models.CharField(max_length=300,  null=True, blank=True) 
    philosohy_year_of_completion  = models.CharField(max_length=300,null=True, blank=True)
    philosohy_certification_attained = models.CharField(max_length=300, null=True, blank=True)    
  
    describe_your_thaughts = models.CharField(max_length=300, blank=True, null=True)  
    describe_special_skills = models.CharField(max_length=300, blank=True, null=True)   

    describe_specialization_indetail = models.CharField(max_length=300, blank=True, null=True)  
    describe_professional_certificates = models.CharField(max_length=300, blank=True, null=True)  
                          
                          
class PersonalInformation(models.Model):
 
    image = models.FileField(null=True, blank=True)
    registration_number = models.CharField(max_length=50, null=True, blank=True)
    confirmation_code = models.CharField(max_length=50, null=True, blank=True)
    full_name = models.CharField(max_length=30, null=True, blank=True)
    alias_or_nicknames = models.CharField(max_length=30, null=True, blank=True)
    relationship = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(null=True, blank=True, max_length=100)
    identification_number = models.CharField(max_length=40,  null=True, blank=True)
    
    type_of_identification = models.CharField(max_length=500, null=True, blank=True)
    issuing_country = models.CharField(max_length=50, null=True, blank=True)
    
    nationality_at_birth = models.CharField(max_length=50,   null=True, blank=True)
    other_citizenships = models.CharField(max_length=50, null=True, blank=True)
    state_of_rigin = models.CharField(max_length=50, null=True, blank=True)
    county_of_origin = models.CharField(max_length=50, null=True, blank=True)
    payam_of_origin = models.CharField(max_length=50, blank=True ,null= True)
    boma_of_origin = models.CharField(max_length=50, null=True, blank=True)
    state_or_area_of_residence = models.CharField(max_length=50, null=True, blank=True)
    county_of_residence = models.CharField(max_length=50, null=True, blank=True)
    payam_of_residence = models.CharField(max_length=50, null=True, blank=True)
    boma_of_residence = models.CharField(max_length=50, null=True, blank=True)
    tribe = models.CharField(max_length=50, null=True, blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=50,null=True, blank=True)
    physical_address = models.CharField(max_length=50,null=True, blank=True)
    mailing_address = models.CharField(max_length=50,null=True, blank=True)
    telephone_numbers = models.CharField(max_length=50,null=True, blank=True)
    email_address = models.CharField(max_length=50,null=True, blank=True)
    whatsApp_number = models.CharField(max_length=50, null=True, blank=True)
    social_media_handles = models.CharField(max_length=50, null=True, blank=True)
    other_contact_number = models.CharField(max_length=50, null=True, blank=True)
    additional_information = models.CharField(max_length=50, null=True, blank=True)
    marital_status = models.CharField(max_length=52, null=True, blank=True)
    
    how_many_wive = models.CharField(max_length=20, null=True, blank=True)
  
    boys = models.IntegerField( null=True, blank=True)
    girls = models.IntegerField( null=True, blank=True)

    next_full_name = models.CharField(max_length=30, null=True, blank=True)
    next_alias_or_nicknames = models.CharField(max_length=30, null=True, blank=True)
    next_relationship = models.CharField(max_length=50 , null=True, blank=True)
    next_gender = models.CharField(max_length=50, null=True, blank=True)
    
    next_date_of_birth = models.DateField(null=True, blank=True)
    next_place_of_birth = models.CharField(null=True, blank=True, max_length=100)
    
    next_identification_number = models.CharField(max_length=40,  null=True, blank=True)
    next_type_of_identification = models.CharField(max_length=500, null=True, blank=True)
    next_issuing_country = models.CharField(max_length=50, null=True, blank=True)
    next_nationality_at_birth = models.CharField(max_length=50,   null=True, blank=True)
    next_other_citizenships = models.CharField(max_length=50, null=True, blank=True)
    next_state_of_rigin = models.CharField(max_length=50, null=True, blank=True)
    next_county_of_origin = models.CharField(max_length=50, null=True, blank=True)
    next_payam_of_origin = models.CharField(max_length=50, blank=True ,null= True)
    next_boma_of_origin = models.CharField(max_length=50, null=True,  blank=True)
    next_state_or_area_of_residence = models.CharField(max_length=50, null=True, blank=True)
    next_county_of_residence = models.CharField(max_length=50, null=True, blank=True)
    next_payam_of_residence = models.CharField(max_length=50, null=True, blank=True)
    next_boma_of_residence = models.CharField(max_length=50, null=True, blank=True)
    next_tribe = models.CharField(max_length=50, null=True, blank=True)
    next_race = models.CharField(max_length=50, null=True, blank=True)
    next_religion = models.CharField(max_length=50,null=True, blank=True)
    next_physical_address = models.CharField(max_length=50,null=True, blank=True)
    next_mailing_address = models.CharField(max_length=50,null=True, blank=True)
    next_telephone_numbers = models.CharField(max_length=50,null=True, blank=True)
    next_email_address = models.CharField(max_length=50,null=True, blank=True)
    next_whatsApp_number = models.CharField(max_length=50, null=True, blank=True)
    next_social_media_handles = models.CharField(max_length=50, null=True, blank=True)
    next_other_contact_number = models.CharField(max_length=50, null=True, blank=True)
    next_additional_information = models.CharField(max_length=50, null=True, blank=True)
    
    
    
class Employment_information(models.Model):
 
    employee_deginations = models.CharField(max_length=200, null=True, blank=True)
    current_name_of_organization = models.CharField(max_length=50, null=True, blank=True)
    current_type_of_organization = models.CharField(max_length=50, null=True, blank=True)
    current_job_title = models.CharField(max_length=50, null=True, blank=True)
    current_job_description = models.CharField(max_length=50, null=True, blank=True)
    current_address_of_organization = models.CharField(max_length=50, null=True, blank=True)
    current_start_date = models.DateField(null=True, blank=True)
    current_end_date = models.DateField(null=True, blank=True)

    pervious_name_of_organization = models.CharField(max_length=50, null=True, blank=True)
    pervious_type_of_organization = models.CharField(max_length=50, null=True, blank=True)
    pervious_job_title = models.CharField(max_length=50, null=True, blank=True)
    pervious_job_description = models.CharField(max_length=50, null=True, blank=True)
    pervious_address_of_organization = models.CharField(max_length=50, null=True, blank=True)
    pervious_start_date = models.DateField(null=True, blank=True)
    pervious_end_date = models.DateField(null=True, blank=True)

    
    

class Volunteer_informations(models.Model):
    

    current_name_of_organization = models.CharField(max_length=50, null=True, blank=True)
    current_type_of_organization = models.CharField(max_length=50, null=True, blank=True)
    current_job_title = models.CharField(max_length=50, null=True, blank=True)
    current_job_description = models.CharField(max_length=50, null=True, blank=True)
    current_address_of_organization = models.CharField(max_length=50, null=True, blank=True)
    current_start_date = models.DateField(null=True, blank=True)
    current_end_date = models.DateField(null=True, blank=True)

    pervious_name_of_organization = models.CharField(max_length=50, null=True, blank=True)
    pervious_type_of_organization = models.CharField(max_length=50, null=True, blank=True)
    pervious_job_title = models.CharField(max_length=50, null=True, blank=True)
    pervious_job_description = models.CharField(max_length=50, null=True, blank=True)
    pervious_address_of_organization = models.CharField(max_length=50, null=True, blank=True)
    pervious_start_date = models.DateField(null=True, blank=True)
    pervious_end_date = models.DateField(null=True, blank=True)    
    pervious_notes = models.TextField(null=True, blank=True)


class ArmedForcesServiceInformation(models.Model):
    active_services = models.CharField(max_length=40)
    branch_unit = models.CharField(max_length=100)
    

class Specialneedsdetails(models.Model):

    tick_the_item = models.CharField(max_length=100, null=True, blank=True)
    current_need_details = models.TextField(blank=True, null=True)
    disabled = models.CharField(max_length=15, null=True, blank=True)
    disability_war_related = models.CharField(max_length=200, null=True, blank=True)
    orphaned_during = models.CharField(max_length=50, null=True, blank=True)
    age_orphaned_details = models.TextField( null=True, blank=True)
    widowed_during = models.CharField(max_length=50, null=True, blank=True )
    describe_widowed = models.TextField(null=True, blank=True)
    addition_informations = models.TextField(null=True, blank=True)
class RedArmyServicesInformations(models.Model):
    camp = models.CharField(max_length=400, null=True, blank=True)
    division = models.CharField(max_length=400, null=True, blank=True)
    battalion = models.CharField(max_length=400, null=True, blank=True)
    company = models.CharField(max_length=400, null=True, blank=True)
    platoon = models.CharField(max_length=400, null=True, blank=True)
    squad = models.CharField(max_length=400, null=True, blank=True)
    current_rank = models.CharField(max_length=400, null=True, blank=True)
    engaged = models.CharField(max_length=400, null=True, blank=True)
    military_operations = models.TextField(null=True, blank=True)
    any_battle = models.TextField(null=True, blank=True)
    liberation_struggle = models.TextField(null=True, blank=True)
    original_military = models.CharField(max_length=50, null=True, blank=True)
    special_operations = models.TextField(null=True, blank=True)
    civil_administration = models.CharField(max_length=50, null=True, blank=True)
    job_titles_and_locations = models.TextField(null=True, blank=True)
    
    
    
    
class ArmedForcesServiceInformations(models.Model):
    forces_active_service = models.CharField(max_length=50, null=True, blank=True)  
    current_duty_station = models.CharField(max_length=400, null=True, blank=True)
    national_police_service = models.CharField(max_length=400, null=True, blank=True)
    wildlife_service = models.CharField(max_length=400, null=True, blank=True)
    national_prison_service = models.CharField(max_length=400, null=True, blank=True)
    civil_defence_service = models.CharField(max_length=400, null=True, blank=True)
    national_security_service = models.CharField(max_length=400, null=True, blank=True)
    current_rank = models.CharField(max_length=400, null=True, blank=True)
    any_assignments = models.CharField(max_length=50, null=True, blank=True)  
    current_assignment = models.CharField(max_length=400, null=True, blank=True)
    getting_an_assignment = models.CharField(max_length=400, null=True, blank=True)
    rank_adjustment = models.CharField(max_length=400, null=True, blank=True)
    kind_of_assistance = models.TextField(null=True, blank=True)
    rank_or_medal = models.CharField(max_length=50, null=True, blank=True)  
    heroic_act_or_service = models.TextField(null=True, blank=True)
    
    
class CommerdationInformationForms(models.Model):
    image = models.FileField(null=True, blank=True)
    camp = models.CharField(max_length=400, null=True, blank=True)
    division = models.CharField(max_length=400, null=True, blank=True)
    battalion = models.CharField(max_length=400, null=True, blank=True)
    company = models.CharField(max_length=400, null=True, blank=True)
    platoon = models.CharField(max_length=400, null=True, blank=True)
    squad = models.CharField(max_length=400, null=True, blank=True)
    conscription_year = models.CharField(max_length=400, null=True, blank=True)
    current_rank = models.CharField(max_length=400, null=True, blank=True)
    ever_engaged = models.CharField(max_length=50, null=True, blank=True)
    military_operations = models.TextField(null=True, blank=True)
    any_battle = models.TextField(null=True, blank=True)
    special_misssion = models.TextField(null=True, blank=True)
    original_military = models.CharField(max_length=50, null=True, blank=True)
    special_operations = models.TextField(null=True, blank=True)
    civil_administratio = models.CharField(max_length=50, null=True, blank=True)
    job_titles_and_locations = models.TextField(null=True, blank=True)
    rank_or_medal = models.CharField(max_length=50, null=True, blank=True)  
    heroic_act_or_service = models.TextField(null=True, blank=True)
    forces_active_service = models.CharField(max_length=50, null=True, blank=True)  
    
    defence_forces = models.CharField(max_length=200, null=True, blank=True)
    current_duty_station = models.CharField(max_length=400, null=True, blank=True)
    
    police_services = models.CharField(max_length=200, null=True, blank=True)  
    national_police_service = models.CharField(max_length=400, null=True, blank=True)
   
    wildlife_service = models.CharField(max_length=400, null=True, blank=True)
    national_wildlife_service = models.CharField(max_length=400, null=True, blank=True)
    
    prison_service = models.CharField(max_length=400, null=True, blank=True)
    national_prison_service = models.CharField(max_length=400, null=True, blank=True)
    
    civil_service = models.CharField(max_length=400, null=True, blank=True)
    civil_defence_service = models.CharField(max_length=400, null=True, blank=True)
    
    security_service = models.CharField(max_length=400, null=True, blank=True)
    national_security_service = models.CharField(max_length=400, null=True, blank=True)
    
    
    current_rank = models.CharField(max_length=400, null=True, blank=True)
    any_assignments = models.CharField(max_length=50, null=True, blank=True)  
    current_assignment = models.CharField(max_length=400, null=True, blank=True)
    getting_an_assignment = models.CharField(max_length=400, null=True, blank=True)
    rank_adjustment = models.CharField(max_length=400, null=True, blank=True)
    kind_of_assistance = models.TextField(null=True, blank=True)
    recognition_rank_or_medal = models.CharField(max_length=50, null=True, blank=True)  
    such_heroic_act_or_service = models.TextField(null=True, blank=True)
    declaration = models.TextField( null=True, blank=True)
    full_name = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    membership_determination = models.CharField(max_length=40, null=True, blank=True)
    reasons_for_rejection = models.TextField( null=True, blank=True)
    membership_number = models.CharField(max_length=40, null=True, blank=True)
    membership_classification = models.CharField(max_length=40, null=True, blank=True)
    registration_fee_paid = models.CharField(max_length=40, null=True, blank=True)
    subscription_dues_paid = models.CharField(max_length=40, null=True, blank=True)
    any_contribution = models.CharField(max_length=40, null=True, blank=True)
    any_donation = models.CharField(max_length=40, null=True, blank=True)
    official_waiver = models.CharField(max_length=40, null=True, blank=True)
    notes = models.TextField( null=True, blank=True)
    date_of_application = models.DateField(null=True, blank=True) 
    date_of_certification = models.DateField(null=True, blank=True) 
    membership_full_name  = models.CharField(max_length=40, null=True, blank=True)
    membership_date = models.DateField(null=True, blank=True) 
    membership_member_location = models.CharField(max_length=200, null=True, blank=True)    
    
    
class MembershipDeterminationsModel(models.Model):
    membership_determinations = models.CharField(max_length=30, null=True, blank=True)
    reasons_for_rejection = models.TextField( null=True, blank=True)
    membership_number = models.CharField(max_length=40, null=True, blank=True)
    confirmation_code = models.CharField(max_length=40, null=True, blank=True)
    
    membership_classification = models.CharField(max_length=40, null=True, blank=True)
    registration_fee_paid = models.CharField(max_length=40, null=True, blank=True)
    subscription_dues_paid = models.CharField(max_length=40, null=True, blank=True)
    any_contribution = models.CharField(max_length=40, null=True, blank=True)
    any_donation = models.CharField(max_length=40, null=True, blank=True)
    official_waiver = models.CharField(max_length=40, null=True, blank=True)
    notes = models.TextField( null=True, blank=True)
    date_of_application = models.DateField(null=True, blank=True) 
    date_of_admission = models.DateField(null=True, blank=True) 
    full_name  = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateField(null=True, blank=True) 
    member_location = models.CharField(max_length=200, null=True, blank=True)     
    
    
    
    
class MartyrsInformationModel(models.Model):
    image = models.FileField(null=True, blank=True)
    causality_status = models.FileField(null=True, blank=True)
    cause_of_death = models.TextField( null=True, blank=True)
    led_to_death = models.TextField( null=True, blank=True)
    full_name = models.CharField(max_length=30, null=True, blank=True)
    alias_or_nicknames = models.CharField(max_length=30, null=True, blank=True)
    relationship = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    place_of_death = models.DateField(null=True, blank=True)
                              
                              
    issuing_country = models.CharField(max_length=50, null=True, blank=True)
    
    nationality_at_birth = models.CharField(max_length=50,   null=True, blank=True)
    other_citizenships = models.CharField(max_length=50, null=True, blank=True)
    state_of_rigin = models.CharField(max_length=50, null=True, blank=True)
    county_of_origin = models.CharField(max_length=50, null=True, blank=True)
    payam_of_origin = models.CharField(max_length=50, blank=True ,null= True)
    boma_of_origin = models.CharField(max_length=50, null=True, blank=True)

    tribe = models.CharField(max_length=50, null=True, blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)                          
    additional_information = models.CharField(max_length=50, null=True, blank=True)
     
    camp = models.CharField(max_length=400, null=True, blank=True)
    division = models.CharField(max_length=400, null=True, blank=True)
    battalion = models.CharField(max_length=400, null=True, blank=True)
    company = models.CharField(max_length=400, null=True, blank=True)
    platoon = models.CharField(max_length=400, null=True, blank=True)
    squad = models.CharField(max_length=400, null=True, blank=True)
    rank = models.CharField(max_length=400, null=True, blank=True)
    causality_marital_status = models.CharField(max_length=400, null=True, blank=True)
    how_many_wive = models.CharField(max_length=20, null=True, blank=True)
  
    boys = models.CharField(max_length=30, null=True, blank=True)
    girls = models.CharField(max_length=30, null=True, blank=True)
    next_full_name = models.CharField(max_length=30, null=True, blank=True)
    next_alias_or_nicknames = models.CharField(max_length=30, null=True, blank=True)
    next_relationship = models.CharField(max_length=50 , null=True, blank=True)
    next_gender = models.CharField(max_length=50, null=True, blank=True)
    
    next_date_of_birth = models.DateField(null=True, blank=True)
    next_place_of_birth = models.CharField(null=True, blank=True, max_length=100)
    
    next_identification_number = models.CharField(max_length=40,  null=True, blank=True)
    next_type_of_identification = models.CharField(max_length=500, null=True, blank=True)
    next_issuing_country = models.CharField(max_length=50, null=True, blank=True)
    next_nationality_at_birth = models.CharField(max_length=50,   null=True, blank=True)
    next_other_citizenships = models.CharField(max_length=50, null=True, blank=True)
    next_state_of_rigin = models.CharField(max_length=50, null=True, blank=True)
    next_county_of_origin = models.CharField(max_length=50, null=True, blank=True)
    next_payam_of_origin = models.CharField(max_length=50, blank=True ,null= True)
    next_boma_of_origin = models.CharField(max_length=50, null=True,  blank=True)
    next_state_or_area_of_residence = models.CharField(max_length=50, null=True, blank=True)
    next_county_of_residence = models.CharField(max_length=50, null=True, blank=True)
    next_payam_of_residence = models.CharField(max_length=50, null=True, blank=True)
    next_boma_of_residence = models.CharField(max_length=50, null=True, blank=True)
    next_tribe = models.CharField(max_length=50, null=True, blank=True)
    next_race = models.CharField(max_length=50, null=True, blank=True)
    next_religion = models.CharField(max_length=50,null=True, blank=True)
    next_physical_address = models.CharField(max_length=50,null=True, blank=True)
    next_mailing_address = models.CharField(max_length=50,null=True, blank=True)
    next_telephone_numbers = models.CharField(max_length=50,null=True, blank=True)
    next_email_address = models.CharField(max_length=50,null=True, blank=True)
    next_whatsApp_number = models.CharField(max_length=50, null=True, blank=True)
    next_social_media_handles = models.CharField(max_length=50, null=True, blank=True)
    next_other_contact_number = models.CharField(max_length=50, null=True, blank=True)
    next_additional_information = models.CharField(max_length=50, null=True, blank=True)
    
    person_full_name = models.CharField(max_length=30, null=True, blank=True)
    person_alias_or_nicknames = models.CharField(max_length=30, null=True, blank=True)
    person_relationship = models.CharField(max_length=50 , null=True, blank=True)
    person_gender = models.CharField(max_length=50, null=True, blank=True)
    
    person_date_of_birth = models.DateField(null=True, blank=True)
    person_place_of_birth = models.CharField(null=True, blank=True, max_length=100)
    
    person_identification_number = models.CharField(max_length=40,  null=True, blank=True)
    person_type_of_identification = models.CharField(max_length=500, null=True, blank=True)
    person_issuing_country = models.CharField(max_length=50, null=True, blank=True)
    person_nationality_at_birth = models.CharField(max_length=50,   null=True, blank=True)
    person_other_citizenships = models.CharField(max_length=50, null=True, blank=True)
    person_state_of_rigin = models.CharField(max_length=50, null=True, blank=True)
    person_county_of_origin = models.CharField(max_length=50, null=True, blank=True)
    person_payam_of_origin = models.CharField(max_length=50, blank=True ,null= True)
    person_boma_of_origin = models.CharField(max_length=50, null=True,  blank=True)
    person_state_or_area_of_residence = models.CharField(max_length=50, null=True, blank=True)
    person_county_of_residence = models.CharField(max_length=50, null=True, blank=True)
    person_payam_of_residence = models.CharField(max_length=50, null=True, blank=True)
    person_boma_of_residence = models.CharField(max_length=50, null=True, blank=True)
    person_tribe = models.CharField(max_length=50, null=True, blank=True)
    person_race = models.CharField(max_length=50, null=True, blank=True)
    person_religion = models.CharField(max_length=50,null=True, blank=True)
    person_physical_address = models.CharField(max_length=50,null=True, blank=True)
    person_mailing_address = models.CharField(max_length=50,null=True, blank=True)
    person_telephone_numbers = models.CharField(max_length=50,null=True, blank=True)
    person_email_address = models.CharField(max_length=50,null=True, blank=True)
    person_whatsApp_number = models.CharField(max_length=50, null=True, blank=True)
    person_social_media_handles = models.CharField(max_length=50, null=True, blank=True)
    person_other_contact_number = models.CharField(max_length=50, null=True, blank=True)
    person_additional_information = models.CharField(max_length=50, null=True, blank=True)
    rank_or_medal = models.CharField(max_length=50, null=True, blank=True)  
    heroic_act_or_service = models.TextField(null=True, blank=True)