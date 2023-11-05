# ex1--- Python class that simulates a Stack
# methods like push, pop, peek (the last two methods should return None if no element is present in the stack)
class StackClass:

    def __init__(self):
        self.numbers = []

    def push(self, new_number):
        self.numbers.append(new_number)

    def pop(self):
        if len(self.numbers) == 0:
            return None
        else:
            popped_number = self.numbers[-1]
            self.numbers.pop()
            return popped_number

    def peek(self):
        if len(self.numbers) == 0:
            return None
        return self.numbers[-1]

    def print_stack(self):
        print(self.numbers)
        #print("-------------")


def ex1_test():
    my_stack = StackClass()

    my_stack.push(4)
    my_stack.push(5)
    my_stack.push(7)

    print("Current stack:")
    my_stack.print_stack()

    print("Just popped this number: ")
    print(my_stack.pop())

    print("Current stack:")
    my_stack.print_stack()

    my_stack.pop()
    print("Current stack:")
    my_stack.print_stack()

    my_stack.push(10)
    my_stack.push(20)

    print("Current stack:")
    my_stack.print_stack()

    print("Top of the stack is:")
    print(my_stack.peek())

#ex1_test()


# ex2---Write a Python class that simulates a Queue
# methods like push, pop, peek (the last two methods should return None if no element is present in the queue).
class QueueClass:

    def __init__(self):
        self.numbers = []

    def push(self, new_number):
        self.numbers.append(new_number)

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_number = self.numbers[0]
            self.numbers.pop(0)
            return popped_number

    def peek(self):
        if self.is_empty():
            return None
        return self.numbers[0]

    def is_empty(self):
        return len(self.numbers) == 0

    def print_queue(self):
        print(self.numbers)


def ex2_test():

    my_queue = QueueClass()

    my_queue.push(4)
    my_queue.push(5)
    my_queue.push(7)

    print("Current queue:")
    my_queue.print_queue()

    print("Just popped this number")
    print(my_queue.pop())
    print("Current queue:")
    my_queue.print_queue()
    print("Just popped this number")
    print(my_queue.pop())
    print("Current queue:")
    my_queue.print_queue()

    my_queue.push(10)
    my_queue.push(20)

    print("Current queue:")
    my_queue.print_queue()

    print("First element from the queue")
    print(my_queue.peek())

#ex2_test()


#ex3--- Python class that simulates a matrix of size NxM
# The class should provide methods to access elements (get and set methods)
# and functions such as transpose, matrix multiplication and a method that allows
# iterating through all elements form a matrix an apply a transformation over them (via a lambda function).
class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for j in range(cols)] for i in range(rows)]

    def get(self, row, col):
        # doar daca e in chenar, pot face operatii
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matrix[row][col]
        else:
            return None

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = value

    def transpose(self):

        transpose_matrix = [[0 for i in range(self.rows)] for j in range(self.cols)]

        for i in range(self.rows):
            for j in range(self.cols):
                transpose_matrix[j][i] = self.matrix[i][j]

        self.matrix = transpose_matrix

        number_of_rows = self.rows
        self.rows = self.cols
        self.cols = number_of_rows

    def multiply(self, matrix2):

        if self.cols != matrix2.rows:
            return None

        # daca au dimens dif, matr1: n x m si matrix2: m x p-> matr output n x p
        output_matrix = Matrix(self.rows, matrix2.cols)

        for i in range(self.rows):
            for j in range(matrix2.cols):
                k_line_col_product = sum(self.matrix[i][k] * matrix2.matrix[k][j] for k in range(self.cols))
                output_matrix.matrix[i][j] = k_line_col_product

        return output_matrix

    def apply(self, lambda_expression):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = lambda_expression(self.matrix[i][j])
    '''
    def print_matrix(self):
        for row in self.matrix:
            for value in row:
                print(value, end="\t")
            print()
    '''
    # sau
    def __str__(self):#un fel de toString, in loc de print_matrix
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])


def ex3_test():
    matrix1 = Matrix(3, 3)
    matrix2 = Matrix(3, 3)

    value = 1
    for i in range(3):
        for j in range(3):
            matrix1.set(i, j, value)
            matrix2.set(i, j, value * 2)
            value += 1

    print("matrix1:")
    print(matrix1)
    #matrix1.print_matrix()

    print("using get method:")
    print(matrix1.get(0,0))
    print(matrix1.get(1,1))
    print(matrix1.get(2,2))

    print("matrix2:")
    print(matrix2)

    print("transpose matrix1:")
    matrix1.transpose()
    print(matrix1)
    print("transpose matrix2:")
    matrix2.transpose()
    print(matrix2)

    print("matrix1 x matrix2:")
    matrix_multiplication = matrix1.multiply(matrix2)
    print(matrix_multiplication)

    print("matrix before lambda:")
    print(matrix1)
    print("lambda changing the matrix:")
    matrix1.apply(lambda x: chr(ord('a') + (x-1) % 26))
    print(matrix1)


ex3_test()