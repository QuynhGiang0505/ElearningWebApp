from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import messages

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('../../')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			# mail=request.POST.get('email')
			# if User.objects.filter(email=mail).exists():
			# 	# messages.add_message(request, messages.INFO, 'Email is already exists!')
			# 	# messages.warning(request,'Email is already exists!')
			# 	return render(
			# 		request, 
			# 		'accounts/register.html', 
			# 		{
			# 			'form':form
			# 		}
        	# 	)
			if form.is_valid():
				# save form in the memory not in database  
				user = form.save(commit=False)  
				user.is_active = False  
				user.save()  
				# to get the domain of the current site  
				current_site = get_current_site(request)  
				mail_subject = 'Activation link has been sent to your email id'  
				message = render_to_string('accounts/acc_active_email.html', {  
					'user': user,  
					'domain': current_site.domain,  
					'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
					'token':account_activation_token.make_token(user),  
				})  
				to_email = form.cleaned_data.get('email')  
				email = EmailMessage (  
							mail_subject, message, to=[to_email]  
				)  
				email.send()  
				return HttpResponse('Please confirm your email address to complete the registration') 
				# form.save()
				# user = form.cleaned_data.get('username')
				# messages.success(request, 'Account was created for ' + user)
		return render(
            request, 
            'accounts/register.html', 
            {
                'form':form
            }
        )

def loginPage(request):
	if request.user.is_authenticated:
		return redirect("../../GTEAMS")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('../../GTEAMS')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('../../GTEAMS')

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  
