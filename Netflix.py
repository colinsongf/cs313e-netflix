
import sys

def netflix_read (r) :
  for line in r:
    line = line.strip()
    if line == "" :
      return
    return line

# calculates offset
def predict_ratings(a, overall_mean):
#  if a in dict_movie:


  if a in dict_user:
    a_rating = dict_user[a]
    rating = abs(overall_mean - a_rating)
  return rating

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
<<<<<<< HEAD
  ## this list is used for general input 
  cashe = []

  # our_predict = list for input customer ID
  our_predict = []

  # dict_movie = dictionary for actual ratings
=======
  ## this list is used to print movie ratings
  cache = []

  # dict_movie = dictionary for movie ID from cache_output.txt
>>>>>>> aaa696fd083eb68962f93ea96a3d6d024978efca
  dict_movie = {}
  # list_movie = search the input movie in c_movie
  # lists all the ratings for individual movie
  list_movie = []

  # dict_user = dictionary for customer ID from savant-cacheUsers.txt
  dict_user = {}
  # list_user = search the input muser in c_user
  # lists all the ratings for individual user
  list_user = []

<<<<<<< HEAD

  ## this list is used as an actual cashe
=======
  ## this list is used as an actual cache
>>>>>>> aaa696fd083eb68962f93ea96a3d6d024978efca
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


  while True :
    a = netflix_read(r)        
    if not a :
      for i in range (len(cache)):
            netflix_print(w, cache[i])

      rms = rmse(list_user, our_predict)
#      rms2 = rmse(list_movie, our_predict)
      print("rmse for user:", rms)
      return
    else:
      f = a.find(":")
      ## if runs for user IDs
      if f < 0 :
        # a = customer ID

        if a in dict_user: 
          # p = rating for customer     
          overall_mean = []
          overall_mean = overall_mean + (dict_user[a]/len(dict_user.keys()))
          p = predict_ratings(a, overall_mean) + overall_mean

          list_user.append(dict_user[a])
#         print("f_u", found_user)

          # list_user contains user ratings
          our_predict.append(p)
#         print("l_u", list_user)
          # cache contains user rating to print 
          cache.append(p)
        else:
<<<<<<< HEAD
          cashe.append("DNE")
=======
          cache.append("DNE")

        if f in dict_movie:
          found_movie.append(dict_movie[f])
          dict_movie[f] = p
          list_movie.append(p)
>>>>>>> aaa696fd083eb68962f93ea96a3d6d024978efca
          
      else:
        cache.append(a)


netflix_solve(sys.stdin, sys.stdout)

