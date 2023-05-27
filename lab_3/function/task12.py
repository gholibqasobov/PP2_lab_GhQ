lis = list(input().split())
def histogram(l):
    for i in range(len(l)):
        print('*' * int(l[i]))

histogram(lis)