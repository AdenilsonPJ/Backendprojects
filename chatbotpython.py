import os

def processar_resposta(resposta,nome):
    if resposta=='1':
        print(f'{os.linesep}{nome} ,na minha opinião vale muito a pena.{os.linesep}')

    elif resposta == '2':
        print(f'{os.linesep}{nome} ,isso varia muito com o nível de esforço ,dedicação e busca por vagas de cada indivíduo.{os.linesep}')

    elif resposta == '3':
        print(f'{os.linesep}{nome} ,você simplesmente tem que aplicar seu conhecimento nas oportunidades oferecidas.{os.linesep}')

    elif resposta == '4':
        print(f'{os.linesep}{nome} ,você pode estudar através de vídeos gratuitos no Youtube,dos livros e dos sites de programação.{os.linesep}')

    else:
        print('Opção inexistente.')
def start():
    print('Olá! Seja bem vindo!')# apresentação
    nome=input('Digite o seu nome:')# pedir o nome
    email=input('Digite seu email:')# pedir email

    # ofercer menu opções
    while True:
     resposta=input(f'O que gostaria de saber hoje?{os.linesep}[1] - Vale a pena aprender Python?{os.linesep}[2] - Quanto tempo leva pra conseguir um emprego com Python?{os.linesep}[3] - quando vou estar bom para um emprego?{os.linesep}[4] - Onde recomendaria estudar Python?{os.linesep}')

     processar_resposta(resposta,nome)# processar a resposta à pergunta

if __name__=='__main__':
    start()