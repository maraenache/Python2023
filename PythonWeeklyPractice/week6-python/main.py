import sys
import os


# ex1------------------------

def print_files(directory, extension):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory {directory} not found")

        file_list = os.listdir(directory)
        for file_name in file_list:
            if file_name.endswith(extension):
                file_path = os.path.join(directory, file_name)
                print(file_path)
                # cu with- e asigurata inchiderea fisierului
                try:
                    with open(file_path, "r") as f:
                        for line in f:
                            print(line)
                except IOError as err_open:
                    print(f"Error - unable to open {file_path}: {err_open}")
                except Exception as err_read:
                    print(f"Error - unable to read from {file_path}: {err_read}")

    except FileNotFoundError as err_directory:
        print(f"Error - unable to access {directory}: {err_directory}")
    except ValueError as err_extension:
        print(f"Error: {err_extension}")


def ex1():
    try:
        if len(sys.argv) != 3:
            raise ValueError("You should have a directory path and a file extension as command line arguments")

        directory = sys.argv[1]
        extension = sys.argv[2]

        print_files(directory, extension)

    except ValueError as err_value:
        print(f"Error: {err_value}")
    except Exception as e:
        print(f"Error: {e}")

# python C:\Users\Mara\PycharmProjects\pythonProject6\main.py C:\Users\Mara\Desktop\tema6-python\ txt
# if __name__ == "__main__":
#   ex1()

'''(pt mine) 
   - sys.argv: lista cu argumente de la linia de comanda sys.argv[0] e file_path_name
   - os.path.isdir(directory)- verif daca calea specif este un director
   - os.listdir(directory)- ret o lista cu numele fisierelor din directorul specificat
   - os.path.join(directory, file_name): combina directory_path cu file_name si => file_name_path
   - os.path.exists(file_path)- verif daca un fisier/director exista la calea specificata
   
open # fara with, ca in curs-trb si f.close()
        try:
            f = open(file_path, "r")
           //
            f.close()  
        except IOError as err_open:
           //
        except Exception as err_read:
            //
        finally:
            f.close() 
'''


# ex2------------------------
def rename_files(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory {directory} not found")

        file_list = os.listdir(directory)
        file_list.sort()

        for position, file_name in enumerate(file_list, start=1):  # fara start e implicit 0
            file_path = os.path.join(directory, file_name)
            new_name = f"file{position}.{file_name.split('.')[-1]}"  # pastram extensia -secventa de la . la ult
            renamed_file_path = os.path.join(directory, new_name)

            os.rename(file_path, renamed_file_path)
            print(f"just renamed {file_name} to {new_name}")

    except FileNotFoundError as err_directory:
        print(f"Error- unable to access {directory}: {err_directory}")
    except PermissionError as err_permission:
        print(f"Error: permission denied - {err_permission}")
    except Exception as e:
        print(f"Error: {e}")


def ex2():
    directory_path = "C:\\Users\\Mara\\Desktop\\tema6-python\\ex2-files\\"
    rename_files(directory_path)


# ex2()

'''
- enumerate(file_list) merge prin lista de fisiere si ret tuple index, file_name
- os.rename(file_path, file_new_path) -schimba numele pt un fisier cu unul nou
'''


# ex3------------------------
def calculate_size(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory {directory} not found")

        size = 0

        for root, directories, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                size += os.path.getsize(file_path)

        print(f"Total size of the {directory}: {size} bytes")

    except FileNotFoundError as err_directory:
        print(f"Error- unable to access {err_directory}")
    except PermissionError as err_permission:
        print(f"Error- permission denied {err_permission}")
    except Exception as e:
        print(f"Error: {e}")


def ex3():
    try:
        if len(sys.argv) != 2:
            raise ValueError("You should have a directory path as command line argument")

        directory = sys.argv[1]
        calculate_size(directory)

    except ValueError as value_error:
        print(f"Error: {value_error}")
    except Exception as general_error:
        print(f"Error: {general_error}")


# python C:\Users\Mara\PycharmProjects\pythonProject6\main.py C:\Users\Mara\Desktop\tema6-python\
# if __name__ == "__main__":
#   ex3()

'''
- os.path.getsize(file_path) - ret size in bytes a unui fisier cu calea specif
- os.walk(directory) - merge prin director si subdirectoare si returneaza tuplu (root,directories,files)
'''


# ex4------------------------
def calculate_file_extension_number(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory {directory} not found")

        number_occurrences_extension = {}

        file_list = os.listdir(directory)
        for file_name in file_list:

            file_path = os.path.join(directory, file_name)

            if os.path.isfile(file_path):
                name, extension = os.path.splitext(file_name)  # desparte in C:\....\main si py

                if extension not in number_occurrences_extension:
                    number_occurrences_extension[extension] = 1
                else:
                    number_occurrences_extension[extension] += 1

        if not number_occurrences_extension:
            raise ValueError(f"No files found in {directory}")

        print("Number of files by each extension")
        for extension, count in number_occurrences_extension.items():
            print(f"{extension}: {count} files")

    except FileNotFoundError as err_directory:
        print(f"Error- unable to access {err_directory}")
    except PermissionError as err_permission:
        print(f"Error- permission denied - {err_permission}")
    except ValueError as err_value:
        print(f"Error: {err_value}")
    except Exception as e:
        print(f"Error: {e}")


def ex4():
    try:
        if len(sys.argv) != 2:
            raise ValueError("You should have a directory path as a command line argument")

        directory_path = sys.argv[1]
        calculate_file_extension_number(directory_path)

    except ValueError as err_value:
        print(f"Error: {err_value}")
    except Exception as e:
        print(f"Error: {e}")

# python C:\Users\Mara\PycharmProjects\pythonProject6\main.py C:\Users\Mara\Desktop\tema6-python\
#if __name__ == "__main__":
#   ex4()

'''
-  os.path.splitext(file_name) -desparte din file_path_name si face un tuplu (nume fara extensie, extensia)
'''

#----------------------------------------------------^
''' 
din curs
print("the file where i m working is ", sys.argv[0])
print("lista dir", os.listdir("."))
print(os.path.dirname(sys.argv[0]))
print(os.listdir(os.path.dirname(sys.argv[0])))
# x=input("write smth")
# print(x)
for arg in sys.argv:
    print(arg)
for (root, directories, files) in os.walk("."):
    for file_name in files:
        full_file_name = os.path.join(root, file_name)
print(full_file_name)
print (os.path.splitext ("C:\\Windows\\abc.txt")- separa extensia
'''
