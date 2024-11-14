# eleborar um algoritimo que solicita 4 notas ao usuario.
# o programa deve calcularva média e
# verificar se a média é maior ou igual a 80.
# se a média for maior ou igual a 80, o programa
# deve exibir a mensagem "aprovado " e se a media for menor que 
# 80, o programa deve exibir a mensagem "reprovado."
 
nota1 = float(input("digite a nota1"))
nota2 = float(input("digite a nota2"))
nota3 = float(input("digite a nota3"))
nota4 = float(input("digite a nota4"))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"a media final obitida = {media}")

if (media >= 80):
    print("aprovado")
else:
    print("reprovado") 