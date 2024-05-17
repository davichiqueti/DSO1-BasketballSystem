from controle.controlador_sistema import ControladorSistema
from controle.controlador_cursos import ControladorCursos
from controle.controlador_equipes import ControladorEquipes
from controle.controlador_partidas import ControladorPartidas


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
# Entidade $ENTIDADE
# controlador_$ENTIDADE = Controlador#ENTIDADES()
# controlador_sistema.controlador_$ENTIDADE = controlador_$ENTIDADE
# controlador_$ENTIDADE.controlador_sistema = controlador_sistema

# Execução do sistema
controlador_sistema.mostrar_opcoes()
