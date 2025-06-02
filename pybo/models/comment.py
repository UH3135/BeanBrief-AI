from typing import Any
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .question import Question
from .answer import Answer


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

    @classmethod
    def create_comment(cls, **kwargs) -> 'Comment':
        kwargs['create_date'] = timezone.now()
        return cls.objects.create(**kwargs)
    
    def update_comment(self, **kwargs) -> 'Comment':
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        return self
    
    def delete_comment(self) -> None:
        self.delete()