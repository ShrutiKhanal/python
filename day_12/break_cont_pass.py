#Break statement
vowels = ["a", "e", "i", "o", "u"]

for vowel in vowels:
    if vowel == 'i':
        break
    print(vowel)


count = 0
while True:
    if count == 10:
      break
    print(count)
    count += 1


##Continue statement

vowels = ["a", "e", "i", "o", "u"]

for vowel in vowels:
    if vowel == 'i':
        continue
    print(vowel)

count = 0
while count < 10:
    if count == 5:
      continue
    print(count)  #Result 0, 1, 2, 3, 4, 6, 7, 8, 9
    count += 1

##Pass statement is used when we know that we need a function or class in future but the logic is unclear currently.
#future ma code rakhnu cha or code add garnu cha bhaney pass lekhni

def addition():
    pass #logic is added here in future

class A:
    pass #Logic is added in future