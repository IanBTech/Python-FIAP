rm_alunos = {"563469": ["Giovanna", "2007"], "562227": ["Allana", "2004"]}
print(rm_alunos)

print(rm_alunos["563469"])

rm_alunos_back = rm_alunos.copy()
del rm_alunos["563469"]
print(rm_alunos)
print(rm_alunos_back)
rm_alunos["562227"][1] = "2003"
print(rm_alunos)

print("562227" in rm_alunos)
print("563469" in rm_alunos)

print(rm_alunos.keys())
print(rm_alunos.values())

