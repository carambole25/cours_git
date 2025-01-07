from functions import *

def menu():
    print("1. Display a random quote")
    print("2. Display multiple quotes")
    print("3. Exit")

def main():
    quotes = load_quotes()  # Fonction qui charge les citations
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            display_quote(quotes)
        elif choice == "2":  # Gestion de l'affichage de plusieurs citations
            count = int(input("Enter the number of quotes to display: "))
            display_quotes(quotes, count)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
