import fresh_tomatoes
import media

#create movie object instances of each movie title

commando = media.Movie("Commando",
                        "Commando goes after those who took his daughter",
                        "https://upload.wikimedia.org/wikipedia/en/"
                        "d/d9/Commandoposter.jpg",
                        "https://www.youtube.com/watch?v=m264f4tfG2s")
# print(commando.storyline)

thematrix = media.Movie("The Matrix",
                     "Dystopian movie of humans in a simulated world",
                     "https://upload.wikimedia.org/wikipedia/en/"
                     "c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=tGgCqGm_6Hs")
# print(thematrix.storyline)
# thematrix.show_trailer()

castaway = media.Movie("Castaway",
                             "Survival film of a man on a desolate island",
                             "https://upload.wikimedia.org/wikipedia/en"
                             "/a/a7/Cast_away_film_poster.jpg",
                             "https://www.youtube.com/watch?v=VfXpFgyAY_U")
# castaway.show_trailer()

braveheart = media.Movie("Braveheart",
                          "Story of a Scottish freedom fighter",
                          "https://upload.wikimedia.org/wikipedia/en/"
                          "5/55/Braveheart_imp.jpg",
                          "https://www.youtube.com/watch?v=rXYCBBJBj6Y")

grantorino = media.Movie("Gran Torino",
                         "Korean war vet takes on street gang",
                         "https://upload.wikimedia.org/wikipedia/en/"
                         "c/c6/Gran_Torino_poster.jpg",
                         "https://www.youtube.com/watch?v=RMhbr2XQblk")

expendables = media.Movie("Expendables",
                           "Mercenaries tasked to take out a dictator",
                           "https://upload.wikimedia.org/wikipedia/en/"
                           "7/76/Expendablesposter.jpg",
                           "https://www.youtube.com/watch?v=8KtYRALe-xo")


# create array of movie titles for display in html page
movies = [commando, thematrix, castaway, braveheart, grantorino,
          expendables]

# call open_movies_page function of fresh_tomatoes class that brings up
# description, movie poster and trailer of each movie object
fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
