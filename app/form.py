from django import forms


my_choices = (
        ("What is your Month of Birth?" , "What is your Month of Birth?"),
        ("What is Your Mother's Name?" , "What is Your Mother's Name?"),
        ("What is Your Nickname?" , "What is Your Nickname?"),
        ("What is Pet Name?" , "What is Pet Name?"),
        
    )


class image_upload(forms.Form):
    image = forms.ImageField(widget= forms.FileInput(attrs={'class': "form-control", 'type' : 'file', 'placeholder' : 'Select Paper'}), required=True)

class user_profile_form(forms.Form):
    
    fname = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'First Name'}), required=True)
    lname = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Last Name'}), required=True)
    security_qus = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    ans = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Your Answer'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'email', 'placeholder' : 'Enter Email Address'}), required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'password', 'placeholder' : 'Enter Password'}), required=True)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'password', 'placeholder' : 'Re-Enter Password'}), required=True)

class user_login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'email', 'placeholder' : 'Enter Email Address'}), required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'password', 'placeholder' : 'Enter Password'}), required=True)
    security_qus = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    ans = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Your Answer'}), required=True)