from django.forms import ModelForm
from .models import Poll, User

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']