from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from polls.models import Poll
from polls.forms import SignUpForm

from polls.forms import CreatePollForm


# Create your views here.


def get_base_context(request, pagename):
    return {
        'pagename': pagename,
        'user': request.user,
    }


def index_page(request):
    context = get_base_context(request, 'Voting')
    return render(request, 'pages/index.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'pages/register.html', {'form': form, 'pagename': "Sign Up"})


def add_poll(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            new_poll = form.save(commit=False)
            new_poll.author = request.user
            new_poll.save()
            return redirect('vote', poll_id=new_poll.id)
    else:
        form = CreatePollForm()
    context = {'form': form, 'pagename': 'Add Poll'}
    return render(request, 'pages/add_poll.html', context)

@login_required
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
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('view_poll', poll.id)

    context = {'poll': poll, 'pagename': 'Vote'}
    return render(request, 'pages/vote.html', context)


def view_poll(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll': poll, 'pagename': 'Poll Result'}
    return render(request, 'pages/view_poll.html', context)


def my_polls(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls,
        'pagename': "Polls",
    }
    return render(request, 'pages/my_polls.html', context)