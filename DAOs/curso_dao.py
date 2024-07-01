from DAOs.dao import DAO
from entidade.curso import Curso

class CursoDAO(DAO):
    def __init__(self):
        super().__init__('curso.pkl')

    def add(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.codigo, int)): 
            super().add(curso.codigo, curso)

    def update(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.codigo, int)):
            super().update(curso.codigo, curso)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
