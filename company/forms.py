from django import forms
from company.models import Company

class CompanyForm(forms.ModelForm):
  #  name = forms.CharField(max_length=50)

    class Meta:

        model = Company
        fields = '__all__'


# gor custom validations
        # def clean(self):
        #     form_data = self.cleaned_data