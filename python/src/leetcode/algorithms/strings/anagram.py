def isAnagram(firstStr: str, secondStr: str) -> bool:

    if len(firstStr) != len(secondStr):
        return False

    return sorted(firstStr.replace(" ", "")) == sorted(secondStr.replace(" ", ""))

def main() -> None:

    firstStr = input("Enter first string: ")
    secondStr = input("Enter second string: ")

    print(isAnagram(firstStr, secondStr))

if __name__ == "__main__":
    main()