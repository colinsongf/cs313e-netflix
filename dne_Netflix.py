
import sys
import time
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
  for i in range (len(p)):
    f = p[i].find(":")
    g = r[i].find(":")
    if ((f < 0) & (g < 0)):
      f = p[i]
      g = r[i]
      s = sum(map(lambda x, y: (x-y) ** 2, g, f))
  return (s/len(r)) ** .5

def netflix_print (w, v) :
  w.write(str(v) + "\n")

def netflix_solve (r, w) :


  # list_movie = search the input movie in c_movie
  # lists all the ratings for individual movie
  list_movie = []

  # list_user = search the input user in c_user
  # lists all the ratings for individual user
  

# -------------- "actual" has actual output -------------------------------------------------------------------
  id_rtg = []
  actual = {}
  actual_rtgs = open("hs9234-probe_mv_rtg.txt", "r")
  for line in actual_rtgs:    
    line = line.strip()
    f = line.find(":")
    if f < 0:
      id_rtg.append(line)
    else:
      actual[line] = id_rtg
      id_rtg = []
#  print(actual)
#  print(actual['1:'])
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
     movie_line = line.strip()
     space = movie_line.find(" ")
     if space > -1:
       movie = int(movie_line[:space])
       movie_rtg = float(movie_line[space + 1:])
       dict_movie[movie] = movie_rtg
     sum = sum + float(movie_rtg)
  movie_mean = sum / len(dict_movie)

# --------------------------------------------------------------------------------------------------------------------------------------
  
  probe = []

  # u_offset = dictionary for user_offset with user ID as keys
  u_offset = []

  # our_predict = list for input customer ID
  our_predict = [] 
  start = time.time()
  m_id = ""
  while True :
    a = netflix_read(r) 

    ## this "if" runs after reading all the input       
    if not a :
      
      for i in range (len(u_offset)):
            ## accessing each element from "cache" which includes iputted movie IDs & 
            ## predicted ratings for iputted customer IDs. 
            ## (predicting ratings include user_mean & user offset)
            element = str(u_offset[i])
            f = element.find(":")

            ## "if" runs if each_element contains a movie ID
            if f > -1:
               movie_id = int(element[:f])
               our_predict.append(element)
#               netflix_print(w, element)       
            ## uses the movie-id from "if" statement & uses that movie_id to calculate movie offset
            else:
                         
               movie_offset = predict_offset(dict_movie[movie_id], movie_mean)
                              
               ## element = user_offset
               final_prediction =  movie_mean + float(element) + movie_offset
               
               ## our_predict_m = list of predicted ratings with movie_offset, user_offset & user_mean
               if final_prediction > 5:
                   final_prediction = 5
               if final_prediction < 2:
                   final_prediction = 2
              
               our_predict.append(str(final_prediction))     	       
#               netflix_print(w, (round(float(final_prediction), 1)))
#      print(len(list_movie), len(our_predict))
#      rms2 = rmse(list_movie, our_predict)
#      print("rmse:", rms2)
      end = time.time()
      print(end-start)
      return
    else:
      
      f = a.find(":")
      ## if runs for user IDs
      if f < 0 :
          # a = customer ID for this if statement
          for id in list_user:
            f = id.find(" ")
#            print("a", a, "id", id[:f])
            if a == id[:f]:
               list_movie.append(id[f+1:])
               # list_movie supposed to have actual ratings for inputted customer ids & movie ids
              
          ## calculates user offset
          user_offset = predict_offset(dict_user[a], user_mean)
                  
          # u_offset contains predicted ratings with user offset
          u_offset.append(user_offset)
          
      ## this "else" runs if it finds the movie ID in input     
      else:
          list_user = []
          # list_user has all the customer ID & actual ratings for a specific "a = movie_id"
          list_user = actual[str(a)]
          list_movie.append(a)
          u_offset.append(a)
          
  
netflix_solve(sys.stdin, sys.stdout)
