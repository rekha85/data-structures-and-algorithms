def reverse_string(text: str) -> str:
    """Return the words in ``text`` in reverse order."""
    strings = text.split()
    reversed_strings = []
    output_strings = []

    # Negative indexes are dynamic: -1 is the last item, then -2, and so on.
    for index in range(len(strings) - 1, -1, -1):
        reversed_strings.append(strings[index])

    print(" ".join(reversed_strings))

    # Without index - Use reverse string function
    for str in reversed(strings):
        output_strings.append(str)

    print("output:"," ".join(reversed_strings))

    return " ".join(reversed_strings)

def main() -> None:
    """Read a string and print its words in reverse order."""
    text = input("Enter a string to reverse: ")
    print(reverse_string(text))

if __name__ == "__main__":
    main()
