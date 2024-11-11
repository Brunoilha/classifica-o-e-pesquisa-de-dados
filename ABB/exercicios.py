class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f"Produto [ID={self.id}, Nome={self.nome}, Descrição={self.descricao}, Preço={self.preco:.2f}]"

class Node:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None


class BST:
    def __init__(self):
        self.raiz = None

  
    def inserir(self, produto):
        self.raiz = self._inserir_recursivo(self.raiz, produto)

    def _inserir_recursivo(self, raiz, produto):
        if raiz is None:
            return Node(produto)
        if produto.id < raiz.produto.id:
            raiz.esquerda = self._inserir_recursivo(raiz.esquerda, produto)
        elif produto.id > raiz.produto.id:
            raiz.direita = self._inserir_recursivo(raiz.direita, produto)
        return raiz

    def buscar(self, id):
        resultado = self._buscar_recursivo(self.raiz, id)
        return resultado.produto if resultado else None

    def _buscar_recursivo(self, raiz, id):
        if raiz is None or raiz.produto.id == id:
            return raiz
        if id < raiz.produto.id:
            return self._buscar_recursivo(raiz.esquerda, id)
        return self._buscar_recursivo(raiz.direita, id)

  
    def remover(self, id):
        self.raiz = self._remover_recursivo(self.raiz, id)

    def _remover_recursivo(self, raiz, id):
        if raiz is None:
            return None
        if id < raiz.produto.id:
            raiz.esquerda = self._remover_recursivo(raiz.esquerda, id)
        elif id > raiz.produto.id:
            raiz.direita = self._remover_recursivo(raiz.direita, id)

if __name__ == "__main__":
    bst = BST()

    # Inserindo produtos
    bst.inserir(Produto(30, "Teclado", "Teclado mecânico", 250.00))
    bst.inserir(Produto(20, "Mouse", "Mouse sem fio", 150.00))
    bst.inserir(Produto(40, "Monitor", "Monitor 4K", 1200.00))
    bst.inserir(Produto(10, "Cadeira", "Cadeira gamer", 800.00))

    # Buscar um produto pelo ID
    produto = bst.buscar(20)
    if produto:
        print(f"\nProduto encontrado: {produto}")
    else:
        print("\nProduto não encontrado.")

  
    print("\nLista de produtos em ordem crescente:")
    bst.listar_em_ordem()

    
    print("\nRemovendo o produto com ID 20")
    bst.remover(20)
    print("\nLista de produtos após a remoção:")
    bst.listar_em_ordem()

