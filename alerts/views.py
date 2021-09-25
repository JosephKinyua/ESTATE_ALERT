from django.shortcuts import render, redirect
from .models import Post, Business, Neighborhood, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .form import UserForm, ProfileForm, BusinessForm, PostForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html',)

@login_required(login_url='/accounts/login/')
def index(request):
    if request.user.profile.neighborhood == None:
        messages.success(request, 'Please fill out you Neighborhood')
        return redirect('uprofile')
    else:
        neighdetails = Neighborhood.objects.get(
            name=request.user.profile.neighborhood)
        businesses = Business.objects.filter(
            neighborhood=request.user.profile.neighborhood)
        stories = Post.objects.filter(
            neighborhood=request.user.profile.neighborhood)

        params = {
            'neighdetails': neighdetails,
            'businesses': businesses,
            'stories': stories,
        }
        return render(request, 'index.html', params)

@login_required(login_url='/accounts/login/')
def profile(request):
    print(request.GET)
    if request.method == 'POST':
        print(request.POST)
        userform = UserForm(request.POST or None, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        businessform = BusinessForm(request.POST)
        postiiform = PostForm(request.POST)

        curr_neighborhood = request.user.profile.neighborhood

        if userform.is_valid and profileform.is_valid():
            userform.save()
            profileform.save()
            messages.success(request, 'Profile updated successfully')

        if businessform.is_valid():
            busi = businessform.save(commit=False)
            busi.username = request.user
            busi.neighborhood = curr_neighborhood
            busi.save()

        if postiiform.is_valid():
            post = postiiform.save(commit=False)
            post.postuser = request.user
            post.neighborhood = curr_neighborhood
            post.save()

        return redirect('uprofile')
        
    curr_user = Profile.objects.get(username=request.user)
    userform = UserForm(instance=request.user)
    profileform = ProfileForm(instance=request.user.profile)
    businessform = BusinessForm()
    postiiform = PostForm()

    allbusiness = Business.objects.filter(username=request.user)
    stories = Post.objects.filter(postuser=request.user)

    params = {
        'curr_user': curr_user,
        'userform': userform,
        'profileform': profileform,
        'businessform': businessform,
        'postiiform': postiiform,
        'allbusiness': allbusiness,
        'stories': stories
    }
    return render(request, 'profile/index.html', params)
