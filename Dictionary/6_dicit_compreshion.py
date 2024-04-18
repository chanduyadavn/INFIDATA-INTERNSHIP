odd_dicit={i:i+2 for i in range(1,10,2)}
print(odd_dicit)

square_dicit={i:i**2 for i in range(1,7)}
print(square_dicit)

even_square={i:i*i for i in range(1,10) if i%2==0}
print(even_square)

odd_square={i:i*i for i in range(1,10) if i%2!=0}
print(odd_square)
