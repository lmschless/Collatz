import sys

def most_outer():
  #number = val
  def outer(number):
    if number > 1:
      collatz(number)
      print(f'Current iteration: {number}')
    else: print(f'The final Number is: {number}')

  def collatz(number):
    try:
      while number > 1:
        if number % 2 == 0:
          return outer(number // 2)
        else: return outer(3 * number + 1) 
    except: 
      print(f'There has been an error with Number: {number}')
    
  number = int(input('Enter a number: '))
  outer(number)

most_outer()
