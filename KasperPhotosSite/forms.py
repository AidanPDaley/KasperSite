from django import forms
from .models import Photo, Appointment, Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'phoneNumber', 'email', 'dateRangeLow', 'dateRangeHigh', 'location', 'info',)

        labels = {
            'name': "Name:",
            'phoneNumber': "Phone Number:",
            'email': "Email:",
            'dateRangeLow': "Earliest Available Date:",
            'dateRangeHigh': "Latest Available Date:",
            'location': "Location",
            'info': "Description",

        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'dateRangeLow': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First available day'}),
            'dateRangeHigh': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last available day (leave blank if specific date)'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'info': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe Your Perfect Photoshoot Here!'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'blogText', 'image')

        labels = {
            'title': "Title",
            'createdAt': "Time",
            'image': "",
            'blogText': "",

        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Post Title'}),
            'createdAt': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Current Time by Default'}),
            'taskName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your blogpost here'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),

        }