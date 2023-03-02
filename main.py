from Gif import AsciiGif
from Video import AsciiVideo
from Imagem import AsciiImagem
from prettytable import PrettyTable

class Main:
    def __init__(self):
        self.tabela_opcoes = PrettyTable()
        self.tabela_opcoes.field_names = ["Valor", "Comando"]
        self.tabela_opcoes.add_rows(
            ([1, "URL de Imagem"],
             [2, "Imagem local"],
             [3, "URL de GIF"],
             [4, "GIF local"],
             [5, "Arquivo de vídeo"],
             [6, "Webcam"]))

    def run(self):
        print(self.tabela_opcoes)
        modo_input = int(input("Selecione a opção desejada: "))
        if modo_input == 1:
            url_imagem = input("Insira a URL da imagem: ")
            imagem_ascii = AsciiImagem(url=url_imagem)
            imagem_ascii.exibir_imagem()
        if modo_input == 2:
            caminho_imagem = input("Insira o caminho da imagem: ")
            imagem_ascii = AsciiImagem(path=caminho_imagem)
            imagem_ascii.exibir_imagem()
        elif modo_input == 3:
            url_gif = input("Insira a URL do gif: ")
            gif_ascii = AsciiGif(url=url_gif)
            gif_ascii.exibir_gif()
        elif modo_input == 4:
            caminho_gif = input("Insira o caminho do gif: ")
            gif_ascii = AsciiGif(path=caminho_gif)
            gif_ascii.exibir_gif()
        elif modo_input == 5:
            caminho_video = input("Insira o caminho do video: ")
            video_ascii = AsciiVideo(path=caminho_video)
            video_ascii.exibir_video()
        elif modo_input == 6:
            video_ascii = AsciiVideo()
            video_ascii.exibir_video()


if __name__ == "__main__":
    main = Main()
    main.run()
