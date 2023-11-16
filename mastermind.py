import random
class Mastermind:
    def __init__(self, color=6, position=4):
        self.__answer = ''
        self.color = color
        self.position = position

    def __str__(self):
        return f"Playing Mastermind with {self.color} colors and {self.position} position"

    def random_answer(self):
        for i in range(1, self.position+1):
            self.__answer += str(random.randint(1, self.color))

    def checking(self, guess: str):
        result1 = ''
        result2 = ''
        for i,j in enumerate(self.__answer):
            print(j,guess[i])
            if j == guess[i]:
                result1 += '*'
            elif j in guess:
                result2 += 'o'

        return result1 + result2

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position


while True:
    gaem = Mastermind()
    print(str(gaem))
    gaem.random_answer()
    tries = 0
    while True:
        user_input = input("What's your guess?: ")
        gaem_result = gaem.checking(user_input)
        tries += 1
        print(gaem_result)
        if gaem_result == '****':
            print(f"You solve it after {tries} rounds.")
            break
        else:
            print("HaHa you did a good job but it's not good enough")
    print("Would you like to play the game again?")
    again = int(input("Play again type 1 if you dont want to play again type 0: "))
    if again == 1:
        tries = 0
    elif again == 0:
        yes = input("Or you wanna change the amount of number? Yes/No: ")
        if yes == "Yes":
            count = 0
            while True:
                numbera = int(input("Input your number: "))
                if numbera > 8:
                    print("Number must not be more than 8. Try again my friend.")
                    numbera = int(input("Input your number: "))
                    count += 1
                    if count > 3:
                        print("That's it goodbye.")
                elif numbera == 8:
                    gaem.random_answer(numbera)
                    print("thank you")

                    break
        if yes == "No":
            print("Aight bro cya")
            break










