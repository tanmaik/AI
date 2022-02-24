import sys; args = sys.argv[1:]

idx = int(args[0])-50

myRegexLst = [
    r"/\w*(\w)\w*\1\w*/i",
    r"/\w*(\w)\w*(\1\w*){3}/i",
    r"/^(0[10]*0|1[10]*1|[01])$/",
    r"/\b(?=\w*cat)\w{6}\b/i", 
    r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i", 
    r"/\b(?!\w*cat)\w{6}\b/i",
    r"/\b((\w)(?!\w*(\2)))+\b/i",
    r"/^(?!.*10011)[01]*$/",
    r"/(?=\w*([aeiou])(?=[aeiou])(?!\1))\w+/i",
    r"/^(?!.*1(0|1)1)[01]*$/"
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])
# Tanmai Kalisipudi 2 2023