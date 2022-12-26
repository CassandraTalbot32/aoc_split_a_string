a = 'vJrwpWtwJgWrhcsFMMfFFhFp'

letter_list = list(a)

#print(letter_list)

#def split(letter_list, n):
   # b = letter_list[:n]
   # c = letter_list[n:]

#print(b)
#split the string in half by dividing by 2
length = len(letter_list)
middle_index = length//2

#assign to b variable everything before the middle index
b = letter_list[:middle_index]

#print(b)
#assign to c variable everything after the middle index 
c = letter_list[middle_index:]

print(c)
