from memory_profiler import profile, memory_usage

#    Exercise 1
# def myfunction(list_size):
#     mylist = ['hello']*list_size
#     mylist2 = ['world']*list_size
#     del mylist2
#     return mylist

# myfunction(1000000)

#    Exercise 2
# @profile

# def myfunction(list_size):
#     mylist = ['hello']*list_size
#     mylist2 = ['world']*list_size
#     del mylist2
#     return mylist

# myfunction(1000000)

#    Exercise 3
# log_file = open('memory.log', 'w+')
# @profile(stream=log_file)

# def myfunction(list_size):
#     mylist = ['hello']*list_size
#     mylist2 = ['world']*list_size
#     del mylist2
#     return mylist

# myfunction(1000000)

#    Exercise 4
# log_file = open('memory2.log', 'w+')
# @profile(stream=log_file)

# def myfunction(list_size):
#     mylist = ['hello']*list_size
#     mylist2 = ['world']*list_size
#     del mylist2
#     return mylist

# myfunction(1000000)
# myfunction(10000000)
# myfunction(100000000)

#    Exercise 5
#Running from terminal:
#mprof run mp.py
#mprof plot, will plot file mprofile....

@profile()
def myfunction(list_size):
    mylist = ['hello']*list_size
    mylist2 = ['world']*list_size
    del mylist2
    return mylist

myfunction(10000000)

#https://www.youtube.com/watch?v=3PdmLQIZpwE