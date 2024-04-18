try:
    A=9.99999999/5
except(ArithematicError,IOError) as e:
    Print(e)
else:
    print(A)

    def foo():
        try:
            print(1)
        finally:
            print(2)
    foo()