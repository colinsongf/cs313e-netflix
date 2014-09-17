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
    ## this list is used as an actual cashe
    c_public = []
    ## this list is used to skip movies to calculate rmse
    skip_movies = []
    l = " "
    while True :
        a = netflix_read(r)        
        if not a :
          for i in range (len(cashe)):
            netflix_print(w, cashe[i])

          rms = rmse(c_public, skip_movies)
          netflix_print(w, rms)
          return
        else:
          f = a.find(":")
          if f < 0 :
            p = predict_ratings(a)
            c_public.append(4)
            cashe.append(p)
            skip_movies.append(p)
          else:
            cashe.append(a)
            
#        x = len(c_public)
#        y = len(cashe)
#        print(x, y)
#    rms = rmse(c_public, cashe)
#    netflix_print(w, rms)


import sys

netflix_solve(sys.stdin, sys.stdout)