from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from accounts.forms import UserRegistrationForm, MobileNumberForm
from accounts.models import MobileNumber
# Create your views here.

def userRegistration(request):
    userForm = UserRegistrationForm()
    numberForm = MobileNumberForm()
    return render(request, template_name='accounts/signup.html', context={'user_form':userForm, 'number_form':numberForm})