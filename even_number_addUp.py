#first solution
even_sum = 0

for number in range(2, 101, 2):
  even_sum += number
print(even_sum)

#second solution
total2 = 0
for number in range(1, 101):
  if number % 2 == 0:
    total2 += number
print(total2)
