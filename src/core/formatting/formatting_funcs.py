def print_header(title, width):
    print_line(width)
    print("|" + title.upper().center(width, " ") + "|")
    print_line(width)

def print_line(width):
    print(f"+" + "=" * width + "+")

def get_table_width(title, data):
    longest = len(title)
    additional_spacing = 2
    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + additional_spacing

def menu_text():
    print("\nSelect an option by entering a number:")
    print("[1] Order a round")
    print("[2] List of people")
    print("[3] List of drinks")
    print("[4] Add a person")
    print("[5] Add a drink")
    print("[6] Specify favourite drink")
    print("[7] Display favourites")
    print("[8] Quit\n")

def create_table(title, data):
    width = get_table_width(title, data)
    print_header(title, width)
    for item in data:
        print("| " + item + (" " * (width-1 - len(item))) + "|")
    print_line(width)