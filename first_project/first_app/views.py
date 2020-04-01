from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,Webpage,Users
from . import forms
from first_app.forms import NewUserFormName

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'text': 'hello world',
        'number':100,
        'access_records':webpages_list
    }
    return render(request,'first_app/index.html',context=date_dict)

def users(request):
    users_list = Users.objects.order_by('first_name')
    users_dict = {
        'user_records':users_list
    }
    return render(request,'first_app/users.html',context=users_dict)

def new_users(request):
    form = NewUserFormName()

    if request.method == 'POST':
        form = NewUserFormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("VALIDATION SUCCESS")
            print("FIRST NAME: " + form.cleaned_data['first_name'])
            print("LAST NAME: " + form.cleaned_data['last_name'])
            print("EMAIL: " + form.cleaned_data['email'])

            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'first_app/sign_up_page.html',{'form':form})

def other(request):
    return render(request,'first_app/other.html')

def relative(request):
    return render(request,'first_app/relative_url_templates.html')
