import sys

s = sys.argv[1]

print(s[2])
print(s[4])
print(len(s))
print(s[0])
print(s[-1])
print(s[-2])
print(s[3:8])
print(s[-5:])
print(s[2:])
print(s[::2])
print(s[1::3])
print(s[::-1])
print(s.find(" "))
print(s[:-1])
print(s[1:])
print(s.lower())
print(s.split())
print(len(s.split()))
print([char for char in s])
print(''.join(sorted(s)))
print(s.split()[0])
print(s == s[::-1])

