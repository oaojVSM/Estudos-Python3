class Pokemon:
    def __init__(self, name, level, type, max_hp, curr_hp, ko=False):
        self.name = name
        self.level = level
        self.type = type  # water, fire or grass
        self.max_hp = max_hp
        self.curr_hp = curr_hp
        self.ko = ko

    def lose_hp(self, points):
        self.curr_h = self.curr_h - points
        print('{} has lost {} and now has {} HP left!'.format(self.name, points, self.curr_hp))

    def gain_hp(self, points):
        self.curr_hp = self.curr_hp + points
        if self.curr_hp > self.max_hp:
            self.curr_hp = self.max_hp
        print('{} has gained {} and now has {} HP!'.format(self.name, points, self.curr_hp))

    def attack(self, receiver):
        attack_points = 0
        if self.type == receiver.type:
            attack_points = self.level
        if self.type == 'fire' and receiver.type == 'grass':
            attack_points = self.level * 2
        if self.type == 'fire' and receiver.type == 'water':
            attack_points = self.level / 2
        if self.type == 'water' and receiver.type == 'fire':
            attack_points = self.level * 2
        if self.type == 'water' and receiver.type == 'grass':
            attack_points = self.level / 2
        if self.type == 'grass' and receiver.type == 'water':
            attack_points = self.level * 2
        if self.type == 'grass' and receiver.type == 'fire':
            attack_points = self.level / 2
        receiver.curr_hp -= attack_points
        if receiver.curr_hp > 0:
            print('{attacker} just attacked {receiver} for {points} points and left him with {remaining_health}HP left!'.format(
            attacker = self.name, receiver = receiver.name, points = attack_points, remaining_health = receiver.curr_hp
            ))
        if receiver.curr_hp <= 0:
            receiver.curr_hp = 0
            receiver.ko=True
            print('{} has KOed {}!'.format(self.name, receiver.name))
    def __repr__(self):
        return '{} is a {} pokemon!'.format(self.name, self.type)

#charmander = Pokemon('Charmander', 10, 'fire', 100, 100)
#bulbasaur = Pokemon('Bulbasaur', 10, 'grass', 50, 50)
#charmander.attack(bulbasaur)

class Trainer:

    def __init__(self, name, pk_list, potions, active_pk):
        self.name = name
        self.pk_list = pk_list
        self.potions = potions
        self.active_pk = active_pk

    def use_potion(self, pokemon):
        self.potions -= 1
        pokemon.gain_hp(20)
        print('You now have {} potions left'.format(self.potions))

    def attack(self, receiver_trainer):
        self.active_pk.attack(receiver_trainer.active_pk)

    def change_pk(self, chosen_pk):
        if chosen_pk.ko == False:
            self.active_pk = chosen_pk
            print('Your now active pokemon is {} and has {} hp left'.format(chosen_pk.name, chosen_pk.curr_hp))
        elif chosen_pk.ko == True:
            print('The chosen pokemon is not available, choose a different one!')
            
    def __repr__(self):
        return "Nome {}, pokemons {}, pk ativo: {}".format(self.name, str(self.pk_list), self.active_pk)