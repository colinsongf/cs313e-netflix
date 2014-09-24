
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
    sq_diff = (float(r[i]) - int(p[i])) ** 2
    sum += sq_diff
  mean = sum / len(r)
  sq_root = mean ** .5
  return sq_root

def netflix_print (w, v) :
  w.write(str(v) + "\n")

def netflix_solve (r, w) :

  ## this list is used for general input 
  cashe = []

  # our_predict = list for input customer ID
  our_predict_u = []
  our_predict_m = []

  # dict_movie = dictionary for actual ratings

  ## this list is used to print movie ratings
  cache = []

  # list_movie = search the input movie in c_movie
  # lists all the ratings for individual movie
  list_movie = []

  # list_user = search the input user in c_user
  # lists all the ratings for individual user
  list_user = []

# -------------- "actual" has customer IDs as key & a list of movies w/rtgs -------------------------------------------------------------------
  # For example: {"378466": [["13636", "5", "2005-01-30"], ["16532", "3", "2005-01-30"]],_ _ _ }  
  actual = {}
  actual_rtgs = open("mjh3664customer.txt", "r")
  actual = eval(actual_rtgs.readline()) 
     
  
# -------------- dict_user has customer IDs as keys & average rtgs of each customer as values--------------------------------------------------
  dict_user = {}
  c_user = open("ctd446-userAverageRating.txt", "r")
  dict_user = eval(c_user.readline()) 
  sum = 0
  for i in dict_user.values():
    sum += float(i) 
  user_mean = sum / len(dict_user)

# -------------- dict_movie has movie IDs as keys & average rtgs of each movie as values--------------------------------------------------  
  dict_movie = {}
  c_movie = open("hs9234-mvrtg.txt", "r")
  movie = ""
  movie_rtg = ""
  sum = 0
  for line in c_movie:
    line_movie = line.strip()
    space = line_movie.find(" ")
    if space > -1:
      movie = line_movie[:space]
      movie_rtg = line_movie[space + 1:]
      dict_movie[movie] = movie_rtg
      sum = sum + float(movie_rtg)
  movie_mean = sum / len(dict_movie)
  
# --------------------------------------------------------------------------------------------------------------------------------------
  # u_offset = dictionary for user_offset with user ID as keys
  u_offset = {}

  # our_predict = list for input customer ID
  our_predict = []  
  while True :
    a = netflix_read(r) 

    ## this "if" runs after reading all the input       
    if not a :
      
      for i in range (len(cache)):
            ## accessing each element from "cache" which includes iputted movie IDs & 
            ## predicted ratings for iputted customer IDs. 
            ## (predicting ratings include user_mean & user offset)
            
            each_element = str(cache[i])             
            f = each_element.find(":")

            ## "if" runs if each_element contains a movie ID
            if f > -1:
               movie_id = each_element[:f]
            
            ## uses the movie-id from "if" statement & uses that movie_id to calculate movie offset
            else:
               movie_offset = predict_offset(dict_movie[movie_id], movie_mean)
               final_prediction =  float(each_element) + movie_offset + movie_mean

               ## our_predict_m = list of predicted ratings with movie_offset, user_offset & user_mean
               our_predict_m.append(final_prediction)
     	       
		## list_movie = list of actual movie ratings
               list_movie.append(dict_movie[movie_id])
               netflix_print(w, float(each_element))
               
            ## printing final prediction (supposed to)
            netflix_print(w, cache[i])

      rms2 = rmse(list_user, our_predict_m)
      print("rmse for user:", rms2)
      

      return
    else:
      f = a.find(":")
      ## if runs for user IDs
      if f < 0 :
          # a = customer ID for this if statement

          ## calculates user offset
          user_offset = predict_offset(dict_user[a], user_mean)
                  
          # u_offset contains predicted ratings with user offset
          u_offset[a] = user_offset
          
      ## this "else" runs if it finds the movie ID in input     
      else:        
          u_offset[a] = a

  
netflix_solve(sys.stdin, sys.stdout)

