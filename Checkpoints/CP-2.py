# Dupla: Ian Batinga Barbosa / Giovanna Carmona Roman Lopes
# Programa que cadastra alunos, valida notas de cada semestre,
# descarta a menor nota de checkpoint e calcula a média final
# Fórmula: (2 CP + 2 Sprint)/4 = 40% + GS = 60%

alunos = []  # lista de alunos cadastrados

while True:
    print("\n--- Cadastro de Aluno ---")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")
    turno = input("Turno: ")
    turma = input("Turma: ")

    medias_semestres = []  # armazenará as médias dos dois semestres

    for semestre in range(1, 3):  # 2 semestres
        print(f"\n--- SEMESTRE {semestre} ---")
        checkpoints = []
        sprints = []

        # Ler 3 CPs (0..10)
        for numero_cp in range(3):
            while True:
                entrada_usuario = input(f"CP{numero_cp + 1} (0..10): ")
                entrada_valida, pontos, digitos = (len(entrada_usuario) > 0), 0, 0

                if entrada_valida:
                    for caractere in entrada_usuario:
                        if caractere == '.':
                            pontos += 1
                        elif '0' <= caractere <= '9':
                            digitos += 1
                        else:
                            entrada_valida = False
                            break

                if entrada_valida and pontos <= 1 and digitos >= 1 and entrada_usuario != '.':
                    valor_nota = float(entrada_usuario)
                    if 0 <= valor_nota <= 10:
                        checkpoints.append(valor_nota)
                        break
                print("Inválido. Digite número entre 0 e 10 (use ponto).")

        # Ler 2 Sprints (0..10)
        for numero_sprint in range(2):
            while True:
                entrada_usuario = input(f"Sprint{numero_sprint + 1} (0..10): ")
                entrada_valida, pontos, digitos = (len(entrada_usuario) > 0), 0, 0

                if entrada_valida:
                    for caractere in entrada_usuario:
                        if caractere == '.':
                            pontos += 1
                        elif '0' <= caractere <= '9':
                            digitos += 1
                        else:
                            entrada_valida = False
                            break

                if entrada_valida and pontos <= 1 and digitos >= 1 and entrada_usuario != '.':
                    valor_nota = float(entrada_usuario)
                    if 0 <= valor_nota <= 10:
                        sprints.append(valor_nota)
                        break
                print("Inválido. Digite número entre 0 e 10 (use ponto).")

        # Ler GS (0..10)
        while True:
            entrada_usuario = input("GS (0..10): ")
            entrada_valida, pontos, digitos = (len(entrada_usuario) > 0), 0, 0

            if entrada_valida:
                for caractere in entrada_usuario:
                    if caractere == '.':
                        pontos += 1
                    elif '0' <= caractere <= '9':
                        digitos += 1
                    else:
                        entrada_valida = False
                        break

            if entrada_valida and pontos <= 1 and digitos >= 1 and entrada_usuario != '.':
                gs = float(entrada_usuario)
                if 0 <= gs <= 10:
                    break
            print("Inválido. Digite número entre 0 e 10 (use ponto).")

        # Descarta a menor nota de checkpoint
        indice_menor_cp = 0
        for i in range(1, len(checkpoints)):
            if checkpoints[i] < checkpoints[indice_menor_cp]:
                indice_menor_cp = i

        checkpoints_validos = []
        for i in range(len(checkpoints)):
            if i != indice_menor_cp:
                checkpoints_validos.append(checkpoints[i])

        # Calcula média do semestre (40% CP+Sprint + 60% GS)
        media_40 = (checkpoints_validos[0] + checkpoints_validos[1] + sprints[0] + sprints[1]) / 4
        medias_semestres.append(media_40 * 0.4 + gs * 0.6)

    # Cálculo da média final do aluno
    media_final = medias_semestres[0] * 0.4 + medias_semestres[1] * 0.6

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "curso": curso,
        "turno": turno,
        "turma": turma,
        "medias_semestres": medias_semestres,
        "media_final": media_final
    }
    alunos.append(aluno)

    # Pergunta se deseja continuar
    continuar = input("\nCadastrar outro aluno? (s/n): ").lower()
    if continuar != "s":
        break

# Menu de edição de alunos
while True:
    print("\n--- MENU DE EDIÇÃO ---")
    print("1 - Alterar aluno")
    print("2 - Excluir aluno")
    print("3 - Finalizar e mostrar relatório")
    opcao = input("Escolha: ")

    if opcao == "1":
        matricula_busca = input("Digite a matrícula do aluno que deseja alterar: ")
        encontrado = False
        for a in alunos:
            if a["matricula"] == matricula_busca:
                encontrado = True
                print(f"Editando aluno: {a['nome']}")
                a["nome"] = input(f"Novo nome ({a['nome']}): ") or a["nome"]
                a["curso"] = input(f"Novo curso ({a['curso']}): ") or a["curso"]
                a["turno"] = input(f"Novo turno ({a['turno']}): ") or a["turno"]
                a["turma"] = input(f"Nova turma ({a['turma']}): ") or a["turma"]
                print("Dados alterados com sucesso!")
                break
        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "2":
        matricula_busca = input("Digite a matrícula do aluno que deseja excluir: ")
        for i, a in enumerate(alunos):
            if a["matricula"] == matricula_busca:
                print(f"Aluno {a['nome']} removido.")
                alunos.pop(i)
                break
        else:
            print("Aluno não encontrado.")

    elif opcao == "3":
        break
    else:
        print("Opção inválida.")

# Exibe relatório final
print("\n--- RELATÓRIO DE ALUNOS ---")
for a in alunos:
    print(f"Nome: {a['nome']} | Matrícula: {a['matricula']} | Curso: {a['curso']} | Turno: {a['turno']} | Turma: {a['turma']}")
    print(f"Médias: Sem1={a['medias_semestres'][0]:.1f} | Sem2={a['medias_semestres'][1]:.1f}")
    print(f"MÉDIA FINAL: {a['media_final']:.1f}")
    print("-" * 40)