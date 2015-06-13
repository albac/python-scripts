
def fibonacci():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

import types
if type(fibonacci()) == types.GeneratorType:
        print "Good, The fib function is a generator."

counter = 0
for n in fibonacci():
    print n
    counter += 1
    if counter == 10:
        break
