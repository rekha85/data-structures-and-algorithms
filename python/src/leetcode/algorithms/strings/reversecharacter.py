def reverseChar(s: str) -> str:
    characters = list(s)
    left, right = 0, len(characters) - 1

    while left < right:
        while left < right and not characters[left].isalpha():
            left += 1

        while left < right and not characters[right].isalpha():
            right -= 1

        characters[left], characters[right] = characters[right], characters[left]
        left += 1
        right -= 1

    return "".join(characters)

def main() -> None:
    text = input("Enter a string to reverse: ")
    print(reverseChar(text))

if __name__ == "__main__":
    main()

