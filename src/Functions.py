import pandas as pd

df = pd.read_csv("SongsList.csv")

def err():
    return "Invalid choice!"

def exit():
    return "\nbye bye...\n"

def title():
    title = input("\nDigite o titulo: ")
    return titleSearch(title)

def titleSearch(title):
    df2=df[df["Title"] == title]    
    return df2

def artist():
    artist = input("\nDigite o nome do artista: ")
    return artistSearch(artist)

def artistSearch(artist):
    df2=df[df["Artist"] == artist]    
    return df2

def genre():
    genre = input("\nDigite o gênero da música: ")
    return genreSearch(genre) 

def genreSearch(genre):
    df2=df[df["Genre"] == genre]    
    return df2

def listAll():
    return df