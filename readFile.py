import string
def collatz_read (r) :
    s = r.readline()
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
    return sum/count

def main():

  for i in range (1, 10):
    x = ""
    x = "mv_"+"000000"+str(i)+".txt"
    
    opn = open ("x", "r")
    y = collatz_read(opn)
    print(y)
    opn.close()

main()