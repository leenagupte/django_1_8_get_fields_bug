import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question, Choice


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        # future_question.save()
        # choice = Choice(question=future_question)

        # print choice.serialize()
        print future_question.serialize()

        self.assertEqual(future_question.was_published_recently(), False)

