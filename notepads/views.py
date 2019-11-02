from django.shortcuts import render
from .models import Topic


def index(request):
    return render(request, 'notepads/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'notepads/topics.html', context)


def topic(request, t_id):
    topic = Topic.objects.get(id=t_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'notepads/topic.html', context)
