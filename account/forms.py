# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from account.models import Company,Customer

# class AddCustomerForm(forms.ModelForm):
#     class Meta:
#         model=Customer
#         fields=('user', 'gender', 'dob', 'phone', 'address', 'pin', 'profile_pic')
#         widgets={
#             'user': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'user_id', 'type':'hidden'}),
#             'gender': forms.Select(attrs={'class': 'form-control',}),
#             'dob': forms.DateInput(attrs={'class': 'form-control'}),
#             'phone':forms.NumberInput(attrs={'class':'form-control'}),
#             'address':forms.TextInput(attrs={'class':'form-control'}),
#             'pin':forms.TextInput(attrs={'class':'form-control'}),
#         }

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget= forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )


# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     email = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     first_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     last_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_customer', 'is_company')