# fibonacci.py

def fib():
    
    fibs=[1,2]
    
    for i in range(1,9):
        
        A=fibs[i-1]

        B=fibs[i]

        C=A+B
        
        fibs.append(C)
        
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
