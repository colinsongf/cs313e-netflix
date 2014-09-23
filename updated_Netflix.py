
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

  # dict_movie = dictionary for movie ID from cache_output.txt

  dict_movie = {}
  # list_movie = search the input movie in c_movie
  # lists all the ratings for individual movie
  list_movie = []

  # dict_user = dictionary for customer ID from savant-cacheUsers.txt
  dict_user = {}
  # list_user = search the input user in c_user
  # lists all the ratings for individual user
  list_user = []

  c_user = open("ctd446-userAverageRating.txt", "r")
  dict_user = eval(c_user.readline()) 
  sum = 0
  for i in dict_user.values():
    sum += float(i) 
  user_mean = sum / len(dict_user)   

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
               final_prediction = float(each_element) - movie_offset

               ## our_predict_m = list of predicted ratings with movie_offset, user_offset & user_mean
               our_predict_m.append(final_prediction)
     	       
		## list_movie = list of actual movie ratings
               list_movie.append(dict_movie[movie_id])
               
            ## printing final prediction (supposed to)
            netflix_print(w, cache[i])

      rms = rmse(list_user, our_predict_u)
#      rms2 = rmse(list_user, our_predict_m)
#      print("rmse (average of 2 rmse) for user:", (rms+rms2) / 2)
      print("rmse for user:", rms)
      return
    else:
      f = a.find(":")
      ## if runs for user IDs
      if f < 0 :
          # a = customer ID for this if statement
                
          ## adding the actual ratings for user "a"
          list_user.append(dict_user[a])

          ## calculates user offset
          user_offset = predict_offset(dict_user[a], user_mean)
          prediction = user_mean - user_offset
                  
          # our_predict contains predicted ratings with user offset
          our_predict_u.append(prediction)
        
          # cache contains user rating to print 
          cache.append(prediction)
          
      ## this "else" runs if it finds the movie ID in input     
      else:        
          cache.append(a)


netflix_solve(sys.stdin, sys.stdout)

"""
###################
### output
............
.............
...............
...........
3.169406045300062
9998:
4.079909923977818
3.848202606904646
3.223202606904646
9999:
4.548202606904646
rmse for user: 1.0837564786461598

"""
