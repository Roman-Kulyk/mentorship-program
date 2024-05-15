############################
text = 'hello'
result = iter(text)

while True:
    try:
        print(next(result))
    except StopIteration:
        break

#############################
text = 'hello'
for i in text:
    print(i)

#############################
class Iterator():
    def __init__(self, number_low, number_high, step):
        self.number_low = number_low
        self.number_high = number_high
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number_low >= self.number_high:
            raise StopIteration
        else:
            self.number_low += self.step
            return self.number_low - self.step
        
it1 = Iterator(0, 10, 1)
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))

for i in it1:
    print(i)

it2 = Iterator(5, 20, 4)

for i in it2:
    print(i)
#############################
def generator(n):
    number = 0
    while number < n:
        yield number
        number += 1

gen = generator(10)
print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)