
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
    sq_diff = (float(r[i]) - int(p[i])) ** 2
    sum += sq_diff
  mean = sum / len(r)
  sq_root = mean ** .5
  return sq_root

def netflix_print (w, v) :
  w.write(str(v) + "\n")

def netflix_solve (r, w) :
  ## this list is used to print movie ratings
  cache = []

  # dict_movie = dictionary for movie ID from cache_output.txt
  dict_movie = {}
  # found_movie = search the input movie in c_movie
  found_movie = []
  # list_movie = list for movie ID

  # dict_user = dictionary for customer ID from savant-cacheUsers.txt
  dict_user = {}
  # found_user = search the input muser in c_user
  found_user = []
  # list_user = list for input customer ID
  list_user = []

  ## this list is used as an actual cache
  c_user = open("savant-cacheUsers.txt", "r")
  user = ""
  user_rtg = ""
  for line in c_user:
    line_user = line.strip()
    space = line_user.find(" ")
    if space > -1:
      user = line_user[:space]
      user_rtg = line_user[space + 1:]
      dict_user[user] = user_rtg


  c_movie = open("cashe_output.txt", "r")
  movie = ""
  movie_rtg = ""
  for line in c_movie:
    line_movie = line.strip()
    space = line_movie.find(" ")
    if space > -1:
      movie = line_movie[:space]
      movie_rtg = line_movie[space + 1:]
      dict_movie[movie] = movie_rtg


#  l = " "
  while True :
    a = netflix_read(r)        
    if not a :
      for i in range (len(cache)):
            netflix_print(w, cache[i])

      rms = rmse(found_user, list_user)
      rms2 = rmse(found_movie, list_movie)
      print("rmse for user:", rms)
      print("rmse for movie:", rms2)
      return
    else:
      f = a.find(":")
      ## if runs for user IDs
      if f < 0 :
        # a = customer ID
        # p = rating for customer       
        p = predict_ratings(a) 
        if a in dict_user: 
          found_user.append(dict_user[a])
#         print("f_u", found_user)

          # list_user contains user ratings
          list_user.append(p)
#         print("l_u", list_user)
          # cache contains user rating to print 
          cache.append(p)
        else:
          cache.append("DNE")

        if f in dict_movie:
          found_movie.append(dict_movie[f])
          dict_movie[f] = p
          list_movie.append(p)
          
      else:
        cache.append(a)
        dict_movie.append(f)
'''
            a = a[:f]
            list_movie.append(a)
            ## search for "a" in dict_movie
            if a in dict_movie:
              found_user.append(dict_movie[a])
              
              print(found_user)
'''

netflix_solve(sys.stdin, sys.stdout)

