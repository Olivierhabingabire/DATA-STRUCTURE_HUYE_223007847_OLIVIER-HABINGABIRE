####MOVIE RENTAL SYSTEM

from collections import deque
available_movies = []
rental_requests = deque()
recently_returned = []
def add_movie(movie):
    available_movies.append(movie)
    print(f"The movie:'{movie}' added to available list of movie.")

def rent_movie(customer):
    if available_movies:
        movie = available_movies.pop(0)
        print(f"The customer: '{customer}' rented movie: {movie}")
    else:
        rental_requests.append(customer) 
        print(f"No movies available to rent: '{customer}' you're on waiting list.")

def return_movie(movie):
    recently_returned.append(movie)
    available_movies.append(movie)
    print(f"This movie'{movie}' returned .")
   

def process_rentals():
   while recently_returned and rental_requests:
        movie = recently_returned.pop() 
        customer = rental_requests.popleft()  
        print(f"The customer: '{customer}' rented movie: {movie}   from recently returned movie")
        available_movies.pop()
     
        

def view_status():
    print("\nMOVIE RENTAL SYSTEM")
    print("Recently Returned Movies:", recently_returned)
    print("Rental Requests:", list(rental_requests))
    print("Available Movies:", available_movies)

add_movie("kanyombya")
add_movie("papa sava")
add_movie("bamenya")

rent_movie("olivier")
rent_movie("dior")
rent_movie("bahati pro")
rent_movie("bosco")

 
return_movie("kanyombya")
return_movie("papa sava")
return_movie("bamenya")


process_rentals()
view_status()
