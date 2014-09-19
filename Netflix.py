
import sys

def netflix_read (r) :
    for line in r:
      line = line.strip()
      if line == "" :
        return
      return line

def predict_ratings(a):
    return 3

def rmse (r, p):
    assert (len(p) == len(r))
    sum = 0
    for i in range (len(p)):
      sq_diff = (r[i] - p[i]) ** 2
      sum += sq_diff
    mean = sum / len(r)
    sq_root = mean ** .5
    return sq_root

def netflix_print (w, v) :
    w.write(str(v) + "\n")

def netflix_solve (r, w) :
    ## this list is used to print movie ratings
    cashe = []
    # list_movie = list for input movie
    list_movie = []
    # dict_movie = dictionary for movie ID from cashe_output.txt
    dict_movie = {}
    ## this list is used as an actual cashe
    c_user = open("/u/hyunji/cs313e-netflix/savant-cacheUsers.txt", "r")
    
    c_movie = open("/u/hyunji/cs313e-netflix/cashe_output.txt", "r")
    movie = ""
    movie_rtg = ""
    for line in c_movie:
        line = line.strip()
        space = line.find(" ")
        if space > -1:
            movie = line[:space]
            movie_rtg = line[space + 1:]
        # movie, movie_rtg = line.split(" ")
            dict_movie[movie] = movie_rtg
      
    ## this list is used to skip movies to calculate rmse
    skip_movies = []
    l = " "
    while True :
        a = netflix_read(r)        
        if not a :
          for i in range (len(cashe)):
            netflix_print(w, cashe[i])

          rms = rmse(c_user, skip_movies)
          netflix_print(w, rms)
          return
        else:
          f = a.find(":")
          if f < 0 :
            # a = customer ID
            # p = rating for customer
            p = predict_ratings(a)
            # c_user.append(4)
            cashe.append(p)
            skip_movies.append(p)
          else:
            list_movie.append(a)
            cashe.append(a)
            
#        x = len(c_public)
#        y = len(cashe)
        print(x, y)
#    rms = rmse(c_public, cashe)
#    netflix_print(w, rms)



netflix_solve(sys.stdin, sys.stdout)

