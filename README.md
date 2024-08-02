# Documentação do DeepTube Fake

Este documento descreve o funcionamento dos scripts `links_youtube.py` e `youtube_info.py`. Eles têm como objetivo capturar informações detalhadas de anúncios do youtube, obtidos através da biblioteca de transparência de anúncios do Google.

## links_youtube.py

### Descrição

Este script é responsável por interagir com a plataforma Google Ads Transparency para capturar IDs de anunciantes e códigos de criativos. A partir desses códigos, ele busca links de vídeos no YouTube associados aos criativos.

### Classes e Métodos

#### `class LinksYT`

- **Descrição**: Classe responsável por buscar IDs de anunciantes e códigos de criativos, e construir URLs para acessar vídeos do YouTube.

- **Métodos**:
  - `__init__(self, base_url)`: Inicializa a classe com a URL base do anunciante.
  - `id_search(self)`: Pesquisa o ID do anunciante a partir da URL base.
  - `build_client_url(self)`: Constrói a URL principal da página do anunciante contendo os anúncios em vídeo.
  - `creatives_code(self)`: Captura os códigos dos criativos a partir da página principal do anunciante.
  - `build_creation_url(self, creation_code)`: Constrói a URL de um criativo específico.
  - `youtube_search(self, creation_code)`: Busca links de vídeos do YouTube associados a um criativo específico (método ainda inacabado).

  - obs: o método youtube_search precisa ser aprimorado para filtrar e retornar apenas links de vídeos do YouTube.
  - Necessário um método para criar uma lista com todos os links do YouTube dos criativos que forem do YouTube.
  - Conectar com youtube_info.py para buscar informações detalhadas de cada vídeo.


## youtube_info.py

Este script utiliza a biblioteca `pytube` para obter informações detalhadas sobre um vídeo do YouTube, como título, canal, duração, visualizações, likes, thumbnail, se é um YouTube Shorts, transcrição, data de publicação e o link do vídeo.

## Funções

### `get_video_info(url)`

- **Descrição**: Obtém informações detalhadas sobre um vídeo do YouTube a partir da URL fornecida.
- **Parâmetros**: 
  - `url`: URL do vídeo do YouTube.
- **Retorna**: Um dicionário contendo as seguintes informações:
  - **Título do vídeo**: O título do vídeo.
  - **Título do canal**: O nome do canal que publicou o vídeo.
  - **Duração do vídeo**: A duração do vídeo em segundos.
  - **Quantidade de visualizações**: O número de visualizações do vídeo.
  - **Quantidade de likes**: Placeholder (pytube não fornece diretamente a quantidade de likes).
  - **Link da thumbnail**: URL da imagem de miniatura do vídeo.
  - **Indicação se é um YouTube Shorts**: Indica se o vídeo é um YouTube Shorts.
  - **Transcrição do vídeo**: Texto da transcrição do vídeo (se disponível).
  - **Data de publicação**: A data de publicação do vídeo.
  - **Link do vídeo**: URL do vídeo no YouTube.


### Exemplo de Uso

```python
# Exemplo de uso LinksYT

search = LinksYT('smartfit.com.br')

print(search.id_client)
print(search.creations_list)
print(search.build_client_url())

# Exemplo de uso youtube_info.py

url = "https://www.youtube.com/watch?v=csJKauwbYFk"
video_info = get_video_info(url)

for key, value in video_info.items():
    print(f"{key}: {value}")