from controle.controlador_sistema import ControladorSistema
from controle.controlador_cursos import ControladorCursos
from controle.controlador_equipes import ControladorEquipes
from controle.controlador_partidas import ControladorPartidas
from controle.controlador_arbitros import ControladorArbitros
from controle.controlador_alunos import ControladorAlunos
from controle.controlador_campeonatos import ControladorCampeonatos


controlador_sistema = ControladorSistema()
# Criando controladores de modelos e relacionando-os com o controlador de sistema
# Entidade Curso
controlador_cursos = ControladorCursos()
controlador_sistema.controlador_cursos = controlador_cursos
controlador_cursos.controlador_sistema = controlador_sistema

# Entidade Equipe
controlador_equipes = ControladorEquipes()
controlador_sistema.controlador_equipes = controlador_equipes
controlador_equipes.controlador_sistema = controlador_sistema

# Entidade Partida
controlador_partidas = ControladorPartidas()
controlador_sistema.controlador_partidas = controlador_partidas
controlador_partidas.controlador_sistema = controlador_sistema

# Entidade Arbitro
controlador_arbitros = ControladorArbitros()
controlador_sistema.controlador_arbitros = controlador_arbitros
controlador_arbitros.controlador_sistema = controlador_sistema

#Entidade Aluno
controlador_alunos = ControladorAlunos()
controlador_sistema.controlador_alunos = controlador_alunos
controlador_alunos.controlador_sistema = controlador_sistema

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
