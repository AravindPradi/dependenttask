from django import forms
from .models import Student, Branch


class StudentForm(forms.ModelForm):
    purpose = forms.ChoiceField(choices=[('Select', 'Select'), ('enquiry', 'Enquiry'), ('return', 'Return')],
                                label='Purpose')


    class Meta:
        model = Student
        fields = ('name', 'birthdate','age','gender','phone_number','mail_id','address','materials_provided', 'college','branch','book','pen','exam_papers')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'college' in self.data:
            try:
                college_id = int(self.data.get('college'))
                self.fields['branch'].queryset = Branch.objects.filter(college_id=college_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.college.branch_set.order_by('name')