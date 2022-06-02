from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileCreationForm(UserCreationForm):
    '''Extending the UsercreationForm with the additional field(s) on the CustomUser model.'''
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'email', 'phone', 'city', 'state', 'country']


class UserProfileUpdateForm(UserChangeForm):
    '''Extending the UserChangeForm with the additional field(s) on the CustomUser model.'''
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'email', 'phone', 'city', 'state', 'country']
