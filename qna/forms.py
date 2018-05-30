from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Questions, Questionpaper


class StudentForm(UserCreationForm):
    CHOICES = (('Male', 'Male',), ('Female', 'Female',))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-con\
trol'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    school = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'School','class': 'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Format: YYYY-MM-DD','class':'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone number','class': 'form-control'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), choices=CHOICES)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','school', 'dob', 'gender','p\
hone')


class QuestionsForm(ModelForm):

    class Meta:
        model = Questions
        fields = '__all__'
        labels = {"qtype":"Type","klass":"class"}


class QuestionpaperForm(ModelForm):
    
    class Meta:
        model = Questionpaper
        fields = '__all__'
        labels  = {"paperid":"ID","papername":"Name","klass":"class"}