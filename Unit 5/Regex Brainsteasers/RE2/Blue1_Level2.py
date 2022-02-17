import sys; args = sys.argv[1:]

idx = int(args[0])-40

myRegexLst = [
    r"/^[x.o]{64}$/i", # 40
    r"/^[xo]*\.[xo]*$/i", # 41
    r"/^(\.[xo.]*|[xo.]*\.|x+o*\.[xo.]*|([xo.]*\.o*x+))$/i", # 42
    r"/^.(..)*$/s", # 43
    r"/^0([01][01])*$|^1[01]([01][01])*$/", # 44
    r"/\w*(a[eiou]|e[aiou]|i[eaou]|o[eiau]|u[eioa])\w*/i", # 45
    r"/^(1?0)*1*$/", # 46
    r"/^(a|\b[bc]*a?[bc]*)$/", #47
    r"/^(\b[bc]*((a[bc]*){2})*[bc]*)$/", # 48
    r"/^(2[02]*)*((1[02]*){2})*\b$/" # 49
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])
# Tanmai Kalisipudi 2 2023