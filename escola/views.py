from rest_framework import viewsets
from escola.models import Aluno
from config.serializer import AlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
        queryset = Aluno.objects.all()
        serializer_class = AlunoSerializer


