from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages

from .models import Photo, Blog, Appointment
from .forms import AppointmentForm, CreateUserForm, BlogForm
from .decorators import allowedGroups


# Create your views here.
def kasperHome(request):
    photo = Photo.objects.all()
    return render(request, 'home.html', {"photo": photo})

def aboutMe(request):
    return render(request, 'aboutMe.html', {})

@login_required(login_url="/login")
def contact(request):
    booked = False
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?booked=True')
    else:
        form = AppointmentForm
        if 'booked' in request.GET:
            booked = True
        return render(request, 'contact.html', {"form": form, "booked": booked})

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {"blogposts": blog})

@login_required(login_url="/login")
@allowedGroups(["Photographer"])
def blogEdit(request):
    blog = Blog.objects.all()
    return render(request, 'blogEdit.html', {"blogposts": blog})

@login_required(login_url="/login")
@allowedGroups(["Photographer"])
def deletePost(request, post_id):
    post = Blog.objects.get(pk=post_id)
    post.delete()
    return HttpResponseRedirect('/blogEdit/')

@login_required(login_url="/login")
@allowedGroups(["Photographer"])
def addPost(request):
    submitted = False
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blogEdit/')
    else:
        form = BlogForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addPost.html', {"form": form, 'submitted': submitted})

@login_required(login_url="/login")
@allowedGroups(["Photographer"])
def editPost(request, post_id):
    blog = Blog.objects.get(pk=post_id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/blogEdit')

    return render(request, 'editPost.html',{"blog": blog, "form": form})

# only for photographers and admins. Shows requested Appointments
@login_required(login_url="/login")
@allowedGroups(["Photographer"])
def requestedAppointments(request):
    app = Appointment.objects.all()
    return render(request, 'requested.html', {"appointments": app})

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {"photos": photos})

def signUp(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            newUser = form.save()
            newUser.groups.add(Group.objects.get(name="Customer"))

            firstName = form.cleaned_data.get('first_name')
            messages.success(request, f"Congrats {firstName}. You're signed up!")
            return HttpResponseRedirect('/login')    # change link later

    return render(request, 'signUp.html', {"form": form})

def loginPage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == "POST":
        username = request.POST.get('username')    # change to Email?
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')  # change to HTTPRedirect
        else:
            messages.info(request, 'Username or password is Incorrect. Try Again.')
    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/login')

