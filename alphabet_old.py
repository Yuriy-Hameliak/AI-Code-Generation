"""create a pattern of characters based on a given number"""
def main(number):
    """f"""
    num = int(input()) if not number else number
    n=0
    l=0
    c=0
    while n < num:
        l+=1
        n+=l
    for i in range(1,l+1):
        print('  '*(l-i),end='')
        
        for j in range(i):
            if c==num-1:
                print(chr(65+c))
                break
            elif  j != i-1:
                print(chr(65+c),end=' ')
                c+=1
            else:
                print(chr(65+c))
                c+=1