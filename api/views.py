from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Note

@login_required
def note_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if title and body:
            Note.objects.create(user=request.user, title=title, body=body)
        return redirect('note_list')
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/list.html', {'notes': notes})

@login_required
def delete_note(request, note_id):
    Note.objects.filter(id=note_id, user=request.user).delete()
    return redirect('note_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
