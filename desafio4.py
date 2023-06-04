import urllib.request

nothing = '12345'
for c in range(400):
    print(nothing)
    x = urllib.request.urlopen(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}")
    resposta = x.read()
    html = resposta.decode("UTF-8")
    print(html)
    with open('desafio4.txt', 'a') as arquivo:
        arquivo.write(html + '\n')
    nothing = ''
    for x in range(len(html)):
        if html[x].isnumeric():
            nothing += html[x]
