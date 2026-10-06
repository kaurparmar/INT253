from django import forms
MONTHS=[
    ('Jan', 'Jan'),
    ('Feb', 'Feb'),
    ('Mar', 'Mar'),
    ('Apr', 'Apr'),
    ('May', 'May'),
    ('June', 'June'),
    ('Jul', 'Jul'),
    ('Aug', 'Aug'),
    ('Sep', 'Sep'),
    ('Oct', 'Oct'),
    ('Nov', 'Nov'),
    ('Dec', 'Dec')
]
YEARS=[(str(i), str(i)) for i in range(1900, 2025)]
class MyForm(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email address'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password'}))
    day=forms.ChoiceField(choices=[(str(i), str(i)) for i in range(1, 32)], widget=forms.Select(attrs={'class':'form-control'}))
    month=forms.ChoiceField(choices=[('','MONTHS')]+MONTHS, widget=forms.Select())
    year=forms.ChoiceField(choices=[('','YEARS')]+YEARS, widget=forms.Select())
