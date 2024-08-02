from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_info(url):
    try:
        
        yt = YouTube(url)

        video_info = {
            "Título Vídeo": yt.title,
            "Título do Canal": yt.author,
            "Duração do Vídeo": yt.length,
            "Quantidade de Views": yt.views,
            "Quantidade de Likes": yt.rating,  
            "Link da thumbnail": yt.thumbnail_url,
            "É um YouTube Shorts?": "shorts" in yt.watch_url,
            "Data de publicação": yt.publish_date.strftime("%Y-%m-%d"),
            "Link do Vídeo": yt.watch_url
        }

        # Transcrição
        try:
            transcript = YouTubeTranscriptApi.get_transcript(yt.video_id)
            video_info["Transcrição do vídeo"] = "\n".join([t['text'] for t in transcript])
        
        except Exception as e:
            video_info["Transcrição do vídeo"] = "Transcrição não disponível"

        return video_info

    except Exception as e:
        return {"Erro": str(e)}

# Exemplo
# url = "https://www.youtube.com/watch?v=csJKauwbYFk"
# video_info = get_video_info(url)

# for key, value in video_info.items():
#     print(f"{key}: {value}")