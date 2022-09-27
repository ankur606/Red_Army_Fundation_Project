from multiprocessing import context
from pydoc import describe
from traceback import print_tb
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from .forms import Employment_informationForms
from web_app.models import *
from Admin_dasboard.models import*
from web_app.forms import*
from rest_framework.permissions import IsAuthenticated
# Create your views

#===== Home PAge View======#
class AboutsViews(View):
    def get(self, request):
        data = AboutModel.objects.all()
        other_data = OtherAboutsPageData.objects.all() 
        return render(request, 'dasboard/web_templates/about-us.html', {'data':data, 'other_data':other_data })
class HomePageView(View):
    def get(self, request):
        data = HomePageContents.objects.all()
        event_data = EventsModel.objects.all()
        return render(request, 'dasboard/web_templates/index.html',{'data':data,"event_data":event_data})

class ShowListsFormsView(View):
    def get(self, request):
        return render(request, 'dasboard/web_templates/forms/list_of_forms.html')

class EmploymentInformationViews(View):
    def get(self, request):
        data_forms = Employment_informationForms()
        return render(request, 'dasboard/web_templates/forms/employment-information.html', {'emp_forms':data_forms})
    
    def post(self, request):
        employee_form = Employment_informationForms(request.POST)
       
        if employee_form.is_valid():
            employee_form.save()
            messages.success(request, 'Employees  Informations Forms Submit Successfully..!!')
            
            return redirect('showForms')
        return render(request, 'dasboard/web_templates/forms/employment-information.html', {'emp_forms':employee_form})
        
        
        
         
class MembershipDeterminationViews(View):
    def get(self, request):
        forms_data = MembershipDeterminationsForms()
        return render(request, 'dasboard/web_templates/forms/membership-determination.html',{'forms_data':forms_data}) 
    def post(self,  request):
        forms_data = MembershipDeterminationsForms(request.POST)
        if forms_data.is_valid():
            forms_data.save() 
            messages.success(request, 'Memberships Determinatios Informations Forms Submit Successfully..!!')
            
            return redirect('showForms')
            
class SpecialNeedsDdetailsViews(View):
    def get(self, request):
        snd_forms = SpecialneedsdetailsForms()
        return render(request, 'dasboard/web_templates/forms/special-needs-details.html', {'forms_data':snd_forms})    
    
    
    def post(self, request):
        need_forms = SpecialneedsdetailsForms(request.POST)
    
        if need_forms.is_valid():
            need_forms.save()
            messages.success(request, 'Employees  Informations Forms Submit Successfully..!!')
            
            return redirect('showForms')
        return redirect('special_needsDetails')
            
    
 
    
    
    
class MembershipDeclarationViews(View):
    def get(self, request):
        forms_fileds = MemberDeclarationForms() 
        return render(request, 'dasboard/web_templates/forms/member-declaration.html', {'forms_fileds':forms_fileds})    
    
    def post(self, request):
        data = MemberDeclarationForms(request.POST)
 
        if data.is_valid():
            data.save()
            messages.success(request, 'Member DeclarationForms Submit Successfully..!!')
          
            return redirect("showForms")
        return redirect('memberDeclaration')
class RedArmyServiceInformationView(View):
    def get(self, request):
        red_army_forms = RedArmyServicesInformationsForms()
        return render(request, 'dasboard/web_templates/forms/red-army-service-information.html', {'army_forms':red_army_forms})    
    def post(self, request):
        form_data = RedArmyServicesInformationsForms(request.POST, request.FILES)
        if form_data.is_valid():
            messages.success(request, 'Red Army Services Informations Forms  Submit Successfully..!!')
            form_data.save()
            return redirect("showForms") 

class RedArmyMartyrsRecordView(View):
    def get(self, request):
        forms_data = MartyrsInformationModelForms()
        return render(request, 'dasboard/web_templates/forms/red-army-martyrs-record.html', {'forms_data':forms_data})    
    def post(self, request):
        forms_data = MartyrsInformationModelForms(request.POST, request.FILES)
       
        if forms_data.is_valid():
            messages.success(request, 'Red Army Martyrs Informations Forms  Submit Successfully..!!')
            forms_data.save()    
            return redirect("showForms") 
        











