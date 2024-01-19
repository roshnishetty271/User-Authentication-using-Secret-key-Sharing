from __future__ import division
from random import SystemRandom


primes = []


def generate_random_polynomial(degree, secret, primeBound):
    """
    Generates a random polynomial.
    degree: threshold of the secret scheme
    secret: f(0), i.e. the secret we are sharing
    primeBound: the upperbound on the coefficients, it is chosen by
                select a "just large enough" prime number
    """
    if degree < 0:
        raise Exception('Degree has to be >= 0.')

    polyCoefficients = []
    polyCoefficients.append(secret)
    systemRandom = SystemRandom()

    for i in range(degree):
        randomCoefficient = systemRandom.randint(0, primeBound-1)
        polyCoefficients.append(randomCoefficient)

    return polyCoefficients


def calculate_polynomial_points(coefficients, num_points, primeBound):
    """ Calculates the first n polynomial points,
        and return them in the form of
        [ (1, f(1)), (2, f(2)), ... (n, f(n)) ]
    """
    points = []

    for x in range(1, num_points + 1): # starting at 1 because we've already got f(0)
        y = coefficients[0]

        for i in range(1, len(coefficients)):
            exp = (long(x)**i) % primeBound # raise x to its ith exponent
            term = (coefficients[i] * exp) % primeBound # multiply by the coefficient and then mod by primeBound
            y = (y + term) % primeBound

        points.append((x, y))

    return points


def lagrange_interpolation(x, x_values, y_values, prime):
    """
    From https://en.wikipedia.org/wiki/Lagrange_polynomial#Definition
    Given a set of k+1 data points, as (x0, y0)... then:
    L(x) := Sum j=0 -> k (y_j * P_j(x))
    P_j(x) := Pi of 0 <= m <= k, m =/= j ((x - x_m) / (x_j - x_m))
    """
    if not len(x_values) == len(y_values):
        raise "Number of X and Y values must be the same"

    k = len(x_values)
    result = 0

    for j in range(k):
        result = (prime + result + poly(j, k, x, x_values, prime) * y_values[j]) % prime

    return result


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def mod_inverse(k, prime):
    k = k % prime
    if k < 0:
        r = egcd(prime, -k)[2]
    else:
        r = egcd(prime, k)[2]
    return (prime + r) % prime


def poly(j, k, x, x_values, prime):
    result = []

    for m in range(k):
        if m == j:
            continue

        numerator = (x - x_values[m]) % prime
        denominator = (x_values[j] - x_values[m]) % prime
        p = numerator * mod_inverse(denominator, prime)
        result.append(p)

    product = result[0]
    for i in range(1, len(result)):
        product = product * result[i]

    return product


def toFloat(x, x1, y1):
    x = float(x)
    for i in range(len(x1)):
        x1[i] = float(x1[i])
        y1[i] = float(y1[i])


def calculate_mersenne_primes():
    # both of these from: https://en.wikipedia.org/wiki/Mersenne_prime
    # there are 48 exponents in the list, but this should probably be good enough! (Tested on a 3000 character secret!)
    exponents = \
    [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091]

    for exponent in exponents:
        prime = 1

        for i in range(exponent):
            prime *= 2

        prime = prime - 1
        primes.append(prime)

    return primes


def get_large_enough_prime(values):
    """
    Generate a prime that is JUST large enough than any of the values
    received
    """
    global primes

    # let's not do a crazy amount of work...
    if len(primes) == 0:
        primes = calculate_mersenne_primes()

    maxVal = max(values)

    for prime in primes:
        if prime > maxVal:
            return prime

    raise "No primes could be generated"
