from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'id_num', 'mobile', 'position')
        labels = {
            'fullname':'Full Name',
            'id_num':'ID. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['id_num'].required = False