# Módulo Responsável por gerenciar arquivos
# Responsável: Bruno da Fonseca Chevitarese

import pickle


def info_arquivo_bin() -> dict:
    """
    :Função: Pega as informações contidas em um arquivo do tipo .bin

    :return:  Dicionário de Dicionários condendo as informações do arquivo
    """

    info = dict()

    # O trecho abaixo extraí informações do arquivo binário; Ele só funciona, pois, espera-se um arquivo bin com uma saída específica. Nosso agradecimentos ao aluno Miguel Rabelo por ter nos ensinado a extraír os dados do aquivo .bin
    with open("../../backup.bin", "rb") as f:
        info["usuarios"] = pickle.load(f)
        info["conexoes"] = pickle.load(f)
        info["tentativas"] = pickle.load(f)

    return info

