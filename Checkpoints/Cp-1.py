#Dupla: Ian Batinga Barbosa / Giovanna Carmona Roman Lopes

# O programa solicite as notas de cada semestre utilizando estruturas de repetição for.
# As notas sejam armazenadas em listas.
# Os valores informados sejam validados, aceitando apenas números entre 0 e 10.
# A menor nota de checkpoint seja descartada utilizando um laço for.
# A média final seja exibida com 1 casa decimal.

# Cálculo da média final (descarta menor CP; (2 CP + 2 Sprint)/4 = 40%; GS = 60%)

listanotas = []  # médias dos 2 semestres

for sem in range(2):
    cps, sp = [], []

    # ler 3 CPs (0..10)
    for n in range(3):
        while True:
            t = input(f"CP{n + 1} (0..10): ")
            a, p, d = (len(t) > 0), 0, 0
            if a:
                for ch in t:
                    if ch == '.':
                        p += 1
                    elif '0' <= ch <= '9':
                        d += 1
                    else:
                        a = False; break
            if a and p <= 1 and d >= 1 and t != '.':
                v = float(t)
                if 0 <= v <= 10: cps.append(v); break
            print("Inválido. Digite número entre 0 e 10 (use ponto).")

    # ler 2 Sprints (0..10)
    for n in range(2):
        while True:
            t = input(f"Sprint{n + 1} (0..10): ")
            a, p, d = (len(t) > 0), 0, 0
            if a:
                for ch in t:
                    if ch == '.':
                        p += 1
                    elif '0' <= ch <= '9':
                        d += 1
                    else:
                        a = False; break
            if a and p <= 1 and d >= 1 and t != '.':
                v = float(t)
                if 0 <= v <= 10: sp.append(v); break
            print("Inválido. Digite número entre 0 e 10 (use ponto).")

    # ler GS (0..10)
    while True:
        t = input("GS (0..10): ")
        a, p, d = (len(t) > 0), 0, 0
        if a:
            for ch in t:
                if ch == '.':
                    p += 1
                elif '0' <= ch <= '9':
                    d += 1
                else:
                    a = False; break
        if a and p <= 1 and d >= 1 and t != '.':
            gs = float(t)
            if 0 <= gs <= 10: break
        print("Inválido. Digite número entre 0 e 10 (use ponto).")

    # descartar menor CP usando for
    min_i = 0
    for i in range(1, len(cps)):
        if cps[i] < cps[min_i]: min_i = i

    cp2 = []
    for i in range(len(cps)):
        if i != min_i: cp2.append(cps[i])

    m4 = (cp2[0] + cp2[1] + sp[0] + sp[1]) / 4
    listanotas.append(m4 * 0.4 + gs * 0.6)

final = listanotas[0] * 0.4 + listanotas[1] * 0.6
print(f"\nMÉDIA FINAL: {final:.1f}")


