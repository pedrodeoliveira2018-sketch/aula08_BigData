# numeros = [ 8,15,25,37,9,3]

# numeros.append(5)
# print (numeros)

# print(sum(numeros))
# print(max(numeros))
# print(min(numeros))
# print(len(numeros))
# print(f'numeros : {numeros}')


Alunos = []

for n in range(5) :
    print(f'\n ------ Aluno{n+1}-----')
    nome= input('informe o nome do aluno : ')
    notas = []
    for i  in range(5):
        nota = float(input(f'informe a nota {i + 1} :'))
        notas.append(nota)
    media= sum(notas) / len (notas)

    print(media)

    Aluno = {
        'Nome' : nome,
        'Notas': notas,
        'Media' : media
    }

    Alunos.append(Aluno)

# exibindo os dados 
    
for estudante in Alunos :
    print(f'Nome: {estudante["Nome"]}')
    print(f'Notas: {estudante["Notas"]}')
    print(f'media: {estudante["Media"]}')