def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    x = 0
    y = 0
    z = 0
    while x < len(list1):
        if list1[x] == 1:
            y += 1
        else:
            z += 1
        x += 1
    return [y, z]
print(main([0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1]))