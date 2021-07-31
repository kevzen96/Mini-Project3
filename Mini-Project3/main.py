import random
target = random.randint(0,10)
count = 0
while True:
  n = int(input("Enter a number between 0-10: "))
  count += 1
  if n < target :
    print("The number is too low")
  elif n > target:
    print("The number is too high")
  else:
    print("----------You Win---------")
    break
print("You try %d times" %count)
