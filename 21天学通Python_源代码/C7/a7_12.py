def grade(sum):
    """
    >>> grade(100)
    '优秀'
    >>> grade(80)
    '良'
    >>> grade(65)
    '合格'
    >>> grade(10)
    '不合格'
    """
    if sum > 90:
        return '优秀'
    if sum > 80:
        return '良'
    if sum > 60:
        return '合格'
    if sum < 60:
        return '不合格'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
