from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from .models import Note
from django.utils import timezone
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('notes')
            except IntegrityError:
                #return HttpResponse('Username already exists')
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is wrong'
            })
        else:
            login(request, user)
            return redirect('notes')

@login_required
def notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-createdAt')
    return render(request, 'notes.html', {'notes': notes})

@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def create_note(request):
    if request.method == 'GET':
        return render(request, 'create_note.html', {
            'form': NoteForm
        })
    else:
        try:
            form = NoteForm(request.POST)
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
            return redirect('notes')
        except ValueError:
            return render(request, 'create_note.html', {
                'form': NoteForm,
                'error': 'Please provide valid data'
            })

@login_required
def note_detail(request, note_id):
    if request.method == 'GET':
        note = get_object_or_404(Note, pk=note_id, user=request.user)
        form = NoteForm(instance=note)
        return render(request, 'note_detail.html', {'note': note, 'form': form})
    else:
        try:
            note = get_object_or_404(Note, pk=note_id, user=request.user)
            form = NoteForm(request.POST, instance=note)
            form.save()
            return redirect('notes')
        except ValueError:
            return render(request, 'note_detail.html', {'note': note, 'form': form, 'error': 'Error updating note.'}) 

@login_required
def complete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    if request.method == 'POST':
        note.dateCompleted = timezone.now()
        note.completed = True
        note.save()
        return redirect('notes')

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
