from rest_framework import generics, permissions
from django.utils import timezone  
from pybo.models import Question
from pybo.serializers import QuestionSerializer

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.get_all_questions()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, create_date=timezone.now())

class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(modify_date=timezone.now())  
