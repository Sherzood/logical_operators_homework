def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    a1=a%10
    a//=10
    a2=a%10
    a3=a//10
    sum_digits=a1+a2+a3
    return sum_digits%2==1