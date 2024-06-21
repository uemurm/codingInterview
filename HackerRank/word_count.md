# Word Count Tool

Determine the number of valid words in a given string s. A valid word contains at least 3 characters with only alphanumeric characters (i.e., the numbers 0-9, letters A-Z in either case), at least one vowel ('a', 'e', 'i', 'o', 'u'), and at least one consonant.

# Example

Suppose s = "This is an example string 234".

| Word    | Is Valid | Reason                                                  |
| ------- | -------- | ------------------------------------------------------- |
| This    | Yes      | At least 3 characters, contains a vowel and a consonant |
| is      | No       | Less than 3 characters                                  |
| an      | No       | Less than 3 characters                                  |
| example | Yes      | At least 3 characters, contains a vowel and a consonant |
| string  | Yes      | At least 3 characters, contains a vowel and a consonant |
| 234     | No       | Does not contain a vowel or a consonant                 |

# Function Description

Create the function countValidWords in Python.

countValidWords has the following parameter(s):
  string s: a string to analyze

# Returns

  int: the number of valid words in s

# Constraints

- 1 <= length of s <= 10^5
- s consists of all available ASCII characters.

# Input Format For Custom Testing

The first line contains a string, s.

# Sample Case 0

## Sample Input

This is Form16 submis$ion date

## Sample Output

3

## Explanation

Only 'This', 'Form16', and 'date' are valid words. Since 'is' only
contains 2 characters and 'submis$ion' has an invalid character, they
are not valid.

# Sample Case 1

## Sample Input

Bob wins the game

## Sample Output

4

## Explanation

All the words are valid.
