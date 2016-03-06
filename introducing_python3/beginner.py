#
# Answers for O'REILLY's "Introducing Python 3" review problems 
#
'''
# 4-4
even = [x for x in range(10) if x%2 == 0]
print(even)


# 4-5
squares = {x:x*x for x in range(10)}
print(squares)


# 4-6
odd = {x for x in range(10) if x%2 == 1}
print(odd)


# 4-7
generater = (x for x in range(10))
for i in generater:
  print ('Got ' + str(i))


# 4-9
def get_odds():
  for x in [x for x in range(10) if x%2 == 1]:
    yield x

count = 0
for i in get_odds():
  count += 1 
  if count == 3: 
    print(i)
    break


# 4-10
def test(func):
  def new_func(*args, **kwargs):
    print('start')
    func(*args, **kwargs)
    print('end')
  return new_func

@test
def my_add(a, b):
  print(a + b)

my_add(2,3)


# 4-11
class OopsException(Exception):
  pass
#raise OopsException('Caught an oops')
try:
  raise OopsException
except OopsException:
  print('Caught an oops')


# 4-12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)

'''
