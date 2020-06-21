from django.test import TestCase

from django.test import RequestFactory

from model_bakery import baker

from pprint import pprint

# imports from app 
from polls.models import *
from polls.views import *

class TestVoteView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.question_model = baker.make('polls.Question')
        self.choice_models = baker.make(
            'polls.Choice',
            question=self.question_model,
            _quantity=3)

    def test_get_queryset(self):
        choice = self.choice_models[0]
        view = VoteView()
        queryset = view.get_queryset(choice.pk)
        self.assertEquals(queryset.choice_text, choice.choice_text)
