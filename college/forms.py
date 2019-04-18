from django import forms
from django.core.exceptions import ValidationError

def checkUserName(value):
    if value.isalpha()== False:
        raise ValidationError("Plaese give valid username")

'''def checkEmail(value):
    if value.find('mytectra.com') == -1:
        raise ValidationError("Please provide a mail with mytectra.com domain")'''



class FormExample(forms.Form):

    temp = (
        ('', '--Select option --'),
        ('hydrabad', 'Hydrabad'),
        ('pune', 'Pune'),
        ('bangalore', 'Bangalore'),
    )
    gn = (
        ('m','Male'),
        ('f','Female'),
    )
    username = forms.CharField(validators=[checkUserName],
        error_messages={'required':'username cannot blank',
                       'min_length':'Minium 8 characters or a digits'},
                       label="Name",required=True,min_length=8,
                       max_length=20)

    email = forms.EmailField()
    password1 =forms.CharField(label ='Password',max_length=20)
    password2 =forms.CharField(label ='Re-Password',max_length=20)
    address = forms.CharField(max_length=250, widget=forms.Textarea)
    city = forms.ChoiceField(choices = temp)
    gender = forms.ChoiceField(choices=gn,widget=forms.RadioSelect())
    is_active = forms.CharField(widget=forms.CheckboxInput)

    def clean(self):
        form_data = self.cleaned_data
        if 'password1' in form_data and 'password2' in form_data:
            if form_data['password1']!= form_data['password2']:
                self.errors['password1'] = ['Given password did not match']


        if 'name' in form_data and form_data['name'].isdigit() == True:
            self.errors['name'] =['Give a valid username']


        if 'email' in form_data and form_data['email'].split('@')[1] !='mytectra.com':
            self.errors['email'] = ['Invalid Email']

        return form_data

# new class------------------------------------

class FormExample2(forms.Form):

    dropdown = (
        ('','-- select --'),
        ('new york','New York'),
        ('pune','Pune'),
        ('bangalore','bangalore'),
        ('amritsar','Amritsar'),
    )

    dropdown_country = (
        ('','--select state--'),
        ('india','India'),
        ('united states','United states'),

    )

    radiobt =(
        ('f','Male'),
        ('m','Female'),
    )


    uname = forms.CharField(label='Username', required = False)

    email = forms.EmailField(label='Email',required=False)
    password1 = forms.CharField(label='Password',required = False)
    password2 = forms.CharField(label='Re-Password',required =False)
    city = forms.ChoiceField(choices= dropdown,required=False)
    radiobutton = forms.ChoiceField(label='Gender', choices=radiobt, widget=forms.RadioSelect(),required=False)
    is_active = forms.ChoiceField(widget=forms.CheckboxInput())

    def clean(self):
        form_content = self.cleaned_data
        if 'password1' in form_content and 'password2' in form_content:
            if form_content['password1'] and form_content['password2'] != "":
                if form_content['password1']!=form_content['password2']:
                    self.errors['password2']=['password did not match ']
            else:
                self.errors['password1'] = ['This field is mendatory']
                self.errors['password2'] = ['This field is mendatory']


        if 'uname' in form_content:
            if form_content['uname'].isalpha() == True:
                if len(form_content['uname'])< 8:
                    self.errors['uname'] =['Please enter minimum 8 characters in a field and maximum 20 ']
                elif len(form_content['uname']) > 20:
                    self.errors['uname'] = ['Please provide a maximum 20 characters ']
            else:
                self.errors['uname'] = ['Give a valid username']

        if form_content['uname'] == "":
            self.errors['uname'] = ['Field is required ']

        if 'email' in form_content:
            if form_content['email'] !="":
                if form_content['email'].split('@')[1] != 'syntel.com':
                    self.errors['email'] = ['provide an email with syntel.com domain']
            else:
                self.errors['email'] = ['This field cannot be empty']

            if 'city' in form_content:
                if form_content['city']=="":
                    self.errors['city'] = ['choose your city its mendatory ']

        if 'radiobutton' in form_content:
            if form_content['radiobutton'] == '':
                self.errors['radiobutton'] = ['choose ']


        return form_content




