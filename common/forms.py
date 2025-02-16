# common/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User  # <-- 반드시 지정해야 합니다.
        fields = ("username", "email")  # password1, password2는 상속받은 UserCreationForm에서 처리합니다.
