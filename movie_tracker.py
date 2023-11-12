import pprint

# Enhanced Menu Prompt
MENU_PROMPT = """
╔══════════════════════════════════════════════════════════════╗
║                  Welcome to Movie Tracker!                   ║
║          Manage your personal movie collection.              ║
╠══════════════════════════════════════════════════════════════╣
║ Enter 'a' to add a movie                                     ║
║ Enter 'l' to list your movies                                ║
║ Enter 'f' to find a movie by title                           ║
║ Enter 'u' to update movie details                            ║
║ Enter 'q' to quit                                            ║
╚══════════════════════════════════════════════════════════════╝
Your choice: """
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year,
        'watch_date': None,
        'user_rating': None
    })

def list_movies():
    if not movies:
        print("\nNo movies added yet.\n")
        return

    print("\n╔════════ Movie List ════════╗")
    for movie in movies:
        watch_date = movie['watch_date'] if movie['watch_date'] else 'Not watched'
        user_rating = movie['user_rating'] if movie['user_rating'] else 'Not rated'
        print(f"║ Title: {movie['title']}")
        print(f"║ Director: {movie['director']}")
        print(f"║ Year: {movie['year']}")
        print(f"║ Watch Date: {watch_date}")
        print(f"║ Rating: {user_rating}")
        print("╟───────────────────────────╢")
    print("╚═══════════════════════════╝\n")

def find_movie():
    search_title = input("\nEnter the movie title you're looking for: ")
    found_movies = [movie for movie in movies if movie['title'].lower() == search_title.lower()]

    if not found_movies:
        print("\nMovie not found.\n")
        return None

    print("\n╔═══════ Found Movie ═══════╗")
    for movie in found_movies:
        print(f"║ Title: {movie['title']}")
        print(f"║ Director: {movie['director']}")
        print(f"║ Year: {movie['year']}")
        watch_date = movie['watch_date'] if movie['watch_date'] else 'Not watched'
        user_rating = movie['user_rating'] if movie['user_rating'] else 'Not rated'
        print(f"║ Watch Date: {watch_date}")
        print(f"║ Rating: {user_rating}")
        print("╚═══════════════════════════╝\n")
    return found_movies[0]  # Assuming you want to return the first found movie

def update_movie_details():
    movie = find_movie()
    if movie:
        movie['watch_date'] = input("When did you watch this movie? (YYYY-MM-DD): ")
        movie['user_rating'] = input("How would you rate this movie? (1-5): ")
        print("\nMovie updated successfully!\n")
    else:
        print("Movie not found.")

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            list_movies()
        elif selection == 'f':
            movie = find_movie()
            if movie:
                pprint.pprint(movie, sort_dicts=False)
            else:
                print("Movie not found.")
        elif selection == 'u':
            update_movie_details()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

# Start the program
menu()
