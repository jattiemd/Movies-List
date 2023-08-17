# Movies list initialization
movies = []

# Main Menu
MENU = """
========================
Movie List Application
========================
'a' -- Add movie
'f' -- Find movie
's' -- Show all movies
'q' -- Quit"""


# function that adds a movie to the list
def add():  
    title = input("Title: ").strip().lower()
    director = input("Director: ").strip().lower()
    year = input("Release year: ").strip()

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })
    print(f"\n{title.title()} ({year}) by {director.title()} successfully added!")


def print_movie(movie):  # Printing movie to reduce repetition
    print(f"\n--{movie['title'].title()} ({movie['year']}) by {movie['director']}")


# Search a movie
def find():  
    user_input = input("\nEnter the title of the movie that you are searching for? ").strip().lower()

    for movie in movies:
        if movie["title"] == user_input:
            print_movie(movie)


# Display all movies in Movies List
def show():  
    for movie in movies:
        print_movie(movie)


# Menu operations
def menu():
    while True:
        print(MENU)
        selection = input("\nSelection: ").lower().strip()

        if selection == 'a':
            add()
        elif selection == 'f':
            find()
        elif selection == 's':
            show()
        elif selection == 'q':
            print("Exiting Application...")
            break
        else:
            print("Invalid Selection! Please select a letter from the menu")


# Calling Menu function
menu()


