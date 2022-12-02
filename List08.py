def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    x = 0
    while x < len(fruits):
        if fruits[x] == "apple":
            fruits.pop(x)
        x += 1
    return fruits
print(main(["apple", "apple", "apple", "apple", "kiwi"]))