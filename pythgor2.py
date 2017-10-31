"""
Pythagorean theorem, which states that in a right-angled triangle,
the sum of squares of the legs of the triangles is equal to the square of the hypotenuse. 
Pythagorean triples are any three positive integers a, b and c that such that a² + b² = c².
Here is a program that finds all the Pythagorean triples whose members are not greater than
the provided limit.
"""



import time
import pyximport; pyximport.install()
import pythagorean_triples
 
 
def main():
    start = time.time()
    result = pythagorean_triples.count(1000)
    duration = time.time() - start
    print(result, duration)
 
 
if __name__ == '__main__':
    main()