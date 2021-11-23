from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .forms import List_FORM
from .models import List

# Create your views here.
def index(request):
    return render(request, 'html-files/index.html', {})

def FORM(request):
    submitted = False
    if request.method == 'POST':
        Form = List_FORM(request.POST)
        if Form.is_valid():
            Form.save()
            return HttpResponseRedirect('/index/form?submitted=True',)
    else:
        Form = List_FORM
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'html-files/index.html', {
        'Submitted': submitted,
    })

def View_List(request):
    return render(request, 'html-files/list.html', {
        'list': List.objects.all()
    })

def delete(request, delete_id):
    item = List.objects.get(pk=delete_id)
    item.delete()
    return redirect('list-function')

def update(request, update_id):
    Event_list = List.objects.get(pk=update_id)
    Form = List_FORM(request.POST or None, instance=Event_list)
    if Form.is_valid():
        Form.save()
        return redirect('list-function')
    return render(request, 'html-files/update.html', {
        'Event_list': Event_list,
        'form': Form,
    })
