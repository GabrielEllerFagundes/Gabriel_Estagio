from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

#cabeçalho para a requisição (para evitar erros 403)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

def exibeLista(lista):
    for elemento in lista:
        print (elemento)

def nomeDominio(link):
    try:
        dominio = link.split("/")[2]
        if ((dominio.split('.')[0] == 'www') or (dominio.split('.')[0] == 'www2') or (dominio.split('.')[0] == 'www1')  or (dominio.split('.')[0] == 'www12')) :
            return dominio.split(".")[1]
        return dominio.split(".")[0]
    except:
        return "#"

def exibeDominios(sites):
    for site in sites:
        dominio = nomeDominio(site)
        print(dominio)
     
def verificaDominio(dominio):
    #verifica se o domínio é realmente um site
    caracteres = ['?', '=', '!', '#', '$', '*']
    for caractere in caracteres:
        if caractere in dominio:
            return '#'
    return dominio

stopList = [
    '#',
    '#page',
    'pt-br',
    'itunes',
    'boostingads',
    'statcounter',
    'conta',
    'servedby',
    'anuncie',
    'feeds',
    'whatsapp',
    'xyzscripts',
    'facebook',
    'admin',
    'app',
    'magonedemo',
    'wpbloggertemplates',
    'twitter',
    'linkedin',
    'pinterest',
    'youtube',
    'instagram',
    'support',
    'blogger',
    'plus',
    'tumblr',
    'wordpress',
    'BRASIL',
    'gooyaabitemplates',
    'wix',
    'mybloggerthemes',
    'soratemplates',
    'addtoany',
    'themegrill',
    'webcontadores',
    'evpsistemas',
    'ebay'
]

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

#abrir arquivo csv

with open('listaFake.csv', mode='w', newline='') as listaFake:
    escreveLista = csv.writer(listaFake, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    sites = fontes.split("\npublicabrasil;")
    sites.remove('')
    #exibeLista(sites)
    #exibeDominios(sites)

    escreveLista.writerow(['Target', 'Source'])
    for site in sites:
        req = Request(url=site, headers=headers)
        try:
            html = urlopen(req).read()
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                try:
                    dominio = nomeDominio(link['href'])
                except:
                    dominio = '#'
                dominio = verificaDominio(dominio)
                if dominio not in stopList and len(dominio)>3:
                    escreveLista.writerow([nomeDominio(site), dominio])

        except:
            escreveLista.writerow(["Site inacessível."])
        escreveLista.writerow(["___________________________"])
