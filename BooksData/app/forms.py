from django import forms

from django.contrib.auth.models import User

from app.models import Book,UserProfile

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','author','price')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','city')