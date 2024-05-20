from tela.tela_base import TelaBase


class TelaCampeonatos(TelaBase):
    def __init__(self):
        super(). __init__()

    def tela_opcoes(self):
        self.limpar_tela()
        print("--------Campeonatos--------")
        print("Escolha uma opção:")
        print("1 - Incluir campeonatos")
        print("2 - Incluir partidas em um campeonato")
        print("3 - Alterar campeonatos")
        print("4 - Excluir campeonatos")
        print("5 - Listar campeonatos")
        print("6 - Exibir relatórios de campeonatos")
        print("10 - Retornar")

        opcao = int(input("Escolha uma opcao: "))
        return opcao


    def incluir_campeonato(self):
        print("--------Inclusão de Campeonatos--------")
        while True:
            codigo_campeonato = input("Insira o codigo do Campeonato: ")
            if codigo_campeonato.isnumeric():
                codigo_campeonato = int(codigo_campeonato)
                break
            else:    
                print("Código inválido, por favor informe um código válido")
                input("Aperte ENTER para continuar.")

        while True:
            descricao_campeonato = input("Insira a descrição do Campeonato: ")
            if descricao_campeonato.isspace():
                self.mostrar_mensagem('Descrição inválida. Descrição inserida é vazia')
            if len(descricao_campeonato) < 10:
                self.mostrar_mensagem('Descrição inválida. Descrição deve ter mais de 10 caracteres')
            else:
                break
        equipes = list()
        #equipes
        while True:
            codigo_equipe = input("insira o codigo da equipe para inclusão no Cammpeonato:")
            if codigo_equipe.isnumeric():
                codigo_equipe = int(codigo_equipe)
                equipes.append(codigo_equipe)

            if not self.confirmar_acao("Deseja cadastrar mais uma equipe no campeonato?") and len(equipes) >= 2:
                break
            
            else:
                print("É necessário pelo menos 2 equipes para incluir um campeonato.")
                return self.tela_opcoes()
        
        dict_incluir_campeonato = {
            "codigo_campeonato" : codigo_campeonato,
            "lista_equipes" : equipes,
            "descricao": descricao_campeonato
        }

        return dict_incluir_campeonato



    def incluir_partida_campeonato(self):

        #verifica qual opcao o usuario quer
        print("--------Inclusão de Partidas no Campeonato--------")
        print("É necessário ter ao menos uma partida cadastrada para utilizar esse módulo.")
        print("Deseja Cadastrar uma partida ou informar o código de uma partida existente?")
        print("1 - Cadastrar partida")
        print("2 - Incluir uma partida já existente")
        print("10 - Sair")
        retorno = int(input("Escolha uma opção: "))

        #tratamento para cada opcao
        while True:
            if retorno == 10:
                break

            if retorno == 2:
                self.limpar_tela()
                print("--------Incluir Partida no Campeonato--------")
                dict_retorno = []
                while True:
                    codigo_campeonato = input("Insira o codigo do Campeonato: ")
                    if codigo_campeonato.isnumeric():
                        codigo_campeonato = int(codigo_campeonato)
                        break
                    else:    
                        print("Código inválido, por favor informe um código válido")
                        input("Aperte ENTER para continuar.")

                while True:
                    codigo_partida = input("Insira o código da partida: ")
                    if codigo_partida.isnumeric():
                        codigo_partida = int(codigo_partida)
                        break
                    else:    
                        print("Código inválido, por favor informe um código válido")
                        input("Aperte ENTER para continuar.")
                
                dict_retorno = {
                    "codigo_campeonato" : codigo_campeonato,
                    "codigo_partida" : codigo_partida
                }
                return dict_retorno

            elif retorno == 1:
                dict_retorno = {
                    "codigo_campeonato" : 'incluir'
                }
                return dict_retorno

            else:    
                print("Código inválido, por favor informe um código válido")
                input("Aperte ENTER para continuar.")


        

    def alterar_campeonato(self):
        print("--------Alteração Campeonato--------")
        while True:
            codigo_campeonato_alteracao = input("Insira o codigo do Campeonato: ")
            if codigo_campeonato.isnumeric():
                codigo_campeonato = int(codigo_campeonato)
                break
            else:    
                print("Código inválido, por favor informe um código válido")
                input("Aperte ENTER para continuar.")

        while True:
            codigo_campeonato_novo = input("Insira o codigo do Campeonato: ")
            if codigo_campeonato.isnumeric():
                codigo_campeonato = int(codigo_campeonato)
                break
            else:    
                print("Código inválido, por favor informe um código válido")
                input("Aperte ENTER para continuar.")

        codigos_alteracoes_equipes = list()
        while True:
            codigos = input("insira o codigo da equipe do Cammpeonato:")
            if codigos.isnumeric():
                codigos = int(codigos)
                codigos_alteracoes_equipes.append(codigos)
                self.confirmar_acao("Deseja inserir mais um código de equipe?")
                if not self.confirmar_acao:
                    break
            
        
        dict_alterar_campeonato = {
            "codigo_campeonato" : codigo_campeonato,
            "codigos_alteracoes_equipes" : codigos_alteracoes_equipes
        }

        return dict_alterar_campeonato
    
    def excluir_campeonato(self):
        print("--------Exclusão de Campeonato--------")
        while True:
            codigo_campeonato_exclusao = input("Insira o codigo para exclusão do Campeonato: ")
            if codigo_campeonato_exclusao.isnumeric():
                codigo_campeonato_exclusao = int(codigo_campeonato_exclusao)
                break
            else:    
                print("Código inválido, por favor informe um código válido")
                input("Aperte ENTER para continuar.")
                return self.alterar_campeonato()

        return codigo_campeonato_exclusao

    def listar_campeonatos(self, dados_campeonatos):
        self.limpar_tela()
        print('-------- Listagem de Campeonatos --------')
        for campeonato in dados_campeonatos:
            campeonato_selecionado = campeonato
            codigo = dados_campeonatos["codigo_campeonato"]
            print(f"Campeonato: {campeonato_selecionado.nome}, {campeonato_selecionado.codigo}")
            print()
            for equipe in campeonato_selecionado.equipe:
                equipe_selecionada = equipe
                print(f"Equipe: {equipe_selecionada.nome}, {equipe_selecionada.codigo}")
                print()
        self.esperar_resposta()

    def selecionar_campeonato(self, dados_campeonatos: list[dict]) -> int:
        print('Selecione um dos campeonatos abaixo')
        codigos = set()
        for campeonato in self.dados_campeonatos:
            print(f'- {campeonato["nome"]} (Código {campeonato["codigo"]})')
            codigos.add(campeonato['codigo'])
        codigo = input('\nDigite o código do campeonato selecionado: ').strip()
        if not codigo.isnumeric():
            self.mostrar_mensagem('O código inserido não é númerico. Tente novamente')
            return self.selecionar_campeonato(dados_campeonatos)
        elif int(codigo) not in codigos:
            self.mostrar_mensagem('O código inserido não pertence a nenhum dos campeonatos listados')
            return self.selecionar_campeonato(dados_campeonatos)
        else:
            return int(codigo)

    def exibir_relatorios_campeonato(self, dados_relatorios: dict):
        self.limpar_tela()
        print('--- RELÁTORIOS CAMPEONATO ---\n')
        print(f'Campeonato {dados_relatorios["descricao_campeonato"]}')
        # Exibindo as posições de cada equipe no campeonato
        print("Pódio do campeonato:")
        for i in range(len(dados_relatorios['podio'])):
            equipe = dados_relatorios['podio'][i]
            print(f'\t - {i}° Lugar: {equipe["nome"]}({equipe["codigo"]}) {equipe["pontos"]} Pontos')
        self.esperar_resposta()
        print('\nEquipes que mais marcaram pontos:')
        for i in range(len(dados_relatorios['equipes_mais_pontos'])):
            equipe = dados_relatorios['equipes_mais_pontos'][i]
            print(f'\t - {i}° Lugar: {equipe["nome"]}({equipe["codigo"]}) {equipe["pontos"]} Pontos')
        self.esperar_resposta()
        print('\nJogadores que mais marcaram pontos:')
        for i in range(len(dados_relatorios['alunos_mais_pontos'])):
            jogador = dados_relatorios['alunos_mais_pontos'][i]
            print(f'\t - {i}° Lugar: {jogador["nome"]}({jogador["codigo"]}) {jogador["pontos"]} Pontos')
        self.mostrar_mensagem('Fim dos relátorios')
