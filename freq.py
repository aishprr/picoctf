import optparse

parser = optparse.OptionParser()

parser.add_option('-s', '--string', action="store", dest="string",
                    help="string to freq", default="spam")

options, args = parser.parse_args()

alphabets = {}

def alphaFreq(s):
  
  for c in s:
    if c in alphabets:
      alphabets[c] = alphabets[c] + 1
    else:
      alphabets[c] = 1
 

if __name__ == '__main__':

  alphaFreq(options.string);
  print alphabets


