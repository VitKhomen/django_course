from django import forms

from lesson_5.models import Client, Flower


class MyForm(forms.Form):
    name = forms.CharField(label='User name', initial='User name',
                           error_messages={'required': 'Enter your name'})
    profile_picture = forms.FileField(
        label='Profile picture', widget=forms.FileInput)
    additional_file = forms.FileField(
        label='Additional file', widget=forms.FileInput)
    email = forms.EmailField(initial='admin@admin.com', label='Email',
                             error_messages={'required': 'Enter your email'})
    password = forms.CharField(max_length=20, min_length=8, required=False,
                               widget=forms.PasswordInput(), label='Password')
    age = forms.IntegerField(initial=18, required=False, label='Age')
    agreement = forms.BooleanField(required=False, label='Agreement')
    average_score = forms.FloatField(label='Average score', initial=7.2)
    sex = forms.ChoiceField(
        choices=[('M', 'male'), ('F', 'female')], label='Gender')
    birthday = forms.DateField(
        widget=forms.SelectDateWidget, label='Birthday', required=False)
    work_experience = forms.DurationField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your work experience'}),
        label='Work experience', required=False)


class FormFromModel(forms.ModelForm):
    class Meta:
        model = Flower
        fields = '__all__'


class ValidFOrm(forms.Form):
    name = forms.CharField(label='User name', )
    email = forms.EmailField(label='Email')
