from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from accounts.models import Profile


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        new_profile = Profile.objects.create(
            user=user,
        )
        return new_profile


class UpdateForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        new_profile = Profile.objects.create(
            user=user,
        )
        return new_profile


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

