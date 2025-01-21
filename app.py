import os

fandoms = [
    "Arianators",
    "ARMY",
    "Beliebers",
    "BeyHive",
    "Blinks",
    "Camilizers",
    "Directioners",
    "Harries",
    "Lanatics",
    "Little Monsters",
    "Lovatics",
    "Mendes Army",
    "Selenators",
    "Swifties",
    "XO Crew"
]

usuarios = []

eventos = []

fandoms_analise = []

def exibir_nome_programa():
    print(
        """
        █▀▀ ▄▀█ █▄░█ █▀▀ ▄▀█ █▀▄
        █▀░ █▀█ █░▀█ █▄▄ █▀█ █▄▀
        """)
    print('Para todos os fãs de carteirinha​​​​​!\n')

def voltar_ao_menu_principal():
    input('Digite uma tecla para retornar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'* {texto} *')
    print(linha)
    print()

def exibir_opcoes():
    print('[1] Solicitar carteirinha')
    print('[2] Editar cadastro')
    print('[3] Adicionar evento')
    print('[4] Solicitar novo fã clube')
    print('[5] Sair')

def escolher_fa_clube():
    busca = input("Digite o nome de um fandom: ").strip()

    if busca in fandoms:
        print(f"Fandom '{busca}' encontrado!")
        return busca
    else:
        print(f"Fandom '{busca}' não encontrado.")
        return None

def solicitar_carteirinha():
    exibir_subtitulo('Faça seu cadastro gratuitamente!')

    nome_usuario = input('Digite seu nome: ')
    data_nascimento_usuario = input('Digite sua data de nascimento (dd/mm/aa): ')
    genero_usuario = input('Digite seu gênero: ')

    while True:
        fandom_selecionado = escolher_fa_clube()

        if fandom_selecionado:
            dados_usuario = { 
                'nome': nome_usuario, 
                'data de nascimento': data_nascimento_usuario, 
                'genero': genero_usuario,
                'fandom': fandom_selecionado 
            }
            usuarios.append(dados_usuario)
            print('Carteirinha cadastrada com sucesso!')
            voltar_ao_menu_principal()
            break
        else:
            print('Cadastro não concluído, tente novamente.')

def editar_cadastro():
    nome_usuario = input('Digite o nome de usuário que deseja editar: ').strip()
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['nome'].lower() == nome_usuario.lower():  # Compara sem diferenciar maiúsculas/minúsculas
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        print(f"\nCadastro de {nome_usuario} encontrado.")
        
        # Permite editar os dados
        novo_nome = input(f"Novo nome (atualmente {usuario_encontrado['nome']}): ").strip()
        if novo_nome:
            usuario_encontrado['nome'] = novo_nome
        
        nova_data_nascimento = input(f"Nova data de nascimento (atualmente {usuario_encontrado['data de nascimento']}): ").strip()
        if nova_data_nascimento:
            usuario_encontrado['data de nascimento'] = nova_data_nascimento
        
        novo_genero = input(f"Novo gênero (atualmente {usuario_encontrado['genero']}): ").strip()
        if novo_genero:
            usuario_encontrado['genero'] = novo_genero
        
        novo_fandom = input(f"Novo fandom (atualmente {usuario_encontrado['fandom']}): ").strip()
        if novo_fandom in fandoms:
            usuario_encontrado['fandom'] = novo_fandom
        else:
            print("Fandom não encontrado. O campo será mantido com o valor atual.")

        print('Cadastro atualizado com sucesso!')
        voltar_ao_menu_principal()
    else:
        print(f"Usuário {nome_usuario} não encontrado.")

def adicionar_evento():
    evento = input('Qual o nome do evento? ')
    data_evento = input('Qual será a data do evento? ')
    local_evento = input('Qual será o local do evento? ')

    evento_cadastrado = {
        'nome': evento,
        'data': data_evento,
        'local': local_evento
    }
    eventos.append(evento_cadastrado)

    print('Evento cadastrado com sucesso!')
    voltar_ao_menu_principal()

def solicitar_novo_fa_clube():
    novo_fanclub = input('Qual fandom deseja solicitar? ')

    if novo_fanclub in fandoms:
        print(f'O fandom "{novo_fanclub}" já está registrado.')
    else:
        solicitacao_fandom = {
            'nome': novo_fanclub
        }
        fandoms_analise.append(solicitacao_fandom)
        print('Sua solicitação foi registrada com sucesso! Aguarde pela análise do FANCAD.')
    
    voltar_ao_menu_principal()

def encerrar_app():
    print('Encerrando o app.')

def opcao_invalida():
    print('Opcao inválida!\n')
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('O que gostaria de fazer hoje?'))

        if opcao_escolhida == 1:
            solicitar_carteirinha()
        elif opcao_escolhida == 2:
            editar_cadastro()
        elif opcao_escolhida == 3:
            adicionar_evento()
        elif opcao_escolhida == 4:
            solicitar_novo_fa_clube()
        elif opcao_escolhida == 5:
            encerrar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()