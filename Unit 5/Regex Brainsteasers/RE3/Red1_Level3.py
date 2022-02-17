import sys; args = sys.argv[1:]

idx = int(args[0])-50

myRegexLst = [
    r"/\w*(\w)\w*\1\w*/i",
    r"/\w*(\w)\w*\1\w*\1\w*\1\w*/i",
    r"/^(0[10]*0|1[10]*1|[01])$/",
    r"/(?=\w*cat\w*\b)\w*(?<=\b\w{6}\b)/i", 
    r"/(?=\w*(bri\w*ing|ing\w*bri)\w*\b)(?=\b\w{5,9}\b)\w*|bring/i",
    r"/(?!\w*cat\w*)(?=\b\w{6}\b)\w*/i",
    r"/\b((\w)(?!\w*(\2)))+\b/i",
    r"/^(?![01]*10011)[01]*$/",
    r"/\b(?=\w*([aeiou])(?=[aeiou])(?!\1))\w*/i",
    r"/^(?![01]*(101|111))[01]*$/"
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])
# Tanmai Kalisipudi 2 2023