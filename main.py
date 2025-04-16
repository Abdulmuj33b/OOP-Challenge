from pet import Pet

def main():
    my_pet = Pet("Fluffy")

    while True:
        print("\nChoose an action:")
        print("1. Eat 🍖")
        print("2. Sleep 😴")
        print("3. Play 🎾")
        print("4. Get Status 📊")
        print("5. Train Trick 🐕")
        print("6. Show Tricks 🎭")
        print("7. Exit 🚪")

        try:
            choice = int(input("Enter a number (1-7): "))

            if choice == 1:
                my_pet.eat()
            elif choice == 2:
                my_pet.sleep()
            elif choice == 3:
                my_pet.play()
            elif choice == 4:
                my_pet.get_status()
            elif choice == 5:
                trick = input("Enter a new trick: ")
                my_pet.train(trick)
            elif choice == 6:
                my_pet.show_tricks()
            elif choice == 7:
                print("Goodbye! 👋")
                break
            else:
                print("Invalid choice, please enter a number between 1 and 7.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()



