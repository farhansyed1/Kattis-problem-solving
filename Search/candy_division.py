import math

def benny_friends(N):
    friends = set()
    for i in range(1, int(math.isqrt(N)) + 1):
        if N % i == 0:
            friends.add(i - 1) # divisor 1
            friends.add(N // i - 1) # divisor 2
    friends = sorted(f for f in friends if f >= 0)
    print(' '.join(map(str, friends)))

def main():    
    N = int(input())
    benny_friends(N)

if __name__ == "__main__":
    main()