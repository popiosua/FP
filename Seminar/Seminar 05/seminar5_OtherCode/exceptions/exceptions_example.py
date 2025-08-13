import math


def verify_if_prime(x: int) -> bool:
    if x < 1:
        raise ValueError("Numarul nu poate fi negativ.")
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def test_prime():
    assert (not verify_if_prime(12))
    assert (not verify_if_prime(1))
    assert (not verify_if_prime(35))
    assert (not verify_if_prime(4))
    assert (not verify_if_prime(121))
    assert (not verify_if_prime(9))

    assert (verify_if_prime(2))
    assert (verify_if_prime(3))
    assert (verify_if_prime(5))
    assert (verify_if_prime(23))
    assert (verify_if_prime(19))
    assert (verify_if_prime(31))
    assert (verify_if_prime(101))

    try:
        verify_if_prime(-213)
        assert False
    except ValueError:
        assert True

test_prime()
