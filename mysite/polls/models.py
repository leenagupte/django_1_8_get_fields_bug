import uuid
from django.db import models


class Question(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def serialize(self):
        return self._meta.get_fields_with_model()



class Choice(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def serialize(self):
        fields = self._meta.get_fields_with_model()
        field_names = [field.name for field, _ in fields]
        for f in field_names:
            v = getattr(self, f)
            print v
