def count_vowels(s):
    v = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in v:
            count += 1
    return count

string = input("Enter a string: ")
print("The number of vowels:",count_vowels(string))
