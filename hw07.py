#V00700624 Jasmine Roland

# Constants
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

# Functions
def is_alpha(s: str) -> bool:
    """Returns True if all characters in the string are ASCII letters, False otherwise."""
    for char in s:
        if char not in ASCII_LOWERCASE and char not in ASCII_UPPERCASE:
            return False
    return True

def is_digit(s: str) -> bool:
    """Returns True if all characters in the string are ASCII decimal digits, False otherwise."""
    for char in s:
        if char not in DECIMAL_DIGITS:
            return False
    return True

def to_lower(s: str) -> str:
    """Converts all uppercase ASCII letters in the string to lowercase."""
    result = ""
    for char in s:
        if char in ASCII_UPPERCASE:
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_upper(s: str) -> str:
    """Converts all lowercase ASCII letters in the string to uppercase."""
    result = ""
    for char in s:
        if char in ASCII_LOWERCASE:
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def find_chr(s: str, c: str) -> int:
    """Returns the index of the first occurrence of character c in string s, or -1 if c is not found or not of length 1."""
    if len(c) != 1:
        return -1
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1

def find_str(s: str, sub: str) -> int:
    """Returns the index of the first occurrence of substring sub in string s, or -1 if sub is not found."""
    len_sub = len(sub)
    for i in range(len(s) - len_sub + 1):
        if s[i:i + len_sub] == sub:
            return i
    return -1

def replace_chr(s: str, old: str, new: str) -> str:
    """Replaces all occurrences of character old with character new in string s."""
    if len(old) != 1 or len(new) != 1:
        return ""
    result = ""
    for char in s:
        if char == old:
            result += new
        else:
            result += char
    return result

def replace_str(s: str, old: str, new: str) -> str:
    """Replaces all occurrences of substring old with substring new in string s."""
    if old == "":
        return new.join(s) + new
    result = ""
    i = 0
    while i < len(s):
        if s[i:i + len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result
