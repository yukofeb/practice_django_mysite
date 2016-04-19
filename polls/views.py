from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice
from django.template import RequestContext


def index(request):
    latest_polls = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request,
                  'index.html',
                  {'latest_polls': latest_polls})


def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('polls/templates/detail.html', {'poll': p},
    #                          context_instance=RequestContext(request)
    return render(request,
                  'detail.html',
                  {'poll': p},
                  context_instance=RequestContext(request))


def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('polls/templates/results.html', {'poll': p})
    return render(request,
                  'results.html',
                  {'poll': p})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
       return render_to_response('polls/templates/detail.html', {
            'poll': p,
            'error_message': '選択肢を選んでいません。',
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
