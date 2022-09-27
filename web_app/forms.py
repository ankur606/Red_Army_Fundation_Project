from dataclasses import fields

from xml.parsers.expat import model
from django import forms

from .models import*

class PersonalInformationForms(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = "__all__"

Employee_desginations = (('Salaried Employee (A person who is regularly working and earns a salary) ', 'Salaried Employee - (A person who is regularly working and earns a salary)'),
              ('Self Employment - (A person who owns and operates a business)', ' Self-Employment - (A person who owns and operates a business)'),
              ('part time - (A part-time employee is someone who works fewer hours than what an employer considers to be full-time)', 'Part-time - (A part-time employee is someone who works fewer hours than what an employer considers to be full-time)'),
              ('Internship - (An intern is a trainee who has signed on with an organization for a brief period)', ' Internship - (An intern is a trainee who has signed on with an organization for a brief period)'),
              ('casual  - (A person who is employed for a small period)', 'Casual - (A person who is employed for a small period)'),
              ('seasonal - (A person who is temporary work to meet an organizations needs during certain times of the year) ', ' Seasonal Employee - (A person who is temporary work to meet an organizations needs during certain times of the year)'))

    
class Employment_informationForms(forms.ModelForm):
    employee_deginations = forms.MultipleChoiceField( label="Select Employee Designation",  choices=Employee_desginations, widget=forms.CheckboxSelectMultiple, required=False )
    class Meta:
        model = Employment_information
        fields = "__all__"  



Yes_No = (
    ('Yes', 'Yes'),
    ('No', "No")
)      


Tick_The_Item = (
    ('Employment', 'Employment'),
    ('Join Armed Forces', 'Join Armed Forces'),
    ('Review of Rank', 'Review of Rank'),
    ('Adult Education', 'Adult Education'),
    ('Vocational Skills', 'Vocational Skills'),
    ('University Scholarship', 'University Scholarship'),
    ('Medical Treatment', 'Medical Treatment'),
    ('Financial Assistance', 'Financial Assistance'),
    ('Other', 'Other')
    
    
)
class SpecialneedsdetailsForms(forms.ModelForm):
    disabled = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    orphaned_during = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    widowed_during = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    tick_the_item = forms.MultipleChoiceField(choices=Tick_The_Item , widget=forms.CheckboxSelectMultiple, required=False)
    class Meta:
        model = Specialneedsdetails
        fields = "__all__"        
        


MY_DECLARATIONS = (
        ('I Certify That I Am Approved By The Red Army Foundation To Complete This Web Form And That The Information Provided In This Submission - Membership Application Form And Declaration Form – Is Accurate And Correct To The Best Of My Knowledge; Iunderstand That', 'I Certify That I Am Approved By The Red Army Foundation To Complete This Web Form And That The Information Provided In This Submission - Membership Application Form And Declaration Form – Is Accurate And Correct To The Best Of My Knowledge; Iunderstand That.'),
        ('Membership Policy Requires Me To Abide By The Constitution, Policies, And Procedures Of The Red Army Foundation, As May Be Amended From Time To Time.','Membership Policy Requires Me To Abide By The Constitution, Policies, And Procedures Of The Red Army Foundation, As May Be Amended From Time To Time.'),
        ('Information Provided By Me To The Red Army Foundation From Time To Time And Including The Non-sensitive Information Provided In This Declaration Form May Be Shared By The Red Army Foundation For Administrative, Funding, And Legislative Compliance Purposes With The Relevant Authorities And Other Relevant Bodies, In The Best Interest Of The Member.','Information Provided By Me To The Red Army Foundation From Time To Time And Including The Non-sensitive Information Provided In This Declaration Form May Be Shared By The Red Army Foundation For Administrative, Funding, And Legislative Compliance Purposes With The Relevant Authorities And Other Relevant Bodies, In The Best Interest Of The Member.'),
        ('Personal Information Collected By Red Army Foundation (“the Foundation”) Is For Managing The Foundation, Membership Requirements, Preservation Of Social History, And Interacting With The Governments And Partners Who May Assist The Member.', 'Personal Information Collected By Red Army Foundation (“the Foundation”) Is For Managing The Foundation, Membership Requirements, Preservation Of Social History, And Interacting With The Governments And Partners Who May Assist The Member.'),
        ('The Personal Information Collected Will Not Be Released For Commercial Gain And Will Be Maintained In A Secure Location For Your Privacy.','The Personal Information Collected Will Not Be Released For Commercial Gain And Will Be Maintained In A Secure Location For Your Privacy.')
    )
class MemberDeclarationForms(forms.ModelForm):
    declaration = forms.MultipleChoiceField(choices=MY_DECLARATIONS, widget=forms.CheckboxSelectMultiple, required=False)
    class Meta: 
        model = MemberDeclaration
        fields = "__all__"
        
            
class RedArmyServicesInformationsForms(forms.ModelForm):
    engaged = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    original_military = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    civil_administration = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    class Meta:
        model = RedArmyServicesInformations
        fields = "__all__"            


class ArmedForcesServiceInformationsForms(forms.ModelForm):
    forces_active_service = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    any_assignments = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    rank_adjustment = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    rank_or_medal = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    
    class Meta:
        model = ArmedForcesServiceInformations
        fields = "__all__"      
Determinations =(
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected')
)    
Classification =(
    ('Organized Red Army', 'Organized Red Army'),
    ('Liberation Generation', 'Liberation Generation'),
    ('Seeds of the Nation', 'Seeds of the Nation'),
    ('Associate Member', 'Associate Member')
) 
Defence_forces = (
    ('South Sudan People’s Defence Forces', 'South Sudan People’s Defence Forces'),
)

Police_services = (
    ('South Sudan National Police Service', 'South Sudan National Police Service'),
)

Wildlife_service = (
    ('South Sudan National Wildlife Service', 'South Sudan National Wildlife Service'),
)

Prison_service = (
    ('National Prison Service Of South Sudan', 'National Prison Service Of South Sudan'),
)

Civil_service = (
    ('South Sudan National Civil Defence Service', 'South Sudan National Civil Defence Service'),
)

Security_service = (
    ('South Sudan National Security Service','South Sudan National Security Service'),
)

class CommerdationInformationForm(forms.ModelForm):
    ever_engaged = forms.ChoiceField(choices=Yes_No,  widget=forms.RadioSelect, required=False)
   
    civil_administratio = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    rank_or_medal = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    forces_active_service = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    any_assignments = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    recognition_rank_or_medal = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    rank_adjustment = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    original_military = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    subscription_dues_paid = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    any_contribution = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    any_donation = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    official_waiver = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    registration_fee_paid = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    declaration = forms.MultipleChoiceField(choices=MY_DECLARATIONS, widget=forms.CheckboxSelectMultiple, required=False)
    membership_determination = forms.ChoiceField(choices=Determinations, widget=forms.RadioSelect, required=False)
    membership_classification =  forms.ChoiceField(choices=Classification, widget=forms.RadioSelect, required=False)
   
    defence_forces = forms.ChoiceField(choices=Defence_forces, widget=forms.RadioSelect, required=False)
    police_services = forms.ChoiceField(choices=Police_services, widget=forms.RadioSelect, required=False)
    wildlife_service = forms.ChoiceField(choices=Wildlife_service, widget=forms.RadioSelect, required=False)
    prison_service = forms.ChoiceField(choices=Prison_service, widget=forms.RadioSelect, required=False)
    civil_service = forms.ChoiceField(choices=Civil_service, widget=forms.RadioSelect, required=False)
    security_service = forms.ChoiceField(choices=Security_service, widget=forms.RadioSelect, required=False)
    class Meta:
        model = CommerdationInformationForms
        fields = "__all__"    
    
    
 
class MembershipDeterminationsForms(forms.ModelForm):
    membership_determinations = forms.ChoiceField(choices=Determinations, widget=forms.RadioSelect, required=False)
    membership_classification =  forms.ChoiceField(choices=Classification, widget=forms.RadioSelect, required=False)
    registration_fee_paid = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    subscription_dues_paid = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    any_contribution = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    any_donation = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    official_waiver = forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect, required=False)
    class Meta:
        model = MembershipDeterminationsModel
        fields = "__all__"     
        

Causality_status = (
    ('Death','Death'),
    ('Kill in Action','Kill in Action'),
    ('Missing in Action and Presumed Dead', 'Missing in Action and Presumed Dead'),
    ('Captured and Presumed Dead', 'Captured and Presumed Dead')
    
) 



class MartyrsInformationModelForms(forms.ModelForm):
    rank_or_medal =  forms.ChoiceField(choices=Yes_No, widget=forms.RadioSelect(attrs={'class':'radio-button'}), required=False) 
    causality_status = forms.ChoiceField(choices=Causality_status, widget=forms.RadioSelect, required=False)
    class Meta:
        model = MartyrsInformationModel
        fields = "__all__"     
        