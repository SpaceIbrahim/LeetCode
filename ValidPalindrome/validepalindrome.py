import re

def isPalindrome(s: str) -> bool:
    s = re.sub("[!@#$%^&*_+-=~`<>?,./\| ]", "", s).lower()

    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def main():
    
    s = "A man, a plan, a canal: Panama"

    output = isPalindrome(s)

    print(output)


if __name__ == "__main__":
    main()