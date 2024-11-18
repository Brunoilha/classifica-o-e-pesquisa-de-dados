class HashTable:
    def __init__(self, size):
        # Inicializa a tabela hash com um dicionário, onde cada chave é um índice (bucket) com uma lista vazia
        self.size = size
        self.table = {i: [] for i in range(size)}

    def hash_function(self, key):
        # Função de hash simples que usa o módulo do tamanho da tabela para calcular o índice
        return hash(key) % self.size

    def insert(self, key, value):
        # Calcula o índice usando a função de hash
        index = self.hash_function(key)
        # Insere o par (key, value) na lista correspondente ao índice
        self.table[index].append((key, value))

    def get(self, key):
        # Calcula o índice onde a chave deve estar
        index = self.hash_function(key)
        # Procura a chave no bucket correspondente
        for k, v in self.table[index]:
            if k == key:
                return v  # Retorna o valor associado à chave
        return None  # Retorna None se a chave não for encontrada

    def remove(self, key):
        # Calcula o índice onde a chave está armazenada
        index = self.hash_function(key)
        # Procura o par (key, value) para remover
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove o par da lista
                return True
        return False  # Retorna False se a chave não for encontrada

    def display(self):
        # Exibe o conteúdo da tabela hash
        for index, bucket in self.table.items():
            print(f"Bucket {index}: {bucket}")

# Exemplo de uso
if __name__ == "__main__":
    htable = HashTable(5)  # Tamanho da tabela hash é 5
    htable.insert("key1", "value1")
    htable.insert("key2", "value2")
    htable.insert("key3", "value3")
    htable.insert("key4", "value4")
    htable.insert("key5", "value5")
    
    print("Tabela Hash após inserções:")
    htable.display()
    
    print("\nValor associado a 'key1':", htable.get("key1"))  # Saída: "value1"
    print("Valor associado a 'key3':", htable.get("key3"))  # Saída: "value3"
    
    # Remover uma chave
    htable.remove("key2")
    print("\nTabela Hash após remoção de 'key2':")
    htable.display()
