import math
import string
def collatz_read (r) :
    
    s = r.readline()
    z = s.find(":")
    if z > -1:
        m = s[:z]
    sum = 0
    count = 0
    for line in r:
      line = line.strip()
      a = ""
      f = line.find(",")
      if s == "" :
        return []
      elif f > -1:
        count +=1
        a = line[f+1]
        
        sum += int(a)
    return int(m), sum/count

def main():
  
  for i in range (1, 17771):
    x = ""
    x = "/u/downing/cs/netflix/training_set/mv_"+str(i).zfill(7)+".txt"
    
    opn = open (x, "r")
    s, y = collatz_read(opn)
    
    print (s, round(y,1))
    opn.close()

main()
