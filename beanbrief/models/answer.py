from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db import models

from .question import Question


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    @classmethod
    def create_answer(cls, author:'User', question:'Question', content:str, **kwargs) -> 'Answer':
        return cls.objects.create(
            author=author,
            question=question,
            content=content,
            create_date=timezone.now(),
            **kwargs
        )
    
    @classmethod
    def get_answer_by_id(cls, id: int) -> 'Answer':
        return get_object_or_404(cls, pk=id)

    def update_answer(self, content:str) -> 'Answer':
        self.content=content
        self.modify_date=timezone.now()
        self.save()
        return self

    def delete_answer(self) -> None:
        self.delete()
    
    def add_voter(self, voter: 'User'):
        self.voter.add(voter)
