
import sys

def netflix_read (r) :
  for line in r:
    line = line.strip()
    if line == "" :
      return
    return line

# calculates offset
def predict_offset(rating, mean):
  offset = float(rating) - mean
  return offset

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
  ## this list is used for general input/output
  cache = []

  # predictions
  our_predict_u = []
  our_predict_m = []

  # dict_movie = {movie ID: [avg, mode]}
  dict_movie = {}
  # lists all the ratings for individual movie
  list_movie = []

  # dict_user = {customer ID: [avg, mode]}
  dict_user = {}
  # lists all the ratings for individual user
  list_user = []

# =============== CACHES ======================

# cache for actual average and mode per customer
  c_user = open("aip256-cacheAvgAndModeRatingPerCust.txt", "r")
  dict_user = eval(c_user.readline()) 
  sum_u = 0
  # i = each user
  for i in dict_user.values():
    # avg_u = average per user
    # mode_u = mode per user
    avg_u, mode_u = i[0], i[1]
    sum_u += float(avg_u)
  # overall mean across all users
  user_mean = sum_u/len(dict_user)   

# cache for actual average and mode per movie
  c_movie = open("aip256-cacheAvgAndModeRatingPerMovie.txt", "r")
  dict_movie = eval(c_movie.readline())
  sum_m = 0
  # i = each movie
  for i in dict_movie.value():
    # avg_m = average per movie
    # mode_m = mode per movie
    avg_m, mode_m = i[0], i[1]
    sum_m += float(avg_m)
  # overall mean across all movies
  movie_mean = sum_m / len(dict_movie)

# -----------------------------------------------------------------
  while True :
    a = netflix_read(r)
    ## output       
    if not a :
      for i in range (len(cache)):
        ## accessing each element from "cache" 
        ## includes inputted movie IDs & predicted ratings for inputted customer IDs
        ## (predicting ratings include user_mean & user offset)
        line_c = str(cache[i])             
        f = line_c.find(":")

        ## runs if line_c contains a movie ID
        if f > -1:
          movie_id = line_c[:f]

        ## runs if line_c contains a rating
        ## uses the movie_id from loop just above & uses it to calculate MOVIE OFFSET
        else:
#           NEED TO FIX LINE BELOW (dict_movie[movie_id] now returns a list of 2 values)
          # movie_offset = predict_offset(dict_movie[movie_id], movie_mean)

          # final_prediction = rating + movie_offset + movie_mode_offset
          final_prediction = float(line_c) + movie_offset + movie_mode_offset

          ## our_predict_m = list of predicted ratings (what's in this?)
          our_predict_m.append(final_prediction)

#           NEED TO FIX LINE BELOW (dict_movie[movie_id] now returns a list of 2 values)
          ## list_movie = list of actual movie ratings
          list_movie.append(dict_movie[movie_id])
  
        ## printing final prediction (supposed to)
        netflix_print(w, cache[i])

      rms = rmse(list_user, our_predict_u)
      rms2 = rmse(list_movie, our_predict_m)
      print("user rmse:", rms)
      print("movie rmse:", rms2)
      print("rmse (average of movie and user)", (rms + rms2) / 2)
      return

    # reads input
    else:
      f = a.find(":")
      ## runs for user IDs
      if f < 0 :
          # a = customer ID for this loop
          '''      
          ## adding the actual ratings for user "a"
          list_user.append(dict_user[a])

          ## calculates user offset
          user_offset = predict_offset(dict_user[a], user_mean)
          prediction = user_mean - user_offset
                  
          # our_predict contains predicted ratings with user offset
          our_predict_u.append(prediction)
        
          # cache contains user rating to print 
          cache.append(prediction)
          '''
      ## runs if it finds the movie ID in input     
      else:
          # a = movie ID for this loop      
          cache.append(a)
# --------------------------------------------------------------------------------------

netflix_solve(sys.stdin, sys.stdout)