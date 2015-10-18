import sys
# filename = sys.argv[-1]
filename = "wordlist.txt"
file = open(filename)

def chains():
  words = []
  graph = {}
  maxes = 1
  mid  = 0
  
  #Grab words from wordlist and put them in list
  for word in file:
    words.append(word)  
    #finds largest word length and stores it, allows to know what the longest chain could be
    if len(word)-2 > maxes:
      maxes = len(word)-2

  words.sort()
  words.sort(lambda x,y: cmp(len(x), len(y))) 

  #We want to iterate until we hit somewhere in the middle element for efficiency's sake and we only need 3
  for i in range(0, len(words)/2): 
    list = []
    list.append(words[i])
    for j in range(i, len(words)):
      if comparer(words[i], words[j]) == True:
        i = j
        list.append(words[j])
    if len(list) == maxes:
       for x in list:
        print x

#Adapted from code found on stackoverflow and Github to compare words
def comparer(w1, w2):
  w1 = ''.join(sorted(w1))
  w2 = ''.join(sorted(w2))

  if len(w1)==len(w2):
    return False
  elif abs(len(w1)-len(w2)) == 1:
    w1 = sorted(w1)
    w2 = sorted(w2)

    if len(w1)+1 == len(w2):
      matched = 0
      w1temp = w1
      w2temp = w2

      for i in range(1, len(w1temp)):
        if w1temp[i] == w1temp[i-1]:
          w1temp[i] = ''
     
      for i in range(1, len(w2temp)):
        if w2temp[i] == w2temp[i-1]:
          w2temp[i] = '' 
     
      for letterin1 in w1temp:
        found = False

        for letterin2 in w2:
          if letterin1 == letterin2:
            found = True

        if found == True:
          matched = matched + 1

      if matched == len(w1temp):
        return True
      else:
        return False
  else:
    return False

def main(argv):
  chains()

if __name__ == '__main__':
  main(sys.argv)