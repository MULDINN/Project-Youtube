# Importando as bibliotecas

from pytube import YouTube
import os

os.system('color 3')

print("Desenvolvido por Guilherme Richard =)")
a = int(input("Digite qual opção deseja realizar o download:\n1- MP3\n2- MP4\n"))

# Pegando link do vídeo 
link = input('Digite o link do vídeo: ')
video = YouTube(link)
print(f"Video:  {video.title}")
counter = 0

if a == 1:
     counter += 1
     ("Baixando ", {counter}, (video))
     yt = YouTube(link)
     ('Título: ', {yt.title})

    #Pegando somente áudio
     stream = yt.streams.get_audio_only()

     # Baixando e colocando em uma pasta chamada Músicas
     out_file = stream.download(output_path="Músicas")
     base, ext = os.path.splitext(out_file)
     new_file = base + '.mp3'
     os.rename(out_file, new_file)
     os.system('cls')
     
else:
        counter += 1
        ("Baixando ", {counter}, (video))
        yt = YouTube(link)
        ('Título: ', {yt.title})

        # Pegando somente vídeo (em alta qualidade)
        stream = yt.streams.get_highest_resolution()

        # Baixando e colocando em uma pasta chamada Vídeos
        out_file = stream.download(output_path="Vídeos")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        os.system('cls')