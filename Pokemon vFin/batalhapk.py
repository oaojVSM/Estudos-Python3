from pokemonCodeCademy import Pokemon
from pokemonCodeCademy import Trainer


def choose1pk(name, trainerpks):
    chosen1pk = str.title(
        (input(name + '! Choose your first pokemon:' + str(listpk_names) + ' this will be your active pokemon!')))
    try:
        listpk_names.remove(chosen1pk)
        for pk in listpk:
            if pk.name == chosen1pk:
                pokemon = pk
                listpk.remove(pk)
                trainerpks.append(pokemon)

    except:
        print('Please choose an available pokemon!')
        choose1pk(name, trainerpks)


def choosepk(name, trainerpks):
    chosenpk = str.title(input(name + '! Choose another pokemon:' + str(listpk_names)))
    try:
        listpk_names.remove(chosenpk)
        for pk in listpk:
            if pk.name == chosenpk:
                pokemon = pk
                listpk.remove(pk)
                trainerpks.append(pokemon)
    except:
        print('Please choose an available pokemon!')
        choosepk(name, trainerpks)


def round(turn):
    if turn % 2 == 0:
        attacker = trainer1
        receiver = trainer2
    else:
        attacker = trainer2
        receiver = trainer1
    if attacker.active_pk.ko == True:
        if attacker.active_pk != None:
            attacker.pk_list.remove(attacker.active_pk)
        chosen_pk = str.title(
            input(attacker.name + "! Your Pokemon was KOed, please select another one:" + str(attacker.pk_list)))
        try:
            for pk in attacker.pk_list:
                if chosen_pk == pk.name:
                    attacker.change_pk(pk)
                    round(turn)
        except:
            print('Please choose an available Pokemon')

    else:
        decision = str.title(
            input("{}, it's your turn, type 'Attack' to attack your opponents active pokemon, type 'Potion "
                  "to use a potion and heal your pokemon for 20hp, or 'Change' to change your active pokemon!"
                  "Your active Pokemon is {} with {}hp left.".
                  format(attacker.name, attacker.active_pk.name, attacker.active_pk.curr_hp)))
        try:
            if decision == 'Attack':
                attacker.attack(receiver)
            elif decision == 'Potion':
                if attacker.potions == 0:
                    print("You don't have any potions left!")
                    round(turn)
                attacker.use_potion(attacker.active_pk)
            elif decision == 'Change':
                chosen_pk_name = str.title(input('Which pokemon do you choose? You have:' + str(attacker.pk_list)))
                try:
                    for pk in attacker.pk_list:
                        if chosen_pk_name == pk.name:
                            attacker.change_pk(pk)
                except:
                    print('Please choose an available Pokemon')
                    round(turn)
            else:
                print('Please select an available action!')
                round(turn)
        except:
            print('Please select an available action!')
            round(turn)


def check_end_game():

    trainer1_pk_alive = 0
    trainer2_pk_alive = 0

    for pk in name1_pks:
        if pk.ko == False:
            trainer1_pk_alive += 1

    for pk in name2_pks:
        if pk.ko == False:
            trainer2_pk_alive += 1

    if trainer1_pk_alive == 0 or trainer2_pk_alive == 0:
        print('The game has ended. Congratulations, winner!')
        
    else:
        return False


giggy = Pokemon('Giggy', 10, 'grass', 100, 100)
bobly = Pokemon('Bobly', 10, 'fire', 100, 100)
junin = Pokemon('Junin', 10, 'water', 100, 100)
grubles = Pokemon('Grubles', 10, 'water', 100, 100)
charlander = Pokemon('Charlander', 10, 'fire', 100, 100)
jorizard = Pokemon('Jorizard', 10, 'grass', 100, 100)
listpk = [giggy, bobly, junin, grubles, charlander, jorizard]
listpk_names = [giggy.name, bobly.name, junin.name, grubles.name, charlander.name, jorizard.name]

print('Welcome to an amateur Python project by reddit user: u/_jvsm. This is a Pokemon simulator. And these are the available pokemon:')
for pk in listpk:
    print(pk)

name1 = input("Trainer 1, what is your name?")
name2 = input("Trainer 2, what is your name?")
name1_pks = []
name2_pks = []
choose1pk(name1, name1_pks)
choose1pk(name2, name2_pks)
choosepk(name1, name1_pks)
choosepk(name2, name2_pks)
choosepk(name1, name1_pks)
t2pk3 = listpk[0]
name2_pks.append(t2pk3)
print(name2 + ', you got the remaining pokemon: {}!'.format(str(t2pk3)))
print('Okay trainers, you have chosen your pokemon '
      'and you each have 3 potions. In each round, you can attack, use a potion '
      'or change your active pokemon')
trainer1 = Trainer(name1, name1_pks, 3, name1_pks[0])
trainer2 = Trainer(name2, name2_pks, 3, name2_pks[0])

turn = 1

while check_end_game() == False:

    if turn % 2 == 0:
        round(1)
        turn += 1
        check_end_game()

    else:
        round(2)
        turn += 1
        check_end_game()

check_end_game()

