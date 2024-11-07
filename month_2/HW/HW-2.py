from month_2.main import Hero
class Canonman(Hero):
    def __init__(self, name, health, shells=10):
        super().__init__(name, health)
        self.shells = shells

    def cast_spell(self):
        if self.shells >= 1:
            self.shells -= 1
            return f"{self.name} стреляет из пушки! Снарядов осталось: {self.shells}"
        else:
            return f"У {self.name} нет снарядов"

    def action(self):
        base_action = super().action()
        spell_result = self.cast_spell()
        return f"{base_action} {spell_result}"

def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())

canonman = Canonman("Пушечник", 100)

hero_action(canonman)