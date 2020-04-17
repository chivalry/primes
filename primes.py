def is_prime(num: int) -> bool:
    """Uses early prime facts to determine primacy more quickly."""
    if not isinstance(num, int) or num <= 0:
        raise ValueError('Error: Only positive integers can be prime')
    if num in [2, 3, 5, 7]:
        return True
    if num < 2 or num % 2 == 0 or num == 9:
        return False
    if num % 3 == 0:
        return False
    root = int(num ** 0.5)
    fact = 5
    while fact <= root:
        if num % fact == 0 or num % (fact + 2) == 0:
            return False
        fact += 6
    return True

class PrimeFinder:
    """A dynamic programming singleton implementation of a prime finder."""

    def __new__(cls, *args, **kwargs):
        """Create the singleton object if it doesn't exist, just return it otherwise."""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.found_primes = []
        return cls.instance

    def is_prime(self, num: int) -> bool:
        """Use existing function, but store primes as we find them."""
        if not isinstance(num, int) or num <= 0:
            raise ValueError('Error: Only positive integers can be prime')
        if self.found_primes and num in self.found_primes:
            return True
        if self.found_primes and num < max(self.found_primes):
            return False
        is_p = is_prime(num)
        if is_p:
            self.found_primes.append(num)
        return is_p

if __name__ == '__main__':
    pf = PrimeFinder()
    for i in range(1, 11):
        pf.is_prime(i)
    print(pf.found_primes)
    pf2 = PrimeFinder()
    print(pf2.found_primes)
