from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Blog, Project, Message, Account
from . models import *
from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt

def my_custom_csrf_failure_view(request, reason=""):
    return HttpResponseForbidden("CSRF verification failed. Please try again.")



def index(request):
    blogs = Blog.objects.all()
    projects = Project.objects.all()
    return render(request, 'pages/home.html', {'blogs': blogs, 'projects': projects})

def about_page(request):
    return render(request, 'pages/about.html')
def adminbloglist_page(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/adminbloglist.html', {'blogs': blogs})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('adminbloglistpage')
def delete_bloguser(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('bloglistpage')

def contact_page(request):
    return render(request, 'pages/contact.html')


def bloglist_page(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/bloglist.html', {'blogs': blogs})



def adminblogpost_page(request):
    return render(request, 'pages/adminblogpost.html')


def form_page(request):
    return render(request, 'pages/form.html')


def admin_page(request):
    blogs = Blog.objects.all()
    latest_blogs = Blog.objects.order_by('-date')[:5]  # Fetch the 5 latest blog entries
    projects = Project.objects.all()
    messages = Message.objects.all()


    # Filter accounts where accountType is 'U'
    accounts = Account.objects.filter(accountType='U')

    # Count the filtered accounts
    total_accounts = accounts.count()

    donations = Donation.objects.all()

    return render(request, 'pages/admin.html',
                  {'blogs': blogs, 'latest_blogs': latest_blogs, 'projects': projects, 'messages': messages,
                   'total_accounts': total_accounts, 'donations': donations})

def login_page(request):
    return render(request, 'pages/login.html')

from django.core.exceptions import ObjectDoesNotExist

from django.core.exceptions import ObjectDoesNotExist

def LoginUser(request):
    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']

        try:
            # Checking the email with the database
            user = Account.objects.get(email=email)

            if user.password == password:
                # We are getting user data in session


                # Check account type and redirect accordingly
                if user.accountType == 'U':  # Assuming 'U' represents a User account type
                    request.session['Name'] = user.name
                    return redirect('homepage')
                elif user.accountType == 'A':  # Assuming 'A' represents an Admin account type
                    return redirect('adminpage')
                else:
                    message = "Try Again"
                    return render(request, "pages/login.html", {'msg': message})


            else:
                message = "Password does not match"
                return render(request, "pages/login.html", {'msg': message})

        except ObjectDoesNotExist:
            message = "User does not exist"
            return render(request, "pages/login.html", {'msg': message})

    return render(request, "pages/login.html")

def logout_user(request):
    logout(request)
    return render(request, 'pages/login.html')
def addproject_page(request):
    return render(request, 'pages/addproject.html')

def addproject(request):
    if request.method == 'POST':
        a = request.POST.get('projecTitle', '')
        b = request.POST.get('description', '')
        c = request.POST.get('subDescription', '')
        d = request.POST.get('date', '')
        e = request.FILES.get('photo', None)

        mem = Project(projecTitle=a, description=b, subDescription=c, date=d, photo=e)
        mem.save()
    return redirect('adminpage')


def addblog(request):
    if request.method == 'POST':
        names = request.POST.get('name', '')
        titles = request.POST.get('title', '')
        dates = request.POST.get('date', '')
        images = request.FILES.get('photo', None)
        contents = request.POST.get('content', '')

        mem = Blog(name=names, blogTitle=titles, date=dates, photo=images, content=contents)
        mem.save()
    return redirect('bloglistpage')

def addcontact(request):
    if request.method == 'POST':
        names = request.POST.get('name', '')
        emails = request.POST.get('email', '')
        messages = request.POST.get('message', '')

        mem = Message(name=names, email=emails, message=messages)
        mem.save()
        message = "Your message has been sent successfully."
        return render(request, "pages/contact.html", {'msg': message})

    # Handle cases where the request method is not POST
    return HttpResponse("Invalid request method.")

def adddonation_page(request):
    return render(request, 'pages/adddonation.html')

def adddonation(request):
    if request.method == 'POST':
        names = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        images = request.FILES.get('proof', None)
        messages = request.POST.get('message', '')

        mem = Donation(donor_name=names, amount=amount, proof=images, message=messages)
        mem.save()
        message = "Thank you for donation."
        return render(request, "pages/adddonation.html", {'msg': message})

        # Handle cases where the request method is not POST
    return HttpResponse("Invalid request method.")



def edit_blog(request, blog_id):
    # Retrieve the blog object using the provided blog_id
    blog = get_object_or_404(Blog, id=blog_id)

    context = {
        'abc': blog,
    }

    return render(request, 'pages/editblog.html', context)

def uprec(request, blog_id):
    x = request.POST['name']
    y = request.POST['title']
    a = request.POST['date']

    # Access 'photo' from request.FILES
    # Note: Make sure your form has the 'enctype="multipart/form-data"' attribute
    b = request.FILES['photo'] if 'photo' in request.FILES else None

    c = request.POST['content']

    mem = get_object_or_404(Blog, id=blog_id)
    mem.name = x
    mem.blogTitle = y
    mem.date = a

    # Save the file only if it is provided
    if b:
        mem.photo = b

    mem.content = c
    mem.save()
    return render(request, "pages/editblog.html")


def adminblogpost(request,id):
    mem=Blog.objects.get(id=id)
    return render(request, "pages/adminblogpost.html",{'mem':mem})


def blogpost_page(request, id):
    mem = Blog.objects.get(id=id)
    return render(request, 'pages/blogpost.html', {'mem':mem})

def editblogpostpage(request,id):
    mem=Blog.objects.get(id=id)
    return render(request, "pages/editblog.html",{'mem':mem})


def editblogpost(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        date = request.POST.get('date')
        content = request.POST.get('content')

        # Check if an image file is provided in the form
        pimage = request.FILES.get('photo')

        # Get the existing blog post or return a 404 response if not found
        mem = Blog.objects.get(id=id)

        # Update the existing blog post with the new data
        mem.name = name
        mem.blogTitle = title
        mem.date = date
        if pimage:
            mem.photo = pimage
        mem.content = content
        mem.save()
        return redirect('bloglistpage')

def delete_blogs(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('adminpage')

def delete_project(request, blog_id):
    blog = get_object_or_404(Project, id=blog_id)
    blog.delete()
    return redirect('adminpage')

def editprojectpage(request,id):
    mem=Project.objects.get(id=id)
    return render(request, "pages/editproject.html",{'mem':mem})


def editprojectpost(request, id):
    if request.method == 'POST':
        projecTitle = request.POST.get('projecTitle')
        description = request.POST.get('description')
        subDescription = request.POST.get('subDescription')
        date = request.POST.get('date')

        # Check if an image file is provided in the form
        pimage = request.FILES.get('photo')

        # Get the existing blog post or return a 404 response if not found
        mem = Project.objects.get(id=id)

        # Update the existing blog post with the new data
        mem.projecTitle = projecTitle
        mem.description = description
        mem.subDescription = subDescription
        if pimage:
            mem.photo = pimage
        mem.date = date
        mem.save()
        return redirect('adminpage')