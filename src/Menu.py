from Functions import*

print('''
==================
Welcome to My List
==================
''')

choice = 1

while choice != 0 :
    print('''
    1. Buscar por título
    2. Buscar por Artista
    3. Buscar por Gênero
    4. Listar todas as músicas
    0. Sair
    ''')

    choice = int(input("Digite a opção desejada: "))
    op = {
        1: title,
        2: artist,
        3: genre,
        4: listAll,
        0: exit
    }

    output = op.get(choice, err)()
    print(output)

