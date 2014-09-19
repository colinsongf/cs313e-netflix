
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
    cashe = []

    # list_user = list for input customer ID
    list_user = []

    # dict_movie = dictionary for movie ID from cashe_output.txt
    dict_movie = {}
    # dict_user = dictionary for customer ID from savant-cacheUsers.txt
    dict_user = {}

    # found_movie = search the input movie in c_movie
    found_movie = []

    # found_user = search the input muser in c_user
    found_user = []

    ## this list is used as an actual cashe
    c_user = open("savant-cacheUsers.txt", "r")
    
    c_movie = open("cashe_output.txt", "r")
    user = ""
    user_rtg = ""
    for line in c_user:
        line = line.strip()
        space = line.find(" ")
        if space > -1:
            user = line[:space]
            user_rtg = line[space + 1:]
            dict_user[user] = user_rtg

    l = " "
    while True :
        a = netflix_read(r)        
        if not a :
          for i in range (len(cashe)):
            netflix_print(w, cashe[i])

          rms = rmse(found_user, list_user)
          print("rmse:", rms)
          return
        else:
          f = a.find(":")
          ## if runs for user IDs
          if f < 0 :

            if a in dict_user: 
              found_user.append(dict_user[a])
#              print("f_u", found_user)
            
              # a = customer ID
              # p = rating for customer       
              p = predict_ratings(a)
            
              # list_user contains user ratings
              list_user.append(p)
#              print("l_u", list_user)
            
              # cashe contains user rating to print 
              cashe.append(p)

            else:
              cashe.append("DNE")
          
          else:
            cashe.append(a)

'''
            a = a[:f]
            list_movie.append(a)
            ## search for "a" in dict_movie
            if a in dict_movie:
              found_user.append(dict_movie[a])
              
              print(found_user)
'''


netflix_solve(sys.stdin, sys.stdout)

