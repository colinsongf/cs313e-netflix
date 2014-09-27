import sys
import math
def netflix_read (r) :
  for line in r:
    line = line.strip()
    if line == " " :
      return
    elif line == "\n":
      return
    return line

# calculates offset
def predict_offset(a_rating, overall_mean):
  rating = float(a_rating) - overall_mean
  return rating

def rmse (r, p):
  s = 0
  for i in range (len(p)):
      s = sum(map(lambda x, y: (x-y) ** 2, r, p))
  if len(p) > 0 :
    return (s//len(p)) ** .5
  else:
    return 0

def netflix_print (w, v) :
   w.write(str(v) + "\n")

def netflix_solve (r, w) :

# -------------- "actual" has actual output -------------------------------------------------------------------
  probe_ans = []
  actual_rts = open("/u/prat0318/netflix-tests/erb988-ProbeAnswers.txt", "r")
  for line in actual_rts:
     line = line.strip()
     probe_ans.append(line)

  id_rtg = []
  actual = {}
  actual_rtgs = open("/u/prat0318/netflix-tests/hs9234-probe_mv_rtg.txt", "r")
  for line in actual_rtgs:    
    line = line.strip()
    f = line.find(":")
    if f < 0:
      id_rtg.append(line)
    else:
      actual[int(line[:f])] = id_rtg
      id_rtg = []


# -------------- dict_user has customer IDs as keys & average rtgs of each customer as values--------------------------------------------------
  dict_user = {}
  c_user = open("/u/prat0318/netflix-tests/hs9234_user_offset_dict.txt", "r")
  dict_user = eval(c_user.readline()) 
  user_mean = 3.67410130345234

# -------------- dict_movie has movie IDs as keys & average rtgs of each movie as values--------------------------------------------------  
  dict_movie = {}
  c_movie = open("/u/prat0318/netflix-tests/hs9234_movie_offset_dict.txt", "r")
  dict_movie = eval(c_movie.readline())
  movie_mean = 3.2285762521103103

# --------------------------------------------------------------------------------------------------------------------------------------
  probe = []
  while True :
    a = netflix_read(r) 

    ## this "if" runs after reading all the input       
    if not a:
      if len(probe) == len(probe_ans):
        l = 0
        u_offset = []
        list_movie = []
        m_id = ""
        for i in range (len(probe)):
          
          f = probe[i].find(":")
          ## if runs for user IDs
          if f < 0 :
            l += 1
            # a = customer ID for this if statement
            list_movie.append(float(probe_ans[i]))
             
            final_prediction = float(dict_user[probe[i]]) + float(dict_movie[m_id]) + 3.3
            
            if final_prediction > 5:
                  final_prediction = 5
            if (float(dict_user[probe[i]]) + float(dict_movie[m_id])) < 0:
                  final_prediction -= .1
            if (float(dict_user[probe[i]]) + float(dict_movie[m_id])) > 0:
                  final_prediction += .05
            if float(dict_user[probe[i]]) < 0:
                  final_prediction -=.005
            if float(dict_user[probe[i]]) > 0:
                  final_prediction +=.005
            if float(dict_movie[m_id]) < 0:
                  final_prediction +=.025
            if float(dict_movie[m_id]) > 0:
                  final_prediction -=.025

            u_offset.append(final_prediction)
            str(final_prediction)
            netflix_print(w, format(final_prediction, ".1f"))  
          else:
            l += 1
            # list_user has all the customer ID & actual ratings for a specific "a = movie_id"
            m_id = probe[i][:f]
            netflix_print(w, probe[i])
        rms2 = format((rms(list_movie, u_offset)), ".2f")
        if float(rms2) > 0:
          print("RMSE:", rms2)            

      else:
        u_offset = []
        list_movie = []
        m_id = ""
        for i in probe:
          f = i.find(":")
          ## if runs for user IDs
          if f < 0 :
            # a = customer ID for this if statement
            for id in list_user:
              f = id.find(" ")
              if i == id[:f]:
                 list_movie.append(float(id[f+1:]))
           
            final_prediction = float(dict_user[i]) + float(dict_movie[m_id]) + 3.3
          
            if final_prediction > 5:
                  final_prediction = 5
            if (float(dict_user[i]) + float(dict_movie[m_id])) < 0:
                  final_prediction -= .1
            if (float(dict_user[i]) + float(dict_movie[m_id])) > 0:
                  final_prediction += .05
            if float(dict_user[i]) < 0:
                  final_prediction -=.005
            if float(dict_user[i]) > 0:
                  final_prediction +=.005
            if float(dict_movie[m_id]) < 0:
                  final_prediction +=.025
            if float(dict_movie[m_id]) > 0:
                  final_prediction -=.025

            u_offset.append(final_prediction)
            str(final_prediction)
            netflix_print(w, format(final_prediction, ".1f"))
          ## this "else" runs if it finds the movie ID in input     
          else:
            netflix_print(w, i)
            list_user = []
            # list_user has all the customer ID & actual ratings for a specific "a = movie_id"
            m_id = i[:f]
            list_user = actual[int(m_id)]

        rms2 = format((rmse(list_movie, u_offset)), ".2f")
        if float(rms2) > 0:
          print("RMSE:", rms2)
      return
      
    else:
      probe.append(a)

netflix_solve(sys.stdin, sys.stdout)

