from app.py import app
from model2 import itembiblioteca, livro, manga, revista, dvd, usuario
from datetime import datetime, timedelta
from flask import render_template, request, redirect, url_for


class BibliotecaController:
    def __init__(self):
        self.bib = biblioteca()
    
    # CRUD de itens
    def adicionar_livro(self, id_item, titulo, autor, ano_publicacao, genero):
        livro1 = livro(id_item, titulo, autor, ano_publicacao, genero)
        self.bib.adicionar_item(livro1)
    
    def adicionar_manga(self, id_item, titulo, autor, ano_publicacao, volume):
        manga1 = manga(id_item, titulo, autor, ano_publicacao, volume)
        self.bib.adicionar_item(manga1)
    
    def adicionar_revista(self, id_item, titulo, autor, ano_publicacao, edicao):
        revista1 = revista(id_item, titulo, autor, ano_publicacao, edicao)
        self.bib.adicionar_item(revista1)

    def adicionar_dvd(self, id_item, titulo, autor, ano_publicacao, duracao):
        dvd1 = dvd(id_item, titulo, autor, ano_publicacao, duracao)
        self.bib.adicionar_item(dvd1)
    
    def remover_item(self, id_item):
        return self.bib.remover_item(id_item)
    
    # CRUD de usuários
    def registrar_usuario(self, id_usuario, nome, email):
        usuario1 = usuario(id_usuario, nome, email)
        self.bib.registrar_usuario(usuario1)
    
    def remover_usuario(self, id_usuario):
        return self.bib.remover_usuario(id_usuario)

    # Empréstimos e devoluções
    def emprestar(self, id_usuario, id_item, dias=7):
        return self.bib.emprestar_item(id_usuario, id_item, dias)
    
    def devolver(self, id_usuario, id_item):
        return self.bib.devolver_item(id_usuario, id_item)
    
    # Listagens e buscas
    def listar_itens_disponiveis(self):
        return self.bib.listar_itens_disponiveis()
    
    def buscar_item(self, titulo):
        return self.bib.buscar_item(titulo)
    
    def listar_itens_emprestados_usuario(self, id_usuario):
        if id_usuario in self.bib.usuarios:
            return self.bib.usuarios[id_usuario].listar_itens_emprestados()
        return []

    def historico(self):
        return self.bib.historico
