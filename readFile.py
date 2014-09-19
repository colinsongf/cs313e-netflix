# cache for average rating/movie

import math
import string

def netflix_read (r) :
    s = r.readline()
    z = s.find(":")
    # m = movie ID
    if (z > -1):
        m = s[:z]

    sum_a = 0
    count_a = 0
    for line in r:
      line = line.strip()
      # a = ratings for given customer
      a = ""
      f = line.find(",")

      if s == "" :
        return []

      elif f > -1:
        count_a +=1
        a = line[f+1]
        sum_a += int(a)
    # rmr to use python3
    return int(m), sum_a/count_a

def main():
  for i in range (1, 17771):
    x = "/u/downing/cs/netflix/training_set/mv_"+str(i).zfill(7)+".txt"
    
    opn = open (x, "r")
    s, y = netflix_read(opn)
    
    print (s, round(y, 1))
    opn.close()
main()
