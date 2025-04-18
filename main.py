from pet import Pet

def main():
    pet_name = input("Name your pet: ")
    my_pet = Pet(pet_name)
    print(f"\n🎉 Creating pet: {pet_name}.")


    while True:
        print("\n Choose an action:")
        options = ["Eat", "Sleep", "Play","Train Trick","Show Tricks", "Get Status" "Exit"]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter a number (1-7): "))
            if choice == 1:
                my_pet.eat()
            elif choice == 2:
                my_pet.sleep()
            elif choice == 3:
                my_pet.play()
            elif choice == 4:
                trick = input("Enter a new trick: ")
                my_pet.train(trick)
            elif choice == 5:
                my_pet.show_tricks()  
            elif choice == 6:
                my_pet.get_status()      
            elif choice == 7:
                print("\n Final Status Before Exit:")
                my_pet.get_status()
                print("\n Goodbye! Take care of your pet!👋 ")
                break
            else:
                print("\n Invalid choice! Please enter a number between 1 and 6.")
        except ValueError:
            print("\n Please enter a valid number!")

if __name__ == "__main__":
    main()

