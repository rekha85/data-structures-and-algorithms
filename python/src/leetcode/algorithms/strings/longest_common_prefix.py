def longest_common_prefix(strings: list[str]) -> str:
    """Return the longest prefix shared by every string."""
    if not strings:
        return ""

    prefix = strings[0]

    for current in strings[1:]:
        common_length = 0
        while (
            common_length < len(prefix)
            and common_length < len(current)
            and prefix[common_length] == current[common_length]
        ):
            common_length += 1

        prefix = prefix[:common_length]
        if not prefix:
            return ""

    return prefix


def main() -> None:
    count = int(input("Enter the number of strings: "))
    strings = input("Enter the strings separated by spaces: ").split()

    if len(strings) != count:
        raise ValueError(f"Expected {count} strings, but received {len(strings)}")

    result = longest_common_prefix(strings)
    print(f"Prefix: {result}")


if __name__ == "__main__":
    main()
