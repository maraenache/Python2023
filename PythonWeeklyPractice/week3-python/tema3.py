# import math

# ex1--- a function that receives as parameters two lists a and b and returns a list of sets containing:
# (A intersected with B, A reunited with B, A - B, B - A)
def ex1(a, b):
    a_set = set(a)
    b_set = set(b)

    union = a_set | b_set
    # union = a_set.union(b)

    intersection = a_set & b_set
    # intersection = a_set.intersection(b)

    a_minus_b = a_set - b_set
    # a_minus_b = a_set.difference(b)

    b_minus_a = b_set - a_set
    # b_minus_a = b_set.difference(a_set)

    return [union, intersection, a_minus_b, b_minus_a]
    # fara [] la return imi return cu par rot (lista1, lista2)

print(ex1([1,2,3,4],[3,4,5]))


# ex2---a function that receives a string and returns a dictionary in which the keys are the characters
# in the character string and the values are the number of occurrences of that character in the given text.
# ex: "Ana has apples."=> dict: {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}

def ex2_v1(string):
    my_dict = {char: string.count(char) for char in string }
    return my_dict

def ex2_v2(string):
    my_dict = dict()
    for char in string:
        my_dict[char] = my_dict.get(char, 0) + 1
    return my_dict


# print(ex2_v2("Ana has apples."))


'''
output_dict=ex2_v1("Ana has apples.")
print(output_dict)

#(pt mine) functia get, imi returneaza valoarea cheii daca o gaseste, altfel al 2 lea param
#ex slide 24/32

# afisarea fiec tuplu/item
for i in output_dict.items():
    print(i)
# afisarea doar a cheilor, sau cu .keys()
for i in output_dict:
    print(i)
# afisarea doar a valorilor
for i in output_dict.values():
    print(i)
'''

#ex3- compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other containers,
# such as dictionaries, lists, sets, etc.)-adica o cheie a dict poate avea ca val un alt dictionar

def ex3(dict1, dict2):

    if set(dict1.keys()).isdisjoint(set(dict2.keys())):
        return False

    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]

        if type(value1) is not type(value2):
            return False

        if isinstance(value1, dict):
            if not ex3(value1, value2):
                return False

        elif isinstance(value1, set):
            if value1 != value2:
                return False

        elif isinstance(value1, list):#!!!
            if len(value1) != len(value2) or sorted(value1) != sorted(value2):
                return False

        elif value1 != value2:
            return False

    return True


dict1 = {'mara': 100, 'dictionar': {'un set': [99, 88, 77, 55]}, 'si o lista': [77, 66]}
dict2 = {'mara': 100, 'si o lista': [66, 77], 'dictionar': {'un set': [88, 77, 99, 55]}}
dict3 = {'mara': 100, 'dictionar': {'un set': [99, 88, 77]}, 'si o lista': [77, 55]}
dict4 = {'mara': 100, 'dictionar': {'un set': [99, 88, 77, 44]}, 'si o lista': [77, 66]}

# print(ex3(dict1, dict2)) # true
# print(ex3(dict1, dict3)) # false
# print(ex3(dict1, dict4)) # false

#ex4--- build_xml_element function receives the following parameters: tag, content, and key-value elements
# Build and return a string that represents the corresponding XML element.
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
# returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
def build_xml_element(tag, content, **elements_dict):
    elements_string = " ".join([f'{key}="{value}"' for key, value in elements_dict.items()])
    xml_element = f'<{tag} {elements_string}>{content}</{tag}>'
    return xml_element
# sa dau ca parametru elemente cheie valoare  nr variabil**


#print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))


#ex5---The validate_dict function that receives as a parameter a set of tuples (that represents validation rules
# for a dictionary that has strings as keys and values) and a dictionary.
# A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end)
# and ends with "suffix".
#ex the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
#  d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.
def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            #folos startswith si endswith - functii built in
            if not value.startswith(prefix) or not value.endswith(suffix):
                return False
            # middle sa nu fie la inceput sau la sfarsit adica sa se regaseasca in secventa,
            # cuprinsa dintre al doilea caracter si penultimul
            if middle not in value[1:-1]:
                return False
        else:
            return False
    return True


#exemplu din tema
rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
my_dict = {"key1": "come inside, it's too cold out", "key2": "start with winter in the middle", "key3": "this is not valid"}
#print(validate_dict(rules, my_dict)) #false

#exemplu valid
rules2 = {("key1", "start", "middle", "end"), ("key2", "mara", "ceva", "sfarsit")}
my_dict2 = {
    "key1": "start....middle......end",
    "key2": "mara//ggggggg//ceva//gggggg//sfarsit",
    "key3": "pun orice aici ca nu are reguli de respectat"
}
#print(validate_dict(rules2, my_dict2))


#def ex6---a function that receives a list and returns a tuple (a, b),
# a nr de elemente unice, b cate elemente sunt duplicate

def ex6(elements_list):

    unique_elements = set()
    duplicate_elements = set()

    unique_elements = {element for element in elements_list if elements_list.count(element) == 1}
    a = len(unique_elements)

    duplicate_elements = {element for element in elements_list if elements_list.count(element) > 1}
    b = len(duplicate_elements)
    return a, b


#print(ex6([1, 2, 2, 3, 4, 5, 3, 7, 3, 8, 4, 2, 9]))


#ex7---a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -.

def ex7(*args):
    my_dict = {}
    set_list = list(args)

    for i in range(len(set_list)):
        for j in range(i + 1, len(set_list)):

            a = set_list[i]
            b = set_list[j]

            #cheile ca si stringuri
            union = f'"{a} | {b}"'
            intersection = f'"{a} & {b}"'
            a_minus_b = f'"{a} - {b}"'
            b_minus_a = f'"{b} - {a}"'

            #atribuim valorile
            my_dict[union] = a | b
            my_dict[intersection] = a & b
            my_dict[a_minus_b] = a - b
            my_dict[b_minus_a] = b - a

    return my_dict

#exemplu din tema
a = {1, 2}
b = {2, 3}
'''
output_dict = ex7(a, b)
#sau for i in ..print(i), dar ca sa arate ca in ex=>
for key, value in output_dict.items():
    print(f'{key}, {value}')
#alt ex
c = {3, 4}
output_dict = ex7(a, b, c)
for key, value in output_dict.items():
    print(f'{key}, {value}')
'''

#ex8--- a function primeste un dictionar numit mapping.
# acesta incepe mereu cu a string key "start". Starting with the value of this key you must obtain a list of objects
# by iterating over mapping in the following way: the value of the current key is the key for the next value,
# until you find a loop (a key that was visited before).
#adica plec din start are valoarea a, merg la cheia a vad ca are valoarea b, merg la cheia b..., ajung la 2, de aici n am unde
#sa merg deci am vizitat a,6,z,2, si o returnez
def ex8(mapping):
    visited = set()
    ouput_list = []
    current_key = "start"

    while current_key in mapping and current_key not in visited:
        visited.add(current_key)
        value = mapping[current_key]

        #verif sa nu fie in result deja
        if value not in ouput_list:
            ouput_list.append(value)

        current_key = value

    return ouput_list


# ex din tema
mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
#print(ex8(mapping))


#ex9---function that receives a variable number of positional arguments and a variable number of keyword arguments
# ret nr de atribute pozitinale pe care le gasesc in valorile keyword arguments
'''>>
argumente pozitionale (valori fara nume) 1
>>argumente numite (valori cu nume) x=1
si primim ca si tuple, ca din un dictionar, caut arg pozitionale in valorile arg keywd si vad cate apar
'''
def ex9(*positional_args, **keyword_args):
    positional_values = set(positional_args)
    keyword_values = set(keyword_args.values()) #doar valorile conteaza, in ele caut

    count = 0
    for arg in positional_values:
        if arg in keyword_values:
            count += 1

    return count

# ex din tema
#print( ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
