from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv
import nltk
from sys import argv
stopwords = nltk.corpus.stopwords.words('portuguese')

#cabeçalho para a requisição (para evitar erros 403)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

def imprimeLista(lista, arquivo):
    for elemento in lista:
        escreveLista.write(elemento+"\n")

def nomeDominio(link):
    try:
        dominio = link.split("/")[2]
        if ((dominio.split('.')[0] == 'www') or (dominio.split('.')[0] == 'www2') or (dominio.split('.')[0] == 'www1')  or (dominio.split('.')[0] == 'www12')) :
            return dominio.split(".")[1]
        return dominio.split(".")[0]
    except:
        return "#"

def pagPrincipal(link):
    return link.split("/")[0]+"//"+link.split("/")[2]

def retiraPontuacao(texto):
    caracteres = ['.', ',', '”', '“', ':', ';', '(', ')', '"', '!', '?', '’', '‘', "'", '*']
    for caractere in caracteres:
        texto = texto.replace(caractere, ' ')
    return texto




fontes = """
publicabrasil;https://blogdomagno.com.br/ver_post.php?id=204467&pagina=2
publicabrasil;http://www.portalanativa.com.br/2017/author/mabinder/page/23/
publicabrasil;http://blogdorobsonfreitas.blogspot.com/2019/01/ministro-do-meio-ambiente-expoe-farra.html
publicabrasil;https://www.jornalhoradasnoticias.com.br/2018/07/janaina-pascoal-cai-como-uma-luva-sendo.html
publicabrasil;https://goioxim.blogspot.com/2018/11/fernando-haddad-vira-reu-por-corrupcao.html
publicabrasil;https://blogdosaber.com.br/politica-ate-ministro-do-stf-questiona-candidatura-de-jair-bolsonaro/
publicabrasil;https://adautojornalismo.wixsite.com/itabunadigitalnews/blog/categories/universo/
publicabrasil;https://adautojornalismo.wixsite.com/itabunadigitalnews/post/cientistas-se-encontram-para-investigar-o-grande-sil%C3%AAncio-gal%C3%A1ctico
publicabrasil;https://www.ignews.com.br/2019/09/08/olavo-de-carvalho-defende-escolha-de-aras-para-pgr/
publicabrasil;http://soviuagora.blogspot.com/2018/11/a-manobra-de-gilmar-mendes-foi-por-agua.html
publicabrasil;https://gpsdanoticia.com.br/extra-policia-federal-investiga-ligacao-entre-lulinha-e-sergio-cabral/
publicabrasil;https://www.ouropretoonline.com/modules/news/index.php?storytopic=25&start=150
publicabrasil;http://www.findglocal.com/BR/Recife/1392703840824092/Cavalaria-da-Direita
publicabrasil;http://alertabarauna.blogspot.com/2018/
publicabrasil;http://blogdowilliamvieira.blogspot.com/2018/06/extra-general-detona-gleisi-e.html
publicabrasil;https://blogdomicko.blogspot.com/2018/07/em-fato-muito-estranho-membros-da-alta.html
publicabrasil;https://www.atual10.com.br/2018/07/olha-o-que-esse-lixo-da-politica-teve.html?m=0
publicabrasil;https://compartilhandonoticia.com.br/noticias-/roberto-cabrini-denuncia-governadores-estao-roubando-o-povo-na-pandemia
publicabrasil;https://compartilhandonoticia.com.br/noticias-/roberto-cabrini-denuncia-governadores-estao-roubando-o-povo-na-pandemia
"""

#abrir arquivo txt

with open("listaTermos.txt", "w") as escreveLista:

    sites = fontes.split("\npublicabrasil;")
    sites.remove('')
    for site in sites:
        principal = pagPrincipal(site)
        req = Request(url=principal, headers=headers)

        escreveLista.write("Site:"+principal+"\n")
        try:
            html = urlopen(req).read()
            soup = BeautifulSoup(html, 'html.parser')
            paragrafos = soup.find_all('p')
            texto = ""
            for paragrafo in paragrafos:
                texto+=paragrafo.getText()
            texto = retiraPontuacao(texto)
            palavras = texto.split(' ')
            termos = []
            for palavra in palavras:
                if palavra not in stopwords and palavra != '':
                    palavra = palavra.strip('"')
                    termos.append(palavra)
            imprimeLista(termos, escreveLista)


        except:
            escreveLista.write("Site inacessível.\n")
        escreveLista.write("___________________________\n")
