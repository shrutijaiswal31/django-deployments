from django.shortcuts import render
from .models import User
from .forms import TestForm, UserForm
# Create your views here.


def index(request):
    return render(request, 'app2/index.html')

def user(request):
    userobj = User.objects.order_by('firstName')
    user_dict = {"user_list": userobj}
    return render(request, 'app2/user.html', context=user_dict)

def userform(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, 'app2/userform.html', context={'form':form})

def form_view(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    form_dict = {"form_key": form}
    return render(request, 'app2/app_forms.html', context=form_dict)
