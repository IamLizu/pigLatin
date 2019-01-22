print 'Welcome to the Pig Latin Translator!'
pyg = 'ay'

inp = raw_input('Enter a word: ')

if len(inp) > 0 and inp.isalpha():
  word = inp.lower()
  first = word[0]
  n_word = word + first + pyg
  n_word = n_word[1:len(n_word)]
  print n_word
else:
    print 'Invalid input!'
