# average rating per customer



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
  opn = open ("training_set.txt", "r")
  x = collatz_read(opn)
  print(x)
  opn.close()

main()
