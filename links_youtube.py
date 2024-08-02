from requests_html import HTMLSession


class LinksYT:
    def __init__(self, base_url):
        self.base_url = base_url
        self.ads_url = "https://adstransparency.google.com"

        self.id_client = self.id_search()
        self.creations_list = self.creatives_code()

    #Pesquisa o id do alvo
    def id_search(self):
        
        search_url = f"{self.ads_url}/?region=BR&domain={self.base_url}&platform=YOUTUBE&format=VIDEO"
        
        session = HTMLSession()
        response = session.get(search_url)
        response.html.render(sleep=5, keep_page=True)

        links = response.html.links

        id_client = []

        for item in links:
            if 'advertiser/' in item:
                start = item.find('advertiser/') + len('advertiser/')
                end = item.find('/', start)
            
                if end != -1:
                    id_client.append(item[start:end])
                    
                else:
                    id_client.append(0)
                
                break
        
        return id_client[0]
    
    #Cria a url da página principal do alvo, contendo os anúncios em vídeo
    def build_client_url(self):
        
        if self.id_client:
            client_url = f"https://adstransparency.google.com/advertiser/{self.id_client}?region=BR&format=VIDEO"

            return client_url
        else:
            return "ID não encontrado na URL fornecida."
    
    #Captura os códigos dos criativos
    def creatives_code(self):

        session = HTMLSession()
        url_client = self.build_client_url()
        response = session.get(url_client)
        response.html.render(sleep=5, keep_page=True)
        
        links = response.html.links

        creatives = []

        for item in links:
            if 'creative/' in item:
                start = item.find('creative/') + len('creative/')
                end = item.find('?', start)
                if end != -1:
                    creatives.append(item[start:end])
                else:
                    creatives.append(item[start:])

        return creatives

    #Monta a URL para entrar no criativo (e puxar a URL do youtube)
    def build_creation_url(self, creation_code):
        
        url_creation = f"https://adstransparency.google.com/advertiser/{self.id_client}/creative/{creation_code}?region=BR"
        
        return url_creation

    #Busca a URL do youtube em um criativo (inacabado)
    def youtube_search(self, creation_code):

        url_creation = self.build_creation_url(creation_code)
        print(url_creation)

        session = HTMLSession()
        response = session.get(url_creation)
    
        response.html.render(sleep=10, keep_page=True)
        
        links = response.html.links

        return links
    
    #Inserir método para criar uma lista com todos os links do youtube dos criativos que forem do youtube. 

    #Conectar com ./youtube_info.py para buscar informações requisitadas de cada vídeo. 


#Exemplo

search = LinksYT('engluizfernando.com')

print(search.id_client)
print(search.creations_list)

print(search.youtube_search('CR06025348081266982913'))
    

   
 