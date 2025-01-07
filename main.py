# main.py
import functions

def main():
    file_path = "quotes.txt"
    quotes = functions.load_quotes(file_path)

    while True:
        print("\nMenu:")
        print("1. Random Quote")
        print("2. Add Quote")
        print("3. Display Quotes")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("\nRandom Quote:")
            print(functions.random_quote(quotes))
        elif choice == "2":
            new_quote = input("Enter the new quote: ")
            quotes = functions.add_quote(file_path, new_quote)
        elif choice == "3":
            count = int(input("How many quotes to display? "))
            print("\nDisplaying Quotes:")
            functions.display_quotes(quotes, count)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
