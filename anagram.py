def checkAnagram(input1, input2):
    #slice parameter strings into lists
    list1 = []  
    list1[:] = input1
    list2 = []  
    list2[:] = input2

    #remove spaces
    clean1 = []
    clean2 = []
    for i in range(len(list1)):
      if not list1[i] == " ":
        clean1.append(list1[i])
    for i in range(len(list2)):
      if not list2[i] == " ":
        clean2.append(list2[i])

    #compare by length
    size1 = len(clean1)
    size2 = len(clean2)
    if size1 != size2:
        return False

    #compare by contents
    clean1 = sorted(clean1)
    clean2 = sorted(clean2)
    if clean1 != clean2:
      return False
    else:
      return True

#create function to format result
def formatAnagram(s1, s2):
    print("String 1: ", s1)
    print("String 2: ", s2)
    if(checkAnagram(s1, s2)):
        print("** These are anagrams! :) **")
    else:
        print("** These are not the anagrams you are looking for. **")
    print("\n")

#call functions to print in console
formatAnagram("anagram", "nag a ram")
formatAnagram("eleven plus two", "twelve plus one")
formatAnagram("Hello!!", "Goodbye")
