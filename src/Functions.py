import pandas as pd

df = pd.read_csv("SongsList.csv")

def err():
    return "Invalid choice!"

def exit():
    return "\nbye bye...\n"

def title():
    title = input("\nDigite o titulo: ")
    df2=df[df["Title"] == title] 
    return df2

def artist():
    artist = input("\nDigite o nome do artista: ")
    df2=df[df["Artist"] == artist] 
    return df2

def genre():
    genre = input("\nDigite o gênero da música: ")
    df2=df[df["Genre"] == genre]  
    return df2

def listAll():
    return pd.read_csv('SongsList.csv')

def register():
    title = input("\nDigite o título da música: ")
    artist = input("Digite o artista da música: ")
    album = input("Digite o album da música: ")
    release = input("Digite o ano da música: ")
    genre = input("Digite o gênero da música: ")
    newsong = df.append({'Title':title,'Artist':artist,'Album':album,'Release':release,'Genre':genre}, ignore_index=True)
    newsong.to_csv('SongsList.csv', index=False)
    return "\nMúsica cadastrada com sucesso!"
