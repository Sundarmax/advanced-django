from django.shortcuts import render

from django.views import generic

from .models import Question

class IndexView(generic.ListView):
    template_name       = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('id')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class DeleteView(generic.DeleteView):
    model = Question
    success_url = "/polls/"
