import multiprocessing

# empty list with global scope
result = []

def square(a):
    global result
    # append square of numbers in list a to global list result
    for i in a:
        result.append(i*i)
    # print global list result
    print("Result in first process",result)

def square_root(a):
    global result
    # append square root of numbers in list a to global list result
    for i in a:
        result.append(int(i**(1/2)))
    # print global list result
    print("Result in second process",result)

if __name__ == "__main__":
    # list
    a = [1,4,9,16]

    # create process
    p1 = multiprocessing.Process(target=square, args=(a, ))
    p2 = multiprocessing.Process(target=square_root, args=(a, ))

    # start process
    p1.start()
    p2.start()

    #wait until process is finished
    p1.join()
    p2.join()

    # print global list result
    print("Result in main",result)
