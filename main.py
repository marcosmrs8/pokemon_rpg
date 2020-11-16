import pickle

from pokemon import *

from pessoa import *


def escolher_pokemon_inicial(player):
    print('olá {} você deve escolher seu primeiro pokemon!'.format(player))

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 opções: ')
    print('1-', pikachu)
    print('2-', charmander)
    print('3-', squirtle)

    while True:
        escolha = input("Escolha o seu Pokemon: ")

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha invalida')


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('Jogo salvo!')
    except Exception as error:
        print('Eita, deu um erro:', error)


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('loadin feito com sucesso')
            return player
    except Exception as error:
        print('Save não encontrado')


if __name__ == "__main__":
    print('--------------------------')
    print('Bem vindo ao Pokemon RPG de terminal!')
    print('--------------------------')

    player = carregar_jogo()

    if not player:

        nome = input('Olá, qual é o seu nome?')
        player = Player(nome)
        print('Ola {}, esse é um mundo habitado por pokemons,boa aventura!'.format(nome))
        player.mostrar_pokemon()

        if player.pokemons:
            print('Já vi que possui pokemons')
            player.mostrar_pokemon()
        else:
            print('Você não tem pokemon, você precisa escolher 1')
            escolher_pokemon_inicial(player)

        print('Agora que já possui seu primeiro pokemon, batalhe contra Gary!!!')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])

        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print('--------------------------')
        print('1 - Explorar pelo mundo')
        print('2 - lutar com inimigo')
        print('3 - Ver PokeAgenda')
        print('0 - sair do jogo')
        escolha = input('O que deseja fazer?')

        if escolha == '0':
            print('fechando o jogo...')
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemon()
        else:
            print('Escolha invalida')