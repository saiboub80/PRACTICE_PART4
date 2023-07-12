def max_number(*numbs):
    numb= max(numbs)
    print( numb)
max_number(2,6,100)


def mult_list(*numbers) :
    for n in numbers:
        result= n*n
        print(result)

mult_list(2,5,6,4,54)

def rev_string(str):
    result= str[::-1]
    print(result)


rev_string("hello boss")

def num_within(x,y,z):
    if y<=x<=z:
        return True
    else:
        return False
print(num_within(3,2,4))

def pascal(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    for row in triangle:
        print(row)

 
pascal(2)