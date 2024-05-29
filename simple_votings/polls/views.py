from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from polls.forms import CreatePollForm
from polls.forms import SignUpForm
from polls.models import Poll


# Create your views here.


def get_base_context(request, pagename):
    return {
        'pagename': pagename,
        'user': request.user,
    }


def index_page(request):
    most_popular_poll = Poll.objects.annotate(
        total_votes=F('option_one_count') + F('option_two_count') + F('option_three_count')).order_by(
        '-total_votes').order_by('-total_votes').first()

    context = {
        'pagename': 'Voting',
        'most_popular_poll': most_popular_poll,
    }

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
    context = {'form': form, 'pagename': 'Add a Poll'}
    return render(request, 'pages/add_poll.html', context)


@login_required
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_options = request.POST.getlist('poll') if poll.question_type == 'multiple' else [request.POST['poll']]
        if not selected_options:
            return HttpResponse(400, 'No options selected')

        for option in selected_options:
            if option == 'option1':
                poll.option_one_count += 1
            elif option == 'option2':
                poll.option_two_count += 1
            elif option == 'option3':
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


def view_polls(request):
    all_polls = Poll.objects.all()
    my_polls = Poll.objects.filter(author=request.user) if request.user.is_authenticated else Poll.objects.none()

    context = {
        'pagename': 'Polls',
        'all_polls_by_freshness': all_polls.order_by('-time'),
        'all_polls_by_popularity': all_polls.annotate(
            total_votes=F('option_one_count') + F('option_two_count') + F('option_three_count')).order_by(
            '-total_votes'),
        'my_polls_by_freshness': my_polls.order_by('-time'),
        'my_polls_by_popularity': my_polls.annotate(
            total_votes=F('option_one_count') + F('option_two_count') + F('option_three_count')).order_by(
            '-total_votes'),
    }

    return render(request, 'pages/view_polls.html', context)
