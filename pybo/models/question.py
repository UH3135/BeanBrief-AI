from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject

    @classmethod
    def create_question(cls, author: 'User', subject: str, content: str, **kargs) -> 'Question':
        return cls.objects.create(
            author=author,
            subject=subject,
            content=content,
            create_date=timezone.now(),
            **kargs
        )
    
    def update_question(self, subject: str, content: str) -> 'Question':
        self.subject = subject
        self.content = content
        self.modify_date = timezone.now()
        self.save()
        return self

    def delete_question(self) -> None:
        self.delete()