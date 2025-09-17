from datetime import datetime, timedelta

class itembiblioteca:
    def __init__(self, id_item, titulo, autor, ano_publicacao, tipo_item):
        self.id_item = id_item # ID único do item
        self.titulo = titulo # Título do item
        self.autor = autor # Autor do item
        self.ano_publicacao = ano_publicacao  # Ano de publicação (addicionada por minha pessoa ((mod))
        self.tipo_item = tipo_item # Tipo: Livro, Mangá, Revista, DVD
        self.disponivel = True # Disponibilidade do item (addicionada por minha pessoa)
        self.data_emprestimo = None # Data de empréstimo (addicionada por minha pessoa)
        self.data_devolucao = None # Data de devolução prevista (addicionada por minha pessoa)
        
    def emprestar(self, dias=7):
        if self.disponivel:
            self.disponivel = False
            self.data_emprestimo = datetime.now()
            self.data_devolucao = self.data_emprestimo + timedelta(days=dias)
            return True
        return False
        
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            self.data_emprestimo = None
            self.data_devolucao = None
            return True
        return False
        
    def descricao(self):
        return f"{self.tipo_item}: {self.titulo} por {self.autor} ({self.ano_publicacao}) - {'Disponível' if self.disponivel else 'Emprestado até ' + self.data_devolucao.strftime('%d/%m/%Y')}"
        

class usuario:
    def __init__(self, id_usuario, nome, email):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.itens_emprestados = []
        
    def listar_itens_emprestados(self):
        return [item.descricao() for item in self.itens_emprestados]
        

class biblioteca:
    def __init__(self):
        self.itens = {}
        self.usuarios = {}
        self.historico = []  # novo: guarda histórico de empréstimos e devoluções futuramente substituido por um data base
        
    def adicionar_item(self, item):
        self.itens[item.id_item] = item
        
    def remover_item(self, id_item):
        if id_item in self.itens:
            del self.itens[id_item]
            return True
        return False
        
    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario
        
    def remover_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            return True
        return False
        
    def buscar_item(self, titulo):
        return [item.descricao() for item in self.itens.values() if titulo.lower() in item.titulo.lower()]
        
    def listar_itens_disponiveis(self):
        return [item.descricao() for item in self.itens.values() if item.disponivel]

    # 📌 Controle centralizado de empréstimo (centraliza todas as bibliotecas para poupar espaço e maximizar o trabalho)
    def emprestar_item(self, id_usuario, id_item, dias=7):
        if id_usuario in self.usuarios and id_item in self.itens:
            usuario = self.usuarios[id_usuario]
            item = self.itens[id_item]
            if item.emprestar(dias):
                usuario.itens_emprestados.append(item)
                self.historico.append({
                    "acao": "emprestimo",
                    "usuario": usuario.nome,
                    "item": item.titulo,
                    "data": datetime.now().strftime("%d/%m/%Y %H:%M")
                })
                return True
        return False

    def devolver_item(self, id_usuario, id_item):
        if id_usuario in self.usuarios and id_item in self.itens:
            usuario = self.usuarios[id_usuario]
            item = self.itens[id_item]
            if item in usuario.itens_emprestados and item.devolver():
                usuario.itens_emprestados.remove(item)
                self.historico.append({
                    "acao": "devolucao",
                    "usuario": usuario.nome,
                    "item": item.titulo,
                    "data": datetime.now().strftime("%d/%m/%Y %H:%M")
                })
                return True
        return False


#___________Subclasses_______________#
class livro(itembiblioteca):
    def __init__(self, id_item, titulo, autor, ano_publicacao, genero):
        super().__init__(id_item, titulo, autor, ano_publicacao, "Livro")
        self.genero = genero
        
    def descricao(self):
        return f"{super().descricao()} - Gênero: {self.genero}"
        

class manga(itembiblioteca):
    def __init__(self, id_item, titulo, autor, ano_publicacao, volume):
        super().__init__(id_item, titulo, autor, ano_publicacao, "Mangá")
        self.volume = volume
        
    def descricao(self):
        return f"{super().descricao()} - Volume: {self.volume}"
        

class revista(itembiblioteca):
    def __init__(self, id_item, titulo, autor, ano_publicacao, edicao):
        super().__init__(id_item, titulo, autor, ano_publicacao, "Revista")
        self.edicao = edicao
        
    def descricao(self):
        return f"{super().descricao()} - Edição: {self.edicao}"
        

class dvd(itembiblioteca):
    def __init__(self, id_item, titulo, autor, ano_publicacao, duracao):
        super().__init__(id_item, titulo, autor, ano_publicacao, "DVD")
        self.duracao = duracao
        
    def descricao(self):
        return f"{super().descricao()} - Duração: {self.duracao} minutos"
        

# ___________________Exemplo de uso (pode ser removido em produção)______________#
if __name__ == "__main__":
    bib = biblioteca() #bib e baitolagem

    # Criando itens para adicionar na biblioteca
    livro1 = livro(1, "1984", "George Orwell", 1949, "Distopia")
    manga1 = manga(2, "Naruto", "Masashi Kishimoto", 1999, 1)
    revista1 = revista(3, "National Geographic", "Vários", 2020, "Março")
    dvd1 = dvd(4, "Inception", "Christopher Nolan", 2010, 148)
    
    # Adicionando itens na biblioteca
    bib.adicionar_item(livro1)
    bib.adicionar_item(manga1)
    bib.adicionar_item(revista1)
    bib.adicionar_item(dvd1)

    # Criando um usuário e registrando na biblioteca
    usuario1 = usuario(1, "Alice", "alice@example.com")
    bib.registrar_usuario(usuario1)
    
    # Emprestando um item para o usuário
    bib.emprestar_item(1, 1)  # Alice pega o livro 1984
    print(usuario1.listar_itens_emprestados())  
    
    # Listando itens disponíveis
    print(bib.listar_itens_disponiveis())
    
    # Devolvendo item
    bib.devolver_item(1, 1)
    print(usuario1.listar_itens_emprestados())
    print(bib.listar_itens_disponiveis())

    # Histórico de ações
    print("\nHistórico:")
    for h in bib.historico:
        print(h)
