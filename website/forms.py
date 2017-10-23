from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from website.models import Post

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # address = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'username', 
            'first_name',
            'last_name', 
            'email',
            'password1',
            'password2' 
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.firstname = self.cleaned_data['first_name']
        user.lastname = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'email',
            'first_name',
            'last_name',
            
        }
class HomeForm(forms.ModelForm):

    post = forms.CharField()
    gender = forms.CharField()
    dob = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()
    state = forms.CharField()
    postcode = forms.CharField()
    userType = forms.CharField()

    class Meta:
        model = Post
        fields = ('post', 'gender', 'dob', 'phone', 'address', 'state', 'postcode', 'userType' )
    # user = models.ForeignKey(User) 
