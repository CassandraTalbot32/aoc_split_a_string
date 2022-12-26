a = 'vJrwpWtwJgWrhcsFMMfFFhFp'

letter_list = list(a)

#print(letter_list)

#def split(letter_list, n):
   # b = letter_list[:n]
   # c = letter_list[n:]

#print(b)
length = len(letter_list)
middle_index = length//2

b = letter_list[:middle_index]

#print(b)

c = letter_list[middle_index:]

print(c)
