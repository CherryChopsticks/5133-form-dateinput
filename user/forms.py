from django import forms

from wagtail.users.forms import UserEditForm, UserCreationForm
from wagtail.admin.widgets import AdminDateInput


class CustomUserEditForm(UserEditForm):
    date_joined = forms.DateField(
        widget=AdminDateInput(),
        help_text="Date joined",
    )


class CustomUserCreationForm(UserCreationForm):
    date_joined = forms.DateField(
        widget=AdminDateInput(),
        help_text="Date joined",
    )
