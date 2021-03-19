def prost(n):
    d=2
    while n%d!=0:
        d+=1
        print(d==n)
    return d==n
if __name__ == '__main__':
    n=int(input())
    print(n)
    if prost(n)==True:
        print("Простое")
    else:
        print("Составное")
