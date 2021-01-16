from django.db.models.query import QuerySet
from rest_framework import viewsets,generics
from escola.models import Aluno,Curso, Matricula
from .serializer import AlunoSerializer,CursoSerializer,MatriculaSerializer,ListaMatriculasAlunoSerializer,ListaAlunosMatriculadosSerializer
# importar para a autenticação
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os alunos e alunas
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # Autenticando
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# viewsets.ModelViewSet Faz o crud

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Exibir todas as matriculas
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
# generics.ListAPIView Apenas lista
class ListaMatriculaAluno(generics.ListAPIView):
    """
    Listando as matriculas de um aluno(a)
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    """
    Listando alunos e alunas matriculados em um curso
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset 
    
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]