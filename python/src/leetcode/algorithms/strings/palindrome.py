def is_palindrome(text: str) -> bool:
    """Return whether ``text`` is a palindrome.

    Comparison ignores non-alphanumeric characters and is case-insensitive.
    Unicode-aware ``isalnum`` and ``casefold`` make the comparison suitable
    for text beyond ASCII.
    """
    left, right = 0, len(text) - 1

    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1

        if text[left].casefold() != text[right].casefold():
            return False

        left += 1
        right -= 1

    return True

def main() -> None:
    """Read text from the console and print whether it is a palindrome."""
    text = input("Enter a string: ")
    print(is_palindrome(text))


if __name__ == "__main__":
    main()
