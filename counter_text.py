from collections import Counter

text_one = """
A imagem não foi a primeira coisa a trazer atenção para mãe Michelly, que tem mais de 700 mil seguidores no Instagram. 
Ela é conhecida também por fazer amarrações para o amor e até mesmo resolver brigas por herança — ritos controversos 
dentro de vertentes como a umbanda, que defende o livre arbítrio. Apesar de os comentários nos posts se dividirem 
entre elogios e críticas pesadas, a religiosa conta que não sofre preconceito religioso na cidade em que vive. 
E, segundo um estudo da UFRGS publicado em 2020, a tolerância não é fruto da sorte. Os dois últimos censos do I
BGE indicaram o Rio Grande do Sul como o estado mais afro-religioso do Brasil, superando inclusive a Bahia em número... 
- Veja mais em https://noticias.uol.com.br/cotidiano/ultimas-noticias/2023/03/22/estatua-belzebu-casa-alvorada.htm?cmpid=copiaecola
"""

text_two = """
Por outro lado, o especialista explica que, se esse cenário perdurar por longo tempo, a rede não terá outra escolha a não ser criar 
promoções para os clientes. Isso seria uma das únicas saídas para aliviar as pressões sobre os estoques, que, de tempos em tempos, 
precisam girar para não comprometer a geração de caixa das empresas. "Não há muita pressa para a renovação dos estoques por 
desatualização dos modelos, pois ainda estamos em março. Se tivéssemos mais para o fim do ano, isso também seria uma preocupação. 
Mas, ainda assim, as marcas precisam de algum retorno financeiro. Se a manutenção dos preços por tempo indeterminado estiver limitando 
demais as vendas, a próxima medida se... - Veja mais em https://www.uol.com.br/carros/noticias/redacao/2023/03/22/
por-que-carros-nao-vao-baratear-nem-um-pouco-mesmo-sobrando-nos-patios.htm?cmpid=copiaecola
"""
def read_text(text):

    number_letters = Counter(text.lower())
    total_appearance = sum(number_letters.values())

    number_letters = dict(number_letters.most_common(10))

    for letter, total in number_letters.items():
        print(f"{letter} => {(total/total_appearance)*100:.2f}%")


read_text(text_two)




