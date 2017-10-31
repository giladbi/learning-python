"""
Pythagorean theorem, which states that in a right-angled triangle,
the sum of squares of the legs of the triangles is equal to the square of the hypotenuse. 
Pythagorean triples are any three positive integers a, b and c that such that a² + b² = c².
Here is a program that finds all the Pythagorean triples whose members are not greater than
the provided limit.
"""

import time
 
 
def count(limit):
    result = 0
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            for c in range(b + 1, limit + 1):
                if c * c > a * a + b * b:
                    break
 
                if c * c == (a * a + b * b):
                    result += 1
    return result
 
 
if __name__ == '__main__':
    start = time.time()
    result = count(10)
    duration = time.time() - start
    print(result, duration)
     
#Output: