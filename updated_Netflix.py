
import sys

def netflix_read (r) :
  for line in r:
    line = line.strip()
    if line == "" :
      return
    return line

# calculates offset
def predict_offset(a_rating, overall_mean):

  rating = float(a_rating) - overall_mean
  return rating

def rmse (r, p):
  assert (len(p) == len(r))
  sum = 0
  for i in range (len(p)):
    sq_diff = (float(r[i]) - float(p[i])) ** 2
    sum += sq_diff
  mean = sum / len(r)
  sq_root = mean ** .5
  return sq_root

def netflix_print (w, v) :
  w.write(str(v) + "\n")

def netflix_solve (r, w) :


  # list_movie = search the input movie in c_movie
  # lists all the ratings for individual movie
  list_movie = []

  # list_user = search the input user in c_user
  # lists all the ratings for individual user
  list_user = []

# -------------- "actual" has actual output -------------------------------------------------------------------
    
  actual = []
  actual_rtgs = open("/u/prat0318/netflix-tests/erb988-ProbeAnswers.txt", "r")
  for line in actual_rtgs:
     line = line.strip()
     f = line.find(":")
     if f < 0:
       actual.append(line)
  

     
  
# -------------- dict_user has customer IDs as keys & average rtgs of each customer as values--------------------------------------------------
  dict_user = {}
  c_user = open("/u/prat0318/netflix-tests/ctd446-userAverageRating.txt", "r")
  dict_user = eval(c_user.readline()) 
  sum = 0
  for i in dict_user.values():
    sum += float(i) 
  user_mean = sum / len(dict_user)

# -------------- dict_movie has movie IDs as keys & average rtgs of each movie as values--------------------------------------------------  

# cache for actual average and mode per movie
  c_movie = open("/u/prat0318/netflix-tests/aip256-cacheAvgAndModeRatingPerMovie.txt", "r")
  dict_movie = eval(c_movie.readline())
  sum_m = 0
  sum_mode = 0
  # i = each movie
  for i in dict_movie.values():
    # avg_m = average per movie
    # mode_m = mode per movie
    avg_m, mode_m = i[0], i[1]
    sum_m += float(avg_m)
    sum_mode += float(mode_m)
  # overall mean across all movies
  movie_mean = sum_m / len(dict_movie)
  mode_mean = sum_mode / len(dict_movie)

# --------------------------------------------------------------------------------------------------------------------------------------
  
  probe = []

  # u_offset = dictionary for user_offset with user ID as keys
  u_offset = []

  # our_predict = list for input customer ID
  our_predict = []  
  while True :
    a = netflix_read(r) 

    ## this "if" runs after reading all the input       
    if not a :
 
      for i in range (len(u_offset)):
            ## accessing each element from "cache" which includes iputted movie IDs & 
            ## predicted ratings for iputted customer IDs. 
            ## (predicting ratings include user_mean & user offset)
            element = str(u_offset[i])
            each_id = str(probe[i])
            f = element.find(":")
            g = each_id.find(":")

            ## "if" runs if each_element contains a movie ID
            if f > -1:
               movie_id = int(element[:f])
               
            
            ## uses the movie-id from "if" statement & uses that movie_id to calculate movie offset
            else:
                           
               movie_offset = predict_offset(dict_movie[movie_id][0], movie_mean)
               
               
               ## element = user_offset
               final_prediction =  movie_mean + float(element) + movie_offset
               
               ## our_predict_m = list of predicted ratings with movie_offset, user_offset & user_mean
               if final_prediction > 5:
                   final_prediction = 5
               if final_prediction < 2:
                   final_prediction = 2

               our_predict.append(final_prediction)
     	       
		## list_movie = list of actual movie ratings
               list_movie.append(dict_movie[movie_id])
               netflix_print(w, final_prediction)
               
            ## printing final prediction (supposed to)
#            netflix_print(w, cache[i])

      rms2 = rmse(actual, our_predict)
      print("RMSE:", round(rms2, 3)
      return
    else:
      f = a.find(":")
      ## if runs for user IDs
      if f < 0 :
          # a = customer ID for this if statement
          probe.append(dict_user[a])
          ## calculates user offset
          user_offset = predict_offset(dict_user[a], user_mean)
                  
          # u_offset contains predicted ratings with user offset
          u_offset.append(user_offset)
          
      ## this "else" runs if it finds the movie ID in input     
      else:        
          u_offset.append(a)
          probe.append(a)

  
netflix_solve(sys.stdin, sys.stdout)

