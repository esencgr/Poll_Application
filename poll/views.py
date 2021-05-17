from django.shortcuts import render, redirect, Http404
from django.http import HttpResponse, Http404
from .forms import CreatePollForm
from .models import Poll


def index(request):
    # polls = Poll.objects.all()
    # context = {
    #     'polls' : polls
    # }
    return render(request, 'index.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'home.html', context)

def create(request):
    if not request.user.is_superuser:
        raise Http404

    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()

    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

def update(request, poll_id):
    if not request.user.is_authenticated:
        raise Http404

    poll = Poll.objects.get(pk=poll_id)
    form = CreatePollForm(request.POST or None, instance=poll) 
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

def delete(request, poll_id):
    if not request.user.is_authenticated:
        raise Http404
    
    poll = Poll.objects.get(pk=poll_id)
    poll.delete( )
    return redirect('home')
 
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid forz')
        poll.save()
        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'results.html', context)