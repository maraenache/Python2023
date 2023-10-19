#ex1----the greatest common divisor of multiple numbers read from the console---
import math
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def ex1():
    numbers = input("Enter the numbers> ")
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]

    if len(numbers) < 2:
        print("Enter at least two numbers")
    else:
        result = numbers[0]
        for i in range(1, len(numbers)):
            result = gcd(result, numbers[i])
        print(f"The gcd is {result}")

ex1()


#ex2---how many vowels are in a string

def numberOfVowels(str):
    number_of_vowels = 0
    vowels = 'aeiou'
    for char in str:
        if char in vowels:
            number_of_vowels += 1
    return number_of_vowels

def ex2():

    string = input("Enter a string> ")
    vowel_count = numberOfVowels(string)
    print(f"The number of vowels in the string is {vowel_count}")

#ex2()

#ex3---number of occurrences of the first string in the second string

def ex3():

    first_string = input("Enter the first string> ")
    second_string = input("Enter the second string> ")

    number_of_occurrences = second_string.count(first_string)

    print(f"The number of occurrences of the first string in the second is: {number_of_occurrences}")

#ex3()


#ex4--converts a string of characters written in UpperCamelCase into lowercase_with_underscores
def camel_to_snake(camel_string):

    snake_string = camel_string[0].lower()

    for char in camel_string[1:]:
        #daca e majuscula
        if char.isupper():
            #ad _ si litera mica corespunzatoare
            snake_string += '_'
            snake_string += char.lower()
        else:
            snake_string += char

    return snake_string

def ex4():
    input_camel_string= input("Enter a string (UpperCamelCase)> ")

    snake_string = camel_to_snake(input_camel_string)

    print(f"The string in snake_case: {snake_string}")

#ex4()

#ex5---the string obtained by going through the matrix in spiral order
def spiral_matrix(matrix):

    if not matrix or not matrix:
        return ''

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    #marginile matricei
    top = 0
    bottom = rows - 1
    left = 0
    right = cols-1

    while top <= bottom and left <= right:
        #parcurg randul de sus si cresc ingustez matricea, eliminand randul de sus
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        for i in range(right, left-1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom, top-1, -1):
            result.append(matrix[i][left])
        left += 1

    return result


def ex5():

    matrix = [
        ['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p']
    ]
    result = spiral_matrix(matrix)

    print(result)

#ex5()


#---ex6 a function that validates if a number is a palindrome

def is_palindrome(number):
    # number->string
    num_str = str(number)
    # string==reverse
    return num_str == num_str[::-1]


def ex6():

    number = int(input("Enter a number> "))

    if is_palindrome(number):
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")


#ex6()

#ex7---a function that extract a number from a text
def extract_first_number(text):
    number = ""
    found_number = False

    for char in text:
        #parcurg textul, cand am intalnit o cifra setez found_number la True,
        # si la prima litera daca am gasit un numar ies
        if char.isdigit():
            number += char
            found_number = True
        elif found_number:
            break

    return int(number) if number else None


def ex7():
    text = input("Enter the text> ")
    number = extract_first_number(text)

    if number is not None:
        print(f"The (first) number in your text is {number}")
    else:
        print("The text doesn't contain any numbers")

#ex7()

#ex8---a function that counts how many bits with value 1 a number has

def count_set_bits(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count


def ex8():
    number = int(input("Enter a number: "))
    ones_count = count_set_bits(number)
    print(f"The number of set bits in {number} is: {ones_count}")

#ex8()


#sau met2, functia bin()
def count_set_bits(number):
    binary_number= bin(number)
    count_ones = binary_number.count('1')
    return count_ones

def ex8_vplus():
    number = int(input("Enter a number: "))
    ones_count = count_set_bits(number)
    print(f"The number of set bits in {number} is: {ones_count}")

#ex8_vplus()



#ex9---a function that determine the most common letter in a string
def most_common_letter(text):

    text = text.lower()
    frequency = [0] * 26

    for char in text:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
        else:#nu e litera
            continue

        frequency[index] += 1

    max_frequency = max(frequency)
    most_common_index = frequency.index(max_frequency)
    most_common_character = chr(most_common_index + ord('a'))

    return most_common_character, max_frequency


def ex9():

    text = input("Enter a string> ")
    common_letter, frequency = most_common_letter(text)

    print(f"The most common letter '{common_letter}' (number of occurences: {frequency})")

#ex9()

#ex10---a function that counts how many words exists in a text
def count_words_in_text(text):
    text = text.split()
    number_of_words = len(text)
    return number_of_words


def ex10():
    user_text = input("Enter the text> ")
    word_count = count_words_in_text(user_text)
    print(f"The text has {word_count} words")

#ex10()