class CommendationInformationView(View):
    def get(self, request):
        forms_data = CommerdationInformationForm()
        return render(request, 'dasboard/web_templates/forms/sspdf-commendation-request-form.html', {'forms_data':forms_data})    
    def post(self, request):
        form_data = CommerdationInformationForm(request.POST, request.FILES)
   
        if form_data.is_valid():
            messages.success(request, 'Commerdation InformationForm Forms  Submit Successfully..!!')
            form_data.save()
            return redirect("showForms") 
        
class ArmedForcesServicesInformationView(View):
    def get(self, request):
        armed_forms = ArmedForcesServiceInformationsForms()
        return render(request, 'dasboard/web_templates/forms/armed-forces-service-information.html', {'armed_forms':armed_forms})    
    
    def post(self, request):
        armed_forms = ArmedForcesServiceInformationsForms(request.POST)
     
        if armed_forms.is_valid():
        
            armed_forms.save()
            
            
            messages.success(request, 'Armed Forces  Informations Forms Submit Successfully..!!')
        
            return redirect('showForms')
class VolunteerInformationViews(View):
    def get(self, request):
        return render(request, 'dasboard/web_templates/forms/volunteer-information.html')    
    def post(self, request):
        current_name_organization = request.POST.get('current_name_of_organization')
        current_type_Organization = request.POST.get('current_type_of_organization')
        current_job_title = request.POST.get('current_job_title')
        current_job_description = request.POST.get('current_job_description')
        current_start_date = request.POST.get('current_start_date')
        current_end_date = request.POST.get('current_end_date')
        
        current_address_organization = request.POST.get('current_address_of_organization')
        
        pervious_name_organization = request.POST.get('pervious_name_of_organization')
        pervious_type_Organization = request.POST.get('pervious_type_of_organization')
        pervious_job_title = request.POST.get('pervious_job_title')
        pervious_job_description = request.POST.get('pervious_job_description')
        pervious_start_date = request.POST.get('pervious_start_date')
        pervious_end_date = request.POST.get('pervious_end_date')
        
        pervious_address_organization = request.POST.get('pervious_address_of_organization')
        pervious_notes = request.POST.get('pervious_notes')
        data = Volunteer_informations(
            
          current_name_of_organization = current_name_organization,
          current_type_of_organization = current_type_Organization,
          current_job_title = current_job_title,
          current_job_description = current_job_description,
          current_address_of_organization = current_address_organization,
          current_start_date = current_start_date,
          current_end_date = current_end_date,
          
          pervious_name_of_organization = pervious_name_organization,
          pervious_type_of_organization = pervious_type_Organization,
          pervious_job_title = pervious_job_title,
          pervious_job_description = pervious_job_description,
          pervious_address_of_organization = pervious_address_organization,
          pervious_start_date = pervious_start_date,
          
          pervious_end_date = pervious_end_date,
          pervious_notes = pervious_notes
        )
        messages.success(request, "Volunteer Informations  Forms Submit Successfully..!!")
        data.save()
        return redirect('showForms')
