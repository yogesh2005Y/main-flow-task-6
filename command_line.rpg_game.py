class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= max(0, damage - self.defense)

class Game:
    def __init__(self):
        self.player = Character("Hero", 100, 15, 5)
        self.inventory = []

    def battle(self, enemy):
        print(f"A wild {enemy.name} appears!")
        while self.player.is_alive() and enemy.is_alive():
            enemy.take_damage(self.player.attack)
            print(f"You attack {enemy.name}, HP left: {enemy.hp}")
            if enemy.is_alive():
                self.player.take_damage(enemy.attack)
                print(f"{enemy.name} attacks back, your HP: {self.player.hp}")

        if self.player.is_alive():
            print(f"You defeated {enemy.name}!")
        else:
            print("Game Over!")

    def start(self):
        print("Welcome to the RPG!")
        self.battle(Character("Goblin", 30, 10, 2))

if __name__ == "__main__":
    game = Game()
    game.start()
