from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from .forms import NoteForm
from .forms import TagForm
from .models import Note, Tag


def superuser_only(user):
    return user.is_authenticated


@user_passes_test(superuser_only, login_url="/")
def index_view(request):
    notes = Note.objects.filter(user=request.user)
    tags = Tag.objects.all()
    return render(request, 'notes/index.html', {'notes': notes, 'tags': tags})


@user_passes_test(superuser_only, login_url="/")
def add_note(request):
    id = request.GET.get('id', None)
    if id is not None:
        note = get_object_or_404(Note, id=id)
    else:
        note = None

    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, 'Note Deleted!')
            return HttpResponseRedirect(reverse('notes:index'))

        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return HttpResponseRedirect(reverse('notes:index'))

    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/addnote.html', {'form': form, 'note': note})


@user_passes_test(superuser_only, login_url="/")
def add_tag(request):
    id = request.GET.get('id', None)
    if id is not None:
        tag = get_object_or_404(Tag, id=id)
    else:
        tag = None

    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            tag.delete()
            messages.add_message(request, messages.INFO, 'Tag Deleted!')
            return HttpResponseRedirect(reverse('notes:index'))

        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            t = form.save(commit=False)
            t.slug = slugify(t.label)
            t.save()
            messages.add_message(request, messages.INFO, 'Tag Added!')
            return HttpResponseRedirect(reverse('notes:index'))

    else:
        form = TagForm(instance=tag)

    return render(request, 'notes/addtag.html', {'form': form, 'tag': tag})


# @user_passes_test(superuser_only, login_url="/")
# def tag_search(request, **kwargs):
#     slug = kwargs['slug']
#     tag = get_object_or_404(Tag, slug=slug)
#     notes = tag.notes.all()
#
#     return render(request, 'notes/search.html', {'notes': notes, 'tag': tag})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit', None)
        if query is not None:
            lookups = Q(label__icontains=query)
            results = Note.objects.filter(lookups)

            return render(request, 'search.html', {'results': results, 'submitbutton': submitbutton})

        else:
            return render(request, 'base.html')

    else:
        return render(request, 'search.html')

