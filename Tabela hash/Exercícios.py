class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho

    def __str__(self):
        return f"Nome: {self.nome}, Caminho: {self.caminho}, Tamanho: {self.tamanho} KB"

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = {i: [] for i in range(size)}

    def hash_function(self, key):
        # Função de hash baseada na soma dos códigos ASCII dos caracteres do nome
        return sum(ord(char) for char in key) % self.size

    def adicionar_arquivo(self, arquivo):
        index = self.hash_function(arquivo.nome)
        # Adiciona o arquivo ao bucket correspondente
        self.table[index].append(arquivo)

    def buscar_arquivo(self, nome):
        index = self.hash_function(nome)
        # Busca pelo arquivo com o nome especificado
        for arquivo in self.table[index]:
            if arquivo.nome == nome:
                return arquivo
        return None

    def remover_arquivo(self, nome):
        index = self.hash_function(nome)
        # Remove o arquivo pelo nome
        for i, arquivo in enumerate(self.table[index]):
            if arquivo.nome == nome:
                del self.table[index][i]
                return True
        return False

    def listar_arquivos(self):
        for index, arquivos in self.table.items():
            print(f"Bucket {index}:")
            for arquivo in arquivos:
                print(f"  {arquivo}")

# Exemplo de uso
if __name__ == "__main__":
    # Criar uma tabela hash
    tabela = HashTable()

    # Adicionar arquivos à tabela hash
    tabela.adicionar_arquivo(Arquivo("relatorio.pdf", "/documentos/relatorio.pdf", 1024))
    tabela.adicionar_arquivo(Arquivo("foto.jpg", "/imagens/foto.jpg", 2048))
    tabela.adicionar_arquivo(Arquivo("dados.csv", "/planilhas/dados.csv", 512))
    tabela.adicionar_arquivo(Arquivo("backup.zip", "/backup/backup.zip", 4096))

    print("\nLista de Arquivos na Tabela Hash:")
    tabela.listar_arquivos()

    # Buscar um arquivo
    nome_busca = "dados.csv"
    arquivo_encontrado = tabela.buscar_arquivo(nome_busca)
    if arquivo_encontrado:
        print(f"\nArquivo encontrado: {arquivo_encontrado}")
    else:
        print(f"\nArquivo '{nome_busca}' não encontrado")

    # Remover um arquivo
    nome_remover = "foto.jpg"
    if tabela.remover_arquivo(nome_remover):
        print(f"\nArquivo '{nome_remover}' removido com sucesso")
    else:
        print(f"\nArquivo '{nome_remover}' não encontrado para remoção")

    print("\nLista de Arquivos após Remoção:")
    tabela.listar_arquivos()
