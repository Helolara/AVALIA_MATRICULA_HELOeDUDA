import os

alunos = []
turnos = []
cursos = [{"Medicina"}, 
        {"Fisioterapia"}, 
        {"Educação Física"},
        {"Análise de Sistemas"}]; 

def mostrar_subtitulo(texto):
    """Exibe um subtítulo formatado."""
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    """Finaliza o aplicativo."""
    mostrar_subtitulo('Saindo do aplicativo.')
    exit()

def chamar_nome_do_app():
    """Exibe o nome do aplicativo."""
    print('''
    𝑀𝑎𝑡𝑟𝑖𝑐𝑢𝑙𝑎 𝑜𝑛𝑙𝑖𝑛𝑒 
    ''')

def voltar_ao_menu_principal():
    """Retorna ao menu principal após uma pausa."""
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    """Exibe uma mensagem para opções inválidas e volta ao menu principal."""
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_opcoes():
    """Exibe as opções disponíveis no menu principal."""
    print("1. Cadastrar Aluno")
    print("2. Cadastrar Curso")
    print("3. Cadastrar Turno")
    print("4. Listar Matrículas")
    print("5. Sair\n") 

def cadastrar_aluno():
    """Cadastra um novo aluno."""
    os.system('cls')
    nome_aluno = input('Digite o nome do aluno: ')
    matricula = input('Digite o número da matrícula do aluno: ')
    aluno = {'nome': nome_aluno, 'matricula': matricula, 'cursos': []}
    alunos.append(aluno)
    print(f'O aluno {nome_aluno} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def cadastrar_curso():
    """Cadastra um novo curso."""
    os.system('cls')
    nome_curso = input('Digite o nome do curso (Medicina, Fisioterapia, Educação Física, Análise de Sistemas): ')
    ativo = True
    curso = {'nome': nome_curso, 'ativo': ativo}
    cursos.append(curso)
    print(f'O curso {nome_curso} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def cadastrar_turno():
    """Cadastra um novo turno."""
    os.system('cls')
    turno = input('Digite o turno (Matutino, Vespertino, Noturno): ')
    turnos.append(turno)
    print(f'O turno {turno} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_matriculas():
    """Lista todos os alunos e seus cursos associados."""
    mostrar_subtitulo('Listando Matrículas')
    print(f'Nome do Aluno'.ljust(24), 'Matrícula'.ljust(15), 'Cursos')
    for aluno in alunos:
        cursos_aluno = ', '.join(aluno['cursos']) if aluno['cursos'] else 'Nenhum'
        print(f'{aluno["nome"].ljust(24)} {aluno["matricula"].ljust(15)} {cursos_aluno}')
    voltar_ao_menu_principal()

def escolher_opcao():
    """Escolhe a opção selecionada pelo usuário."""
    try:
        opcao_digitada = int(input("Escolha uma opção: "))
        print(f"Você selecionou: {opcao_digitada}\n")
        if opcao_digitada == 1:
            cadastrar_aluno()
        elif opcao_digitada == 2:
            cadastrar_curso()
        elif opcao_digitada == 3:
            cadastrar_turno()
        elif opcao_digitada == 4:
            listar_matriculas()
        elif opcao_digitada == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    """Função principal que exibe o menu e gerencia as opções."""
    os.system('cls')
    chamar_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
