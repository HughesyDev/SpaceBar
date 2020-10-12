def print_header(title, width):
    print_soft_line(width)
    print("|" + title.upper().center(width, " ") + "|")
    print_soft_line(width)

def print_soft_line(width):
    print(f"+" + "-" * width + "+")


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
    print("  1 | Order a round")
    print("  2 | Display members of your party")
    print("  3 | Show available drinks")
    print("  4 | Add a person")
    print("  5 | Add a drink")
    print("  6 | Specify drink preference")
    print("  7 | Display preferences")
    print("  8 | Quit\n")

def create_table(title, data):
    width = get_table_width(title, data)
    if width % 2 == 1: # If width is odd number, title is off-centre, this evens width out for perfect centering of title
        width+=1
    print_header(title, width)

    for item in data:
        print("| " + item + (" " * (width-1 - len(item))) + "|")
    print_soft_line(width)

def clear_and_show_logo():
    os.system("clear")
    greeting_ascii_art

#### NEW TABLE TAKING IN i.e. ID : NAME : DRINK for prefs, or X ordered Y
# Currently they take in a single string, but it LOOKS like it's formatted for two columns, it's ONE.

dummydata = {"FIRST": "SECOND",
           "a": "b",
           "aaaaaddddddddddddddddddddd":"bbsssssssssssssssssbb"}

def new_table(title, data): # expecting two pieces of data.
    width = table_total_width(title, data)

    SPACING = 2

    field_one, field_two = list(zip(*data.items()))
    width_field_one = len(max(field_one, key=len))
    width_field_two = len(max(field_two, key=len))

    print_header(title, width)

    for first, second in data.items():
        column_one = "|" + " " + first  + " " * (width_field_one - len(first))  + " " + "|"
        column_two =       " " + second + " " * (width_field_two - len(second)) + " " + "|"
        print(column_one + column_two)

    print_soft_line(width)

def table_total_width(title, data):
    longest = len(title)
    additional_spacing = 6

    for item1, item2 in data.items():
        if len(item1 + item2) > longest:
            longest = len(item1 + item2)

    return longest + additional_spacing -1


new_table("TEST TITLE", dummydata)