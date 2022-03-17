def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    a1=a%10
    a//=10
    a2=a%10
    a//=10
    a3=a%10
    a//=10
    a4=a%10
    a5=a//10
    return a1<a2 and a2<a3 and a3<a4 and a4<a5