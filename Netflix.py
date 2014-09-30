import time
import math
def netflix_read (r) :
  for line in r:
    line = line.strip()
    if line == " " :
      return
    return line

def netflix_print (w, v) :
     w.write(str(v) + "\n")

def rmse (r, p):
  return (sum(map(lambda x, y: (x-y) ** 2, r, p)) / len(p)) ** .5

#def rms (r, p):
#  z = zip(r,p)
#  v = sum([(x - y) ** 2 for x, y in z])
#  return math.sqrt(v // len(r))

def netflix_solve (r, w) :
  start = time.time()
  probe_ans = eval(open("probe_dict.txt", "r").readline())
  dict_user = eval(open("predct.txt", "r").readline())

# --------------------------------------------------------------------------------------------------------------------------------------
  movie = []
  predict = []
#  actual_id = 0
#  offst = 0
#  d = {}
#  offset = {}
  count = 0
#  sum = 0
  while True :
      a = netflix_read(r)
      if not a:
        rms = format((rmse(movie, predict)), ".2f")
        print("RMSE:", rms)
        end = time.time()
        print(end-start)
        return
      else:
        f = a.find(":")
        if f > -1:
          m = int(a[:f])
          netflix_print(w, a)
        #  d = probe_ans[m]
        #  offset = dict_user[m]
        else: 
          count += 1
          actual_id = probe_ans[m][int(a)]
          offst = dc[m][int(a)]
          # prediction = 3.3 + offst
        #  if prediction > 5:
         #      prediction = 5
          movie.append(actual_id)
          predict.append(offst)
          netflix_print(w, offst)