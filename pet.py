class Pet:
    def __init__(self, name):
        self.name = name
        self.__hunger = 5
        self.__energy = 5
        self.__happiness = 5
        self.tricks = []

    def eat(self):
        self.__hunger = max(0, self.__hunger - 3)
        self.__happiness = min(10, self.__happiness + 1)
        print(f"\n🍖 {self.name} has eaten!")

    def sleep(self):
        self.__energy = min(10, self.__energy + 5)
        print(f"\n😴 {self.name} had a good sleep!")

    def play(self):
        if self.__energy >= 2:
            self.__energy -= 2
            self.__happiness = min(10, self.__happiness + 2)
            self.__hunger = min(10, self.__hunger + 1)
            print(f"\n🎾 {self.name} played and had fun!")
        else:
            print(f"\n⚠️ {self.name} is too tired to play! Try sleeping first.")

    def get_status(self):
        print(f"\n📊 {self.name}'s Current Status:")
        print(f"   Hunger:   {'🟩' * self.__hunger}{'⬜' * (10 - self.__hunger)} {self.__hunger}/10")
        print(f"   Energy:   {'🟩' * self.__energy}{'⬜' * (10 - self.__energy)} {self.__energy}/10")
        print(f"   Happiness: {'🟩' * self.__happiness}{'⬜' * (10 - self.__happiness)} {self.__happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        self.__happiness = min(10, self.__happiness + 1)
        print(f"\n🐕 {self.name} learned a new trick: '{trick}'!")

    def show_tricks(self):
        if self.tricks:
            print(f"\n🎭 {self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"\n❌ {self.name} hasn't learned any tricks yet.")
