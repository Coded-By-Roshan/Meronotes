from django import forms
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Feeds, Note
from django.contrib import messages
from .forms import CreateNote
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')

def feedBack_view(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            exp = request.POST['exp']
            feed = Feeds(full_name=name, experience=exp)
            feed.save()
            messages.success(request, "Feedback sent.")
        return render(request, 'home.html')
    except:
        return render(request, 'error.html')

def note_view(request):
    notes = Note.objects.all().order_by('-timestamp')
    params = {'title':'Notes', 'notes':notes}
    return render(request, 'notes.html', params)

def detial_view(request, pk):
    note_detail = Note.objects.filter(pk=pk)
    params = {'title':'Details', 'notes':note_detail }
    return render(request, 'detail.html', params)

def contact_view(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def addNote_view(request):
    if request.method == 'POST':
        form = CreateNote(request.POST , request.FILES)
        if form.is_valid():
            note = Note(user=request.user, title=form.cleaned_data['title'], file=form.cleaned_data['file'])
            note.save()
            # form.save()
            messages.success(request, "You have Successfully Added a Note")
        return redirect('note')
    else:
        form = CreateNote()
    params = {'title':'Add Notes', 'forms':form}
    return render(request, 'addnote.html',params)


def managecontact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contactmessage = request.POST.get('message')
        send_mail('Blog message', 
        f" name {first_name} {last_name} sent \n{contactmessage}\n\n from {email}",
        email,
        ['pokhrelroshan224@gmail.com'],
        fail_silently=False
        )
        messages.success(request, 'Thanks for contacting us.')
    return redirect('home')


def login_view(request):
    return render(request, 'login.html')

def search_view(request):
    query = request.POST['query']
    if len(query) > 25:
        return render(request, 'error.html')
    if len(query) <= 0:
        messages.error(request, "Please pass correct keyword to search")
        return redirect('home')
    search_result = Note.objects.filter(title__icontains=query)
    if search_result.count() == 0:
        return HttpResponse("<h1>NO RESULT FOUND</h1>")
    params = {'search_results':search_result}
    return render(request, 'query.html', params)

