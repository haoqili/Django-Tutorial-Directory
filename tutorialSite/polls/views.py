from polls.models import Poll, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

''' #3

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]

    #1 output = ', '.join([p.question for p in latest_poll_list])
    #1 return HttpResponse(output)

    #2 from django.template import Context, loader
    #2 t = loader.get_template('polls/index.html')
    #2 c = Context({
    #2    'latest_poll_list': latest_poll_list,
    #2 })
    #2 return HttpResponse(t.render(c))

    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})


def detail(request, poll_id):
    #1 return HttpResponse("You're looking at poll %s." % poll_id)

    #2 from django.http import Http404
    #2 try:
    #2     p = Poll.objects.get(pk=poll_id)
    #2 except Poll.DoesNotExist:
    #2     raise Http404

    p = get_object_or_404(Poll, pk=poll_id)

    # RequestContext is for detail.html's CSRF
    return render_to_response('polls/detail.html', {'poll': p},
                               context_instance = RequestContext(request))

def results(request, poll_id):
    #1 return HttpResponse("You're looking at the results of poll %s." % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})
'''

def vote(request, poll_id):
    #1 return HttpResponse("You're voting on poll %s." % poll_id)

    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        #3 return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