class EducationInformationView(View):
    def get(self, request):
        
     
        return render(request, 'dasboard/web_templates/forms/education-information.html',) 
    
    
  
    def post(self, request):
        id = request.user.id
      
        primary_school_name = request.POST.get('primary_school_name')
        primary_country_study_name = request.POST.get('primary_country_study_name')
        primary_year_of_commencement = request.POST.get('primary_year_of_commencement')  
        primary_year_of_completion = request.POST.get('primary_year_of_completion')
        primary_certification_attained = request.POST.get('primary_certification_attained')
        
        secondary_name_of_school = request.POST.get('secondary_name_school')
        secondary_country_study_name = request.POST.get('secondary_country_of_study')
        secondary_year_of_commencement = request.POST.get('secondary_year_of_commencement')  
        secondary_year_of_completion = request.POST.get('secondary_year_of_completion')
        secondary_certification_attained = request.POST.get('secondry_certification_attained')

           
        diploma_school_name = request.POST.get('diploma_school_name')
        diploma_country_study_name = request.POST.get('diploma_country_of_study')
        diploma_year_of_commencement = request.POST.get('diploma_year_of_commencement')  
        diploma_year_of_completion = request.POST.get('diploma_year_of_completion')
        diploma_certification_attained = request.POST.get('diploma_certification_attained')
        
        associate_school_name = request.POST.get('associate_school_name')
        associate_country_of_study = request.POST.get('associate_country_of_study')
        associate_year_of_commencement = request.POST.get('associate_year_of_commencement')  
        associate_year_of_completion = request.POST.get('associate_year_of_completion')
        associate_certification_attained = request.POST.get('associate_certification_attained')
        
        
        bachelor_school_name = request.POST.get('bachelor_school_name')
        bachelor_country_study_name = request.POST.get('bachelor_country_of_name')
        bachelor_year_of_commencement = request.POST.get('bachelor_year_of_commencement')  
        bachelor_year_of_completion = request.POST.get('bachelor_year_of_completion')
        bachelor_certification_attained = request.POST.get('bachelor_certification_attained')
        
        master_school_name = request.POST.get('master_school_name')
        master_country_study_name = request.POST.get('master_country_name')
        master_year_of_commencement = request.POST.get('master_year_of_commencement')  
        master_year_of_completion = request.POST.get('master_year_of_completion')
        master_certification_attained = request.POST.get('master_certification_attained')
        
        philosohy_school_name = request.POST.get('philosohy_school_name')
        philosohy_country_study_name = request.POST.get('philosohy_ountry_of_study')
        philosohy_year_of_commencement = request.POST.get('philosohy_year_of_commencement')  
        philosohy_year_of_completion = request.POST.get('philosohy_year_of_completion')
        philosohy_certification_attained = request.POST.get('philosohy_certification_attained')
        
        describe_your_thaughts = request.POST.get('self_taught')
        
        special_skilss = request.POST.get('special_skilss')
        
        specialization_indetail = request.POST.get('specialization_indetail')
        professional_certificates = request.POST.get('professional_certificates')
        
  
        
        education_data = EducationInformation(
      
            primary_school_name = primary_school_name,
            primary_country_study_name = primary_country_study_name,
            primary_year_of_commencement = primary_year_of_commencement,
            primary_year_of_completion = primary_year_of_completion,
            primary_certification_attained = primary_certification_attained,
            
            secondary_name_of_school = secondary_name_of_school,
            secondary_country_of_study = secondary_country_study_name,
            secondary_year_of_commencement = secondary_year_of_commencement,
            secondary_year_of_completion = secondary_year_of_completion,
            secondary_certification_attained = secondary_certification_attained,
            
            diploma_name_of_school = diploma_school_name,
            diploma_country_of_study = diploma_country_study_name,
            diploma_year_of_commencement = diploma_year_of_commencement,
            diploma_year_of_completion =  diploma_year_of_completion,
            diploma_certification_attained = diploma_certification_attained,
            
            associate_name_of_school = associate_school_name,
            associate_country_of_study = associate_country_of_study,
            associate_year_of_commencement = associate_year_of_commencement,
            associate_year_of_completion =  associate_year_of_completion,
            associate_certification_attained = associate_certification_attained,
            
            bachelor_name_of_school = bachelor_school_name,
            bachelor_country_of_study = bachelor_country_study_name,
            bachelor_year_of_commencement = bachelor_year_of_commencement,
            bachelor_year_of_completion =  bachelor_year_of_completion,
            bachelor_certification_attained = bachelor_certification_attained,
            
            master_name_of_school = master_school_name,
            master_country_of_study = master_country_study_name,
            master_year_of_commencement = master_year_of_commencement,
            master_year_of_completion =  master_year_of_completion,
            master_certification_attained = master_certification_attained,
            
            philosohy_name_of_school = philosohy_school_name,
            philosohy_country_of_study = philosohy_country_study_name,
            philosohy_year_of_commencement = philosohy_year_of_commencement,
            philosohy_year_of_completion =  philosohy_year_of_completion,
            philosohy_certification_attained = philosohy_certification_attained,

            describe_your_thaughts = describe_your_thaughts,
            
            describe_special_skills = special_skilss,
            
            describe_specialization_indetail = specialization_indetail,
            describe_professional_certificates = professional_certificates)
        education_data.save()
        messages.success(request, 'Educations Informations Forms Submit Successfully..!!')
        return redirect('showForms')    
class PersonalInfomationView(View):
    def get(self, request):
       
        return render(request, "dasboard/web_templates/forms/personal-information.html")
    
    
    def post(self, request):
        personal_forms = PersonalInformationForms(request.POST, request.FILES)
      
        if personal_forms.is_valid():
        
            personal_forms.save()
            
            
            messages.success(request, 'Personal Informations Forms Submit Successfully..!!')
        
            return redirect('showForms')
        return redirect("personalIformation")
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
     
   