# python3
## Aleksandra Červinska 221RDB069 12.grupa
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    inp = input().rstrip().upper()
    if inp == 'F':
        with open('./tests/06','r') as f:
            pattern=f.readline().strip()
            text=f.readline().strip()
    elif inp == 'I':
        pattern=input().strip().lower()
        text=input().strip().lower()
        
    else:
        print("wrong inp")
        return None
    # after input type choice
    # read two lines
    # first line is pattern
    # second line is text in which to look for pattern
    # return both lines in one return
    # this is the sample return, notice the rstrip function
    return pattern, text

def print_gad(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_gad(pattern, text):
    # implementation of Rabin Karp's algorithm
    p = 1000000007  
    q = 10**9+9
    x = 263
    n = len(text)
    m = len(pattern)
    xp = [pow(x, i, q) for i in range(m)]
    hp = sum(ord(pattern[i]) * xp[m-1-i] for i in range(m)) % q
    ht = sum(ord(text[i]) * xp[m-1-i] for i in range(m)) % q
    gad = []
    if ht == hp and text[:m] == pattern:
        gad.append(0)
    for i in range(1, n-m+1):
        ht = (ht - ord(text[i-1]) * xp[m-1]) % q
        ht = (ht * x + ord(text[i+m-1])) % q
        if ht == hp and text[i:i+m] == pattern:
            gad.append(i)
    return gad

# this part launches the functions
if __name__ == '__main__':
    print_gad(get_gad(*read_input()))

