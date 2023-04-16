# python3
## Aleksandra Červinska 221RDB069 12.grupa
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    inp = input().rstrip()
    if inp == 'F':
        with open('./tests/06','r') as f:
            pattern=f.readline().strip().lower()
            text=f.readline().strip().lower()
    else:
        pattern=input().rstrip().lower()
        text=input().rstrip().lower()
    # after input type choice
    # read two lines
    # first line is pattern
    # second line is text in which to look for pattern
    # return both lines in one return
    # this is the sample return, notice the rstrip function
    return pattern, text

def print_gad(output):
    # this function should control output, it doesn't need any return
    #print(' '.join(map(str, output)))
    print(" ".join([str(i) for i in output]))

def get_gad(pattern, text):
    print("get_gad() funkcija")
    # this function should find the occurances using Rabin Karp alghoritm 
    k=31
    p=10**9 + 9
    m=len(pattern)
    n=[1]*(m+1)
    h=[0]*(len(text)-m+1)

    for i in range(1, m+1):
        n[i]=(n[i-1]*k)%p

    pattern_hash = sum(ord(pattern[i])*n[m-i] for i in range(m))%p

    h[0]=sum(ord(text[i])*n[m-i-1] for i in range(m))%p

    for i in range(len(text)-m+1):
        if i+m < len(text):
            h[i+1]=((h[i]-ord(text[i])*n[m-1])*k+ord(text[i+m]))%p

    gad = []
    for i in range(len(text)-m+1):
        if h[i] == pattern_hash:
            if text[i:i+m] == pattern:
                gad.append(i)
    # and return an iterable variable
    return gad


# this part launches the functions
if __name__ == '__main__':
    print_gad(get_gad(*read_input()))

