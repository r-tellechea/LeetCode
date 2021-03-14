# https://leetcode.com/problems/four-divisors/

# Key: n has exactly 4 divisors iff n = p*q, with p != q and p, q primes  or  n = p^3 with p prime
# So we look for a prime p such that p | n, and return False if n/p is not prime and n//p != p^2.

from math import sqrt
    
def four_divisors (n):
    sq = sqrt(n)
    p = 1
    divisors = set([])
    while p < sq + 1:
        if n % p == 0:
            divisors.add(p)
            divisors.add(n // p)
            if len(divisors) > 4:
                return 0
        p += 1
    # If there is no prime in 2 ... sqrt(n) dividing n, there n is prime.
    if len(divisors) == 4:
        return sum(divisors)
    else:
        return 0

class Solution:
    def sumFourDivisors(self, nums) -> int:
        sum_of_four_divisors = 0
        for n in nums:
            sum_of_four_divisors += four_divisors(n)
        return sum_of_four_divisors
