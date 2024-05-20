from controle.controlador_sistema import ControladorSistema
from controle.controlador_cursos import ControladorCursos
from controle.controlador_equipes import ControladorEquipes
from controle.controlador_partidas import ControladorPartidas
from controle.controlador_arbitros import ControladorArbitros
from controle.controlador_alunos import ControladorAlunos
from controle.controlador_campeonatos import ControladorCampeonatos

from entidade.curso import Curso
from entidade.aluno import Aluno
from entidade.arbitro import Arbitro
from entidade.campeonato import Campeonato
from entidade.equipe import Equipe
from entidade.partida import Partida
from entidade.campeonato import Campeonato

from datetime import datetime


controlador_sistema = ControladorSistema()
# Criando controladores de modelos e relacionando-os com o controlador de sistema
# Entidade Curso
controlador_cursos = ControladorCursos()
controlador_sistema.controlador_cursos = controlador_cursos
controlador_cursos.controlador_sistema = controlador_sistema

objetos = [
    Curso(1, 'SISTEMAS DE INFORMAÇÃO'),
    Curso(2, 'ADMINISTRAÇÃO'),
    Curso(3, 'JORNALISMO'),
]
for objeto in objetos:
    controlador_cursos.cursos.append(objeto)

# Entidade Arbitro
controlador_arbitros = ControladorArbitros()
controlador_sistema.controlador_arbitros = controlador_arbitros
controlador_arbitros.controlador_sistema = controlador_sistema
objetos = [
    Arbitro('Roger', '12345678910', datetime(2000, 1, 1), 'SC', 'Florianópolis', 'ingleses', 0),
    Arbitro('João', '12345678900', datetime(2002, 1, 2), 'SP', 'São Paulo', 'Centro', 12),
    Arbitro('Gabriel', '36019045698', datetime(1999, 4, 6), 'RS', 'Porto Alegre', 'Anchieta', 8),
]
for objeto in objetos:
    controlador_arbitros.arbitros.append(objeto)

#Entidade Aluno
controlador_alunos = ControladorAlunos()
controlador_sistema.controlador_alunos = controlador_alunos
controlador_alunos.controlador_sistema = controlador_sistema
objetos = [
    Aluno('Davi', '12345678910', datetime(2000, 1, 1), 'SC', 'Florianópolis', 'Trindade', '23202061', controlador_cursos.cursos[0]),
    Aluno('Arthur', '12345678919', datetime(2000, 2, 8), 'SC', 'Florianópolis', 'Trindade', '23202062', controlador_cursos.cursos[0]),
    Aluno('Xyleine', '12300012300', datetime(2000, 5, 1), 'SC', 'Florianópolis', 'Trindade', '23202090', controlador_cursos.cursos[0]),
    Aluno('Jonlayne', '12300012300', datetime(2000, 1, 1), 'SC', 'Florianópolis', 'Trindade', '23202091', controlador_cursos.cursos[0]),
    Aluno('Paulinho', '12300012302', datetime(2001, 4, 1), 'SC', 'Florianópolis', 'Trindade', '23202092', controlador_cursos.cursos[0]),
    Aluno('Jubiscreia', '12312312310', datetime(2000, 1, 1), 'SC', 'Florianópolis', 'ingleses', '23202060', controlador_cursos.cursos[1]),
    Aluno('Gestor', '98700098700', datetime(2002, 1, 1), 'SC', 'Florianópolis', 'Lagoa', '99009900', controlador_cursos.cursos[1]),
    Aluno('Administrador', '45645645612', datetime(2003, 1, 1), 'SC', 'Florianópolis', 'Lagoa', '09109112', controlador_cursos.cursos[1]),
    Aluno('Pedro', '12398745612', datetime(2004, 12, 1), 'SC', 'Florianópolis', 'Lagoa', '09109009', controlador_cursos.cursos[1]),
    Aluno('Roger', '09309311122', datetime(2003, 1, 12), 'SC', 'Florianópolis', 'Lagoa', '09109111', controlador_cursos.cursos[1]),
    Aluno('Ronaldo', '89074562392', datetime(2002, 5, 2), 'PR', 'Curitiba', 'Centro', '12345678', controlador_cursos.cursos[2]),
    Aluno('Cleiton', '12312312311', datetime(2004, 5, 7), 'PR', 'Curitiba', 'Centro', '12345670', controlador_cursos.cursos[2]),
    Aluno('Cleiton II', '12312312312', datetime(2004, 5, 1), 'PR', 'Curitiba', 'Centro', '12345679', controlador_cursos.cursos[2]),
    Aluno('William Bonnet Jr', '01201201299', datetime(2004, 5, 1), 'PR', 'Cidade Xpto', 'Bairro dos bobos', '09123121', controlador_cursos.cursos[2]),
    Aluno('Regiscraldo', '98765432112', datetime(2005, 5, 1), 'PA', 'Napolitano', 'Centro', '12121212', controlador_cursos.cursos[2])
]
for objeto in objetos:
    controlador_alunos.alunos.append(objeto)

# Entidade Equipe
controlador_equipes = ControladorEquipes()
controlador_sistema.controlador_equipes = controlador_equipes
controlador_equipes.controlador_sistema = controlador_sistema
objetos = [
    Equipe('A5', controlador_cursos.cursos[0], 1, alunos=controlador_alunos.alunos[:5]),
    Equipe('ADM Monsters', controlador_cursos.cursos[1], 2,alunos=controlador_alunos.alunos[5:10]),
    Equipe('Reporters do Caos', controlador_cursos.cursos[2], 3,alunos=controlador_alunos.alunos[10:])
]
for objeto in objetos:
    controlador_equipes.equipes.append(objeto)

# Entidade Partida
controlador_partidas = ControladorPartidas()
controlador_sistema.controlador_partidas = controlador_partidas
controlador_partidas.controlador_sistema = controlador_sistema


#Entidade Campeonato
controlador_campeonatos = ControladorCampeonatos()
controlador_sistema.controlador_campeonatos = controlador_campeonatos
controlador_campeonatos.controlador_sistema = controlador_sistema


# Entidade $ENTIDADE
# controlador_$ENTIDADE = Controlador#ENTIDADES()
# controlador_sistema.controlador_$ENTIDADE = controlador_$ENTIDADE
# controlador_$ENTIDADE.controlador_sistema = controlador_sistema

# Execução do sistema
controlador_sistema.mostrar_opcoes()