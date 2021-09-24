from django.shortcuts import render, redirect
from .models import Post, Business, Neighborhood, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .form import UserForm, ProfileForm, BusinessForm, PostForm
# Create your views here.
def home(request):
    return render(request,'home.html',)
