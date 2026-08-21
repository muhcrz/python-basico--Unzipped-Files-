preco = 120.00

produto = "Camiseta"

quantidade = 3


print(f"Total: R$ {preco * quantidade:.2f}")

total = preco * quantidade

if total >= 200.00:
    print(f"Total com desconto: R$ {total * 0.8:.2f}")
else:
    print(f"Total: R$ {total:.2f}")