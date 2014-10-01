import math
import pickle
def netflix_read (r) :
  for line in r:
    line = line.strip()
    f = line.find(" ")
    if f > -1:
      return
    return line

def netflix_print (w, v) :
     w.write(str(v) + "\n")

def rmse (r, p):
  return (sum(map(lambda x, y: (x-y) ** 2, r, p)) / len(p)) ** .5

def netflix_solve (r, w) :

  probe_ans = {}
  probe_ans = pickle.load( open( "/u/prat0318/netflix-tests/hs9234_probe_ans.p", "rb" ) )

  dict_user = {}
  dict_user = pickle.load( open( "/u/prat0318/netflix-tests/hs9234_offsets.p", "rb" ) )

# --------------------------------------------------------------------------------------------------------------------------------------
  probe = []
  while True :
    a = netflix_read(r) 

    ## this "if" runs after reading all the input       
    if not a:
      if len(probe) > 30000:
        m = 0
        sum = 0
        count = 0
        
        for i in range (len(probe)):
          
          if probe[i][-1:] == ":":
            m = int(probe[i][:-1])
            netflix_print(w, probe[i])
          else:
            count += 1
            actual_id = probe_ans[m][int(probe[i])]
            offst = dict_user[m][int(probe[i])]
            prediction = 3.3 + offst
            sum += (actual_id - prediction) ** 2
            netflix_print(w, round(prediction, 1))

        rms = (sum / count) ** .5
        print("RMSE:", round(rms, 2))
        return      

      else:
        m = 0
        sum = 0
        count = 0
        
        for i in range (len(probe)):
          
          if probe[i][-1:] == ":":
            m = int(probe[i][:-1])
            netflix_print(w, probe[i])
          else:
            count += 1
            actual_id = probe_ans[m][int(probe[i])]
            offst = dict_user[m][int(probe[i])]
            prediction = 3.3 + offst
            sum += (actual_id - prediction) ** 2
            netflix_print(w, round(prediction, 1))

        rms = (sum // count) ** .5
        print("RMSE:", format(rms, ".2f"))
        return      
      
    else:
      probe.append(a)
