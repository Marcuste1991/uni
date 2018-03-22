# define
a = 22
b = 3
x = 77

# part 1 --
a = x
a = a + 1
print(a, x)

# part 2
a = x
x = a
print(a, x)

# part 3
x = x + 1
x = x
print(a, x)

# part 4
a, x = x, a
a, x = x, a
print(a, x)

# part 5
z = x
a = z
x = a
print(a, x, z)

# text
s = "Guten Morgen"

print(s[-3:])

# Text addition
s = 'Accelerate'
t = 'Adventure'

x = s[0:3] + t[3:]
print(x)
print('h' in s)
print('e' in s)
print(s.find('e'))

# find second zip string in text if no 2 -> -1
text1 = 'all zip files are zipped'
text2 = 'all zip files are compressed'


print(text1.find('zip', text1.find('zip') + 1))
print(text2.find('zip', text2.find('zip') + 1))

