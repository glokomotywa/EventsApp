from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Event, Type, Comment, Profile
from .forms import EventForm, UserUpdateForm, ProfileUpdateForm




def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
        
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An Error occured during registration')
            
    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    events = Event.objects.filter(
        Q(type__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(location__icontains=q)
        )
    
    types = Type.objects.all()
    event_count = events.count()
    
    context =  {'events': events, 'types': types, 'event_count': event_count}
    return render(request, 'base/home.html', context)

def event(request, pk):
    event = Event.objects.get(id=pk)
    comments = event.comment_set.all().order_by('-created')
    
    interested = event.interested.all()
    
    if 'interested' in request.POST:
            if request.user.is_authenticated:
                if request.user in event.interested.all():
                    event.interested.remove(request.user)
                else:
                    event.interested.add(request.user)
                return redirect('event', pk=event.id)
    body = request.POST.get('body', '').strip()
    if body and request.user.is_authenticated:
        comment = Comment.objects.create(
            user = request.user,
            event = event,
            body = request.POST.get('body'),
        )
        return redirect('event', pk=event.id)
    
    context = {'event': event, 'comments': comments, 'interested': interested}
    return render(request, 'base/event.html', context)

@login_required(login_url='login')
def manageAccount(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('manage-account')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'base/manage_account.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    events = user.event_set.all()
    event_comment = user.comment_set.all()
    types = Type.objects.all()
    context = {'user': user, 'events': events, 'event_comment': event_comment, 'types': types, 'is_owner': request.user == user}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def createEvent(request):
    form = EventForm()
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser = request.user
            event.save()
            return redirect('home')
            
    context = {'form': form}
    return render(request, 'base/event_form.html', context)

@login_required(login_url='login')
def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    
    if request.user != event.organiser:
        return HttpResponse("You don't have permissions to do this action")
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid:
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/event_form.html', context)

@login_required(login_url='login')
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    
    if request.user != event.organiser:
        return HttpResponse("You don't have permissions to do this action")
    
    if request.method == 'POST':
        event.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': event})

@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    
    if request.user != comment.user:
        return HttpResponse("You don't have permissions to do this action")
    
    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': comment})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

def trigger_error(request):
    raise Exception("Test 500 error")