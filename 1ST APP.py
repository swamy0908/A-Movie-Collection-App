MENU_PROMPT= "\n enter 'a' to add a movie,'l' to see movies, 'f' to find a movie by title, or 'q' to quit:"
movies=[]
def add_movies():

    title=input("enter the movie title:")
    director=input("enter the director name")
    year=input("enter the year")

    movies.append({
        'title':title,
        'director':director,
        'year':year

    })


def show_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title:{movie['title']}")
    print(f"Director:{movie['director']}")
    print(f"Year:{movie['year']}")

def find_movie():
    search_title=input("enter the title your looking for:")

    for movie in movies:
        if movie['title']==search_title:
            print_movie(movie)


def menu():
    selection=input(MENU_PROMPT)
    while selection !="q":
        if selection=="a":
            add_movies()
        elif selection=="l":
            show_movies()
        elif selection=="f":
            find_movie()
        else:
            print("unknown input try again")

        selection=input()
menu()

