import re
word = 'fubar'
regexp = re.compile(r'ba[rzd]')
if regexp.search(word):
  print('matched')