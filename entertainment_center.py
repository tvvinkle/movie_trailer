import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

get_out = movie.Movie("Get Out",
                      "Now that Chris (Daniel Kaluuya) and his girlfriend, Rose (Allison Williams), have reached the meet-the-parents milestone of dating, she invites him for a weekend getaway upstate with Missy and Dean. At first, Chris reads the family's overly accommodating behavior as nervous attempts to deal with their daughter's interracial relationship, but as the weekend progresses, a series of increasingly disturbing discoveries lead him to a truth that he never could have imagined.",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcRzDpX6x-IiJdVRl_wP-Fqtr-Q9yuRHVEAvuIZ35BkEVZ6Yu34n",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

before_me = movie.Movie("Before Me",
                        "Before Me",
                        "https://images.redbox.com/Images/EPC/boxartvertical/7580.jpg",
                        "https://www.youtube.com/watch?v=T0MmkG_nG1U")

okja = movie.Movie("Okja",
                    "",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcSkeKv-OKoYw_T-ObRdOKEMfdTrQoJa6O4dLiOhca2PyD1ZkC5c",
                    "https://www.youtube.com/watch?v=AjCebKn4iic")

emoji = movie.Movie("The Emoji Movie",
                    "",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMzM3OTM2Ml5BMl5BanBnXkFtZTgwMDM0NDU3MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=r8pJt4dK_s4")

despicable = movie.Movie("Despicable Me 3",
                         "",
                         "http://t1.gstatic.com/images?q=tbn:ANd9GcTg3JQThacqbSPauObMc700jNW_GTAd-e9DAV_QIWvMYq8v3mVx",
                         "https://www.youtube.com/watch?v=6DBi41reeF0")

lalaland = movie.Movie("La LA Land",
                        "Love story",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcRhFtgdSYQ89vUMjMJal2D8H39qBCkh9ptCEoZEsafOzkeQPTu2",
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")

sing_street = movie.Movie("Sing Street",
                        "Sing on the street",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcT8740T9I0VTsHGFME_hPrx0Py1qf3t_7GMnBhcvz2hR3QdG6FT",
                        "https://www.youtube.com/watch?v=C_YqJ_aimkM")

civil_war = movie.Movie("Captain America: Civil War",
                        "Captain America: Civil War",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcTz1xU3qYlGXViIS51HIQh71D339ceW2nlWnb8zzSaJAL0newVj",
                        "https://www.youtube.com/watch?v=dKrVegVI0Us")



movies = [toy_story, get_out, before_me, okja, emoji, despicable, lalaland, sing_street, civil_war ]

fresh_tomatoes.open_movies_page(movies)

#print get_out.title, get_out.storyline

#get_out.show_trailer()
