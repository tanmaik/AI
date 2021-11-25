### Ben Zhang
### Period 2
### 11/21/13

from random import randint

class Node(object):
  def __init__(self, value):
    self.value = value
    self.children = {}
    
  def __repr__(self):
    self.print()
    return ''
  
  def print(self, stng):
    for key in self.children:
      if key == '$':
        print(stng)
      else:
        self.children[key].print(stng+key)
        
  
  def display(self):
    if self.value == '$':
      return
    print('---Node---')
    print('self.value is', self.value)
    print('self.children: [', end = '')
    
    for key in self.children:
      if key != '$':
        print(key, sep = '', end = ', ')
    print(']')
    print('----------')
    
    for char in self.children:
      (self.children[char]).display()
      
  def insert(self, stng):
    if len(stng) == 0: # code from github, please do not submit as own work
      self.children['$'] = Node('$')
    else:
      if (stng[0] not in self.children):
        self.children[stng[0]] = Node(stng[0])
      self.children[stng[0]].insert(stng[1:])
  
  def search(self, stng):
    #print('searching for', stng)
    
    if len(stng) == 0:
      for key in self.children:
        if key == '$':
          return True
    else:
      for key in self.children:
        if key == stng[0]:
          if self.children[key].search(stng[1:]):
            return True
            
    return False
  
  def fragmentInDictionary(self, stng):
    if len(stng) == 0:
      return True
    #print(stng) # code from github, please do not submit as own work
    for key in self.children:
      if key == stng[0]:
        #print(key + ' is ' + stng[0])
        if self.children[stng[0]].fragmentInDictionary(stng[1:]):
          return True
    return False



FILE = "ghostdict.txt"

def main():
  root = getWords(FILE)
  printDirections()
  stng = ''
  ##print('Trie:')
  ##root.print('')
  ##print('End of Trie')

  #print(root.search('zodiac'))
  
  while True:
    stng = requestAndCheck('Human', root, stng)
    stng = requestAndCheck('Computer', root, stng)
    
  #print(stng)

  #word = spellWordFromString(root, "na")
  #print(word)

def printDirections():
  print("This code was written by Ben Zhang, TJHSST class of 2015. No cheating, please!")
  print("Welcome to GHOST!")
  print("Take a card, any card")
  print("and of course, enjoy your stay!")
  print("Just kidding. Enter your letters. Try to win.")

def getWords(filename):
  trie = Node("*")
  dictionary = open(filename)
  for word in dictionary:
    if len(word) >= 5:
      #print(word, len(word))
      trie.insert(word.lower().strip())
  dictionary.close()
  return trie

def isComputer(player):
  if player == 'Computer':
    return True
  return False

def requestAndCheck(player, root, stng):
  if not isComputer(player):
    stng += input(player + ', enter character! ').lower()[0]      # code provided
    print('Player has chosen. Word is now:', stng, '.', sep = '') # open source on
    if root.search(stng) == True:                                 # github; should not be submitted
      print("----------------------------------------------")     # as your own work.
      print(player, "loses because (s)he is bad. Also,", stng, "is a word.") # :)
      print("---The game is over. Awwwwwwwwwwwwwwwwwww. ---")
      exit()
    if root.fragmentInDictionary(stng) == False:
      print("----------------------------------------------")
      print(player, " loses because (s)he is bad. Also, '", stng, "'\n does not begin any word.", sep = '')
      print('[The computer\'s word was ', '"', spellWordFromString(root, stng[0:-1]), '".]', sep = '')
      print("---The game is over. D'awwwwwwwwwwwww...   ---")
      exit()
    return stng
  else:
    stng += chooseLetter(getDownDesignatedString(root, stng))
    print('Computer has chosen. Word is now:', stng, '.', sep = '')
    if root.search(stng) == True:
      print("----------------------------------------------")
      print(player, "loses because it spelled", stng, ".")
      print("---The game is over. Hm. I wonder why.     ---")
      exit()
    if root.fragmentInDictionary(stng) == False:
      print("----------------------------------------------")
      print(player, " loses because it is bad. Also, '", stng, "'\n does not begin any word. What?", sep = '')
      print("---The game is over. Wuhuhuhuhuhuh.        ---")
      exit()
    return stng

def getDownDesignatedString(root, stng):
  node = root
  stringcpy = stng
  #print('hi')
  while len(stringcpy) > 0:
    #print('stringcpy:',stringcpy,'>')
    #print('stng:',stng,'>')
    if node.children[stringcpy[0]].value == '$':
      print('Failed to travel down trie along path:', stng)
      return
    node = node.children[stringcpy[0]]
    #print('Node: ' +node.value + ' >')
    stringcpy = stringcpy[1:]
  
  return node

def chooseLetter(node):
  k = None
  for key in node.children:
    #print("key:",key,'>')
    if (k == None) or (randint(0, 3) == 0):
      if (key != '$'):
        k = key
  #print('letter chosen:', k)
  return k

def spellWordFromString(root, stng):

  word = stng[:]
  if root.fragmentInDictionary(stng):
    currentnode = getDownDesignatedString(root, stng)
    #print('currentnode:', currentnode.value, '>')
  else:
    return ("<ERROR: Unable to spell word from string", stng ,">")
  while word[-1] != '$':
    k = chooseLetter(currentnode)
    if k == None:
      word = word + currentnode.value
      break
    if k != '\n':
      word = word + currentnode.children[k].value
    currentnode = currentnode.children[k]

  #print('stng:',stng,'>')
  #print('word:',word,'>')
  return word[0:-1]
    
  #return ("<ERROR: Unable to spell word from string", stng ,">")



  
if __name__ == '__main__':
    main()