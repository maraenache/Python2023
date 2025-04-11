import math

#ex1---a function to return a list of the first n numbers in the Fibonacci string
def ex1(n):
    a = 1
    b = 1
    fibonacciList = [a, b]

    for i in range(0, n - 2):
        c = a + b
        fibonacciList.append(c)
        a = b
        b = c
    return fibonacciList

#print(ex1(12))

#ex2---a function that receives a list of numbers and returns a list of the prime numbers found in it
def ex2(listOfNumbers):

    listOfPrimeNumbers = []

    for number in listOfNumbers:
        isPrime = True
        if number < 2 or (number % 2 == 0 and number != 2):
            isPrime = False
        for divider in range(3, int(math.sqrt(number) + 1), 2):
            if number % divider == 0:
                isPrime = False
                break
        if isPrime:
            listOfPrimeNumbers.append(number)

    return listOfPrimeNumbers

a=[12,23,44,3,4,5]
#print(ex2(a))

#ex3--- a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a

def ex3(list1, list2):
    intersection = []
    union = []
    aMinusB = []
    bMinusA = []

    for element_from_first_list in list1:
        for element_from_second_list in list2:
            if element_from_first_list == element_from_second_list and intersection.count(element_from_first_list) == 0:
                intersection.append(element_from_first_list)

    for element_from_first_list in list1:
        for element_from_second_list in list2:
            if union.count(element_from_first_list) == 0:
                union.append(element_from_first_list)
            if union.count(element_from_second_list) == 0:
                union.append(element_from_second_list)

    for element_from_first_list in list1:
        found = False
        for element_from_second_list in list2:
            if element_from_first_list == element_from_second_list:
                found = True
        if not found:
            aMinusB.append(element_from_first_list)

    for element_from_second_list in list2:
        found = False
        for element_from_first_list in list1:
            if element_from_second_list == element_from_first_list:
                found = True
        if not found:
            bMinusA.append(element_from_second_list)

    return [intersection, union, aMinusB, bMinusA]


a_set=[1,23,45,33,54]
b_set=[2,22,23,33,54]

#print(ex3(a_set,b_set))


#ex4---function will return the song composed by going through the musical notes
# beginning with the start position and following the moves given as parameter

def ex4(a, b, starting_note_position):
    song = [a[starting_note_position]]
    position = starting_note_position

    for i in range(0, len(b)):
        position = position + b[i]
        if position > len(a) or position < 0:
            position = position % len(a)
        song.append(a[position])

    return song


notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
starting_position = 2

#print(ex4(notes, moves, starting_position))


#ex5---the matrix obtained by replacing all the elements under the main diagonal with 0 (zero)
def ex5(matrix):

    n = len(matrix[0])
    for i in range(0, n-1):
        for j in range(0, n-1):
            if i > j:
                matrix[i][j] = 0
    return matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

#print(ex5(matrix))

#ex6---list containing the items that appear exactly x times in the incoming lists, sau cu zip
def ex6(x, *lists):
    all_numbers = []
    
    x_occurrences_numbers = []

    for element in lists:
        all_numbers += element

    for number in all_numbers:
        if all_numbers.count(number) == x and x_occurrences_numbers.count(number) == 0:
            x_occurrences_numbers.append(number)
    return x_occurrences_numbers


#print(ex6(3, [1, 2, 1], [2, 1, 4], [3, 3, 3, 'a'], ['a', 'a', 7, 7, 7]))

#ex7---return a tuple with 2 elements. (first element - the number of palindrome numbers found in the list,
# the second element - the greatest palindrome number

def is_palindrome(number):
    # number->string
    num_str = str(number)
    # string==reverse
    return num_str == num_str[::-1]


def ex7(list):

    counter=0
    max=0

    for number in list:
        if is_palindrome(number):
            counter += 1
            if number > max:
                max = number
    if max == 0:
        return 0, "nu am gasit niciun palindrom"

    return counter, max

#print(ex7([12, 34, 56]))
#print(ex7([1221,7, 7878, 888,98,90]))


#ex8---

def ex8(x=1, list_of_strings=[], flag=True):
    output_list = []
    for string in list_of_strings:
        char_list = []
        for character in string:
            if (ord(character) % x == 0) == flag:
                char_list.append(character)
        if char_list:
            output_list.append(char_list)
    return output_list

#print(ex8(3,["test", "hello", "lab002"], True))


"""
caracterele care se divid la x pt flag true
caracterele care nu se divid la x pt flag false
"e" - 101
"s" - 115
"e" - 101
"o" - 111
"l" - 108
"l" - 108
"a" - 97
"b" - 98
"0" - 48
"0" - 48
"2" - 50
->obs: daca x are default value, toate de dupa trb sa aiba
"""


#ex9---list of tuples (line, column) each one representing a seat of a spectator which can't see the game

def ex9(seats_matrix):
    number_of_rows = len(seats_matrix)
    number_of_columns = len(seats_matrix[0])

    seats_with_no_visibility = []

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            current_position_height = seats_matrix[row][column]
            good_visibility = True

            for front_row in range(row):  # merg pe rândurile din fata si verific, dar la aceeași coloană
                if seats_matrix[front_row][column] >= current_position_height:
                    good_visibility = False
                    break

            if not good_visibility:
                seats_with_no_visibility.append((row, column))

    return seats_with_no_visibility


game_matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

#print(ex9(game_matrix))

#ex10---returns a list of tuples as follows: the first tuple contains the first items in the lists,
# the second element contains the items on the position 2 in the lists etc

def ex10(*lists):
    max_number_of_elements = max(len(x) for x in lists)
    tuples_lists = []

    for i in range(max_number_of_elements):
        current_tuple = tuple(list[i] if i < len(list) else None for list in lists)
        tuples_lists.append(current_tuple)

    return tuples_lists


#print(ex10([12, 23, 33, 22], [1, 2, 3, 4, 4], [7, 8, 9, 10], ['a', 'b', 'c']))
""" sau  
in loc de asta, current_tuple=tuple(list[i] if i<len(list) else None for list in lists)

for i in range(max_length):
        current_tuple = ()
        for list in lists:
            if i < len(list):
                current_tuple += (list[i],)  
            else:
                current_tuple += (None,) 

        tuples_lists.append(current_tuple)
"""


#ex11 -a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple


def ex11(tuples_list):
    sorted_tuples=sorted(tuples_list, key=lambda list: list[1][2])
    return sorted_tuples


tuples = [
    ('abc', 'bcd'),
    ('abc', 'zza'),
    ('def', 'gfh'),
    ('xyz', 'wxy'),
    ('hij', 'klm')
]
sorted_tuples = ex11(tuples)
#print(sorted_tuples)
#print(ex11([('abc', 'bcd'), ('abc', 'zza')]))

def group_words_by_rhyme(word_list):

    # lista liste, fiecare group are aceeasi rima
    rhyming_groups = []

    # Parcurgeți lista de cuvinte
    for word in word_list:

        rhyme = word[-2:]

        # gasesc grupul corespunzător de rimă din lista, daca exista
        found_group = None
        for group in rhyming_groups:
            if group[0][-2:] == rhyme:
                found_group = group
                break

        # daca nu l-am gasit, fac unul nou
        if found_group is None:
            rhyming_groups.append([word])
        else:
            found_group.append(word)

    return rhyming_groups

word_list = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_words_by_rhyme(word_list)

print(result)