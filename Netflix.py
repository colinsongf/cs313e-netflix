def netflix_read (r) :
    for line in r:
      line = line.strip()
      if line == "" :
        return
      return line

def netflix_print (w, v) :
    w.write(str(v) + "\n")

def netflix_solve (r, w) :
    cashe = []
    l = " "
    while True :
        a = netflix_read(r)        
        if not a :
          for i in range (len(cashe)):
            netflix_print(w, cashe[i])
          return
        else:
          f = a.find(":")
          if f < 0 :
            cashe.append(3)
          else:
            
            cashe.append(a)


import sys

netflix_solve(sys.stdin, sys.stdout)