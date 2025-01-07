# functions.py
def load_quotes(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def random_quote(quotes):
    import random
    return random.choice(quotes)

def print_quote(quote):
    print(quote)

def view_quotes(quotes):
    for quote in quotes:
        print(quote)

def add_quote(file_path, new_quote):
    """Adds a new quote to the file and returns the updated list of quotes."""
    with open(file_path, "a") as file:
        file.write(new_quote + "\n")
    print("Quote added successfully!")
    return load_quotes(file_path)

def display_quotes(quotes, count):
    """Displays the first 'count' quotes from the list."""
    count = min(count, len(quotes))
    for i in range(count):
        print(quotes[i])
