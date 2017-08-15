"""
Provide all information of movies

example:
  Movie_Title = movie.Movie(
    "Movie_Title",
    "Movie_Storyline",
    "Movie_Poster_URL",
    "Movie_Trailer_URL")
"""

import movie  # parent class object
import fresh_tomatoes  # scripting for generate html page

toy_story = movie.Movie(
  "Toy Story",
  '''A story of a boy and his toys that come to life''',
  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
  "https://www.youtube.com/watch?v=vwyZH85NQC4")

get_out = movie.Movie(
  "Get Out",
  '''Now that Chris (Daniel Kaluuya) and his girlfriend, \
  Rose (Allison Williams), have reached the meet-the-parents \
  milestone of dating, she invites him for a weekend getaway \
  upstate with Missy and Dean. At first, Chris reads the family's \
  overly accommodating behavior as nervous attempts to deal with \
  their daughter's interracial relationship, but as the weekend \
  progresses, a series of increasingly disturbing discoveries lead \
  him to a truth that he never could have imagined.''',
  "http://t3.gstatic.com/images?q=tbn:ANd9GcRzDpX6x-IiJdVRl_wP-Fqtr-Q9yuRHVEAvuIZ35BkEVZ6Yu34n",  # noqa
  "https://www.youtube.com/watch?v=sRfnevzM9kQ")

before_me = movie.Movie(
  "Before Me",
  '''Young and quirky Louisa 'Lou' Clark (Emilia Clarke) moves from one \
  job to the next to help her family make ends meet. Her cheerful \
  attitude is put to the test when she becomes a caregiver for Will \
  Traynor (Sam Claflin), a wealthy young banker left paralyzed from an \
  accident two years earlier. Will's cynical outlook starts to change \
  when Louisa shows him that life is worth living. As their bond deepens, \
  their lives and hearts change in ways neither one could have imagined.''',
  "https://images.redbox.com/Images/EPC/boxartvertical/7580.jpg",
  "https://www.youtube.com/watch?v=T0MmkG_nG1U"
)

okja = movie.Movie(
  "Okja",
  '''For 10 idyllic years, young Mija has been caretaker and constant \
  companion to Okja - a massive animal and an even bigger friend - \
  at her home in the mountains of South Korea. But that changes when \
  family-owned, multinational conglomerate Mirando Corporation takes \
  Okja for themselves and transports her to New York, where an \
  image-obsessed and self-promoting CEO has big plans for Mija's \
  dearest friend. With no particular plan but single-minded in intent, \
  Mija sets out on a rescue mission.''',
  "http://t1.gstatic.com/images?q=tbn:ANd9GcSkeKv-OKoYw_T-ObRdOKEMfdTrQoJa6O4dLiOhca2PyD1ZkC5c",  # noqa
  "https://www.youtube.com/watch?v=AjCebKn4iic")

emoji = movie.Movie(
  "The Emoji Movie",
  '''Hidden inside a smartphone, the bustling city of \
  Textopolis is home to all emojis. Each emoji has only \
  one facial expression, except for Gene, an exuberant emoji \
  with multiple expressions. Determined to become 'normal' like \
  the other emojis, Gene enlists the help of his best friend Hi-5 \
  and a notorious code breaker called Jailbreak. During their \
  travels through the other apps, the three emojis discover a \
  great danger that could threaten their phone's very existence.''',
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMzM3OTM2Ml5BMl5BanBnXkFtZTgwMDM0NDU3MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
  "https://www.youtube.com/watch?v=r8pJt4dK_s4")

despicable = movie.Movie(
  "Despicable Me 3",
  '''The mischievous Minions hope that Gru will return to a life of\
  crime after the new boss of the Anti-Villain League fires him. \
  Instead, Gru decides to remain retired and travel to Freedonia to \
  meet his long-lost twin brother for the first time. The reunited \
  siblings soon find themselves in an uneasy alliance to take down \
  the elusive Balthazar Bratt, a former 1980s child star who seeks \
  revenge against the world.''',
  "http://t1.gstatic.com/images?q=tbn:ANd9GcTg3JQThacqbSPauObMc700jNW_GTAd-e9DAV_QIWvMYq8v3mVx",  # noqa
  "https://www.youtube.com/watch?v=6DBi41reeF0")

lalaland = movie.Movie(
  "La LA Land",
  '''Sebastian (Ryan Gosling) and Mia (Emma Stone) are drawn together\
  by their common desire to do what they love. But as success mounts\
  they are faced with decisions that begin to fray the fragile fabric\
  of their love affair, and the dreams they worked so hard to maintain\
  in each other threaten to rip them apart.''',
  "http://t2.gstatic.com/images?q=tbn:ANd9GcRhFtgdSYQ89vUMjMJal2D8H39qBCkh9ptCEoZEsafOzkeQPTu2",  # noqa
  "https://www.youtube.com/watch?v=0pdqf4P9MB8")

sing_street = movie.Movie(
  "Sing Street",
  '''In 1985, a Dublin teenager (Ferdia Walsh-Peelo) forms a rock n roll band\
  to win the heart of an aspiring model''',
  "http://t0.gstatic.com/images?q=tbn:ANd9GcT8740T9I0VTsHGFME_hPrx0Py1qf3t_7GMnBhcvz2hR3QdG6FT",  # noqa
  "https://www.youtube.com/watch?v=C_YqJ_aimkM")

civil_war = movie.Movie(
  "Captain America: Civil War",
  '''Political interference in the Avengers' activities causes a \
  rift between former allies Captain America and Iron Man.''',
  "http://t3.gstatic.com/images?q=tbn:ANd9GcTz1xU3qYlGXViIS51HIQh71D339ceW2nlWnb8zzSaJAL0newVj",  # noqa
  "https://www.youtube.com/watch?v=dKrVegVI0Us")

# add all movies in the list

movies = [
  toy_story,
  get_out,
  before_me,
  okja,
  emoji,
  despicable,
  lalaland,
  sing_street,
  civil_war
]

"""
Invoce function in fresh_tomatoes modue,
this function recieves a list of movies,
and provide an HTML file that displays movies
"""

fresh_tomatoes.open_movies_page(movies)
