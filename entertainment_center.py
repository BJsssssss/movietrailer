import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "Story of a marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/"
                     "b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/"
                             "1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
# school_of_rock.show_trailer()

ratatouille = media.Movie("Ratatouille",
                          "Story of a rat who becomes a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/"
                          "50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/"
                                "9/9f"
                                "/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "A reality show in which contestants kill each "
                           "other"
                           "because they are hungry",
                           "https://upload.wikimedia.org/wikipedia/en/4/42"
                           "/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?"
                           "v=FovFG3N_RSU")


movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,
          hunger_games]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
