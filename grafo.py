import networkx as nx
from io import BytesIO
import matplotlib.pyplot as plt

def fazGrafo(materia):
  grafo = nx.DiGraph()

  grafo.add_node("Cálculo 1")
  grafo.add_node("Cálculo 2")
  grafo.add_node("Métodos Numéricos para Engenharia")
  grafo.add_node("Probabilidade e Estatística Aplicada à Engenharia")
  grafo.add_node("Projeto e Análisede Algoritmos")
  grafo.add_node("Física 1")
  grafo.add_node("Algoritmos e Programação de Computadores")
  grafo.add_node("Desenho Industrial Assistido por Computador")
  grafo.add_node("Engenharia e Ambiente")
  grafo.add_node("Introdução à Engenharia")
  grafo.add_node("Física 1 Experimental")
  grafo.add_node("Introdução à Álgebra Linear")
  grafo.add_node("Engenharia Econômica")
  grafo.add_node("Humanidades e Cidadania")
  grafo.add_node("Teoria de Eletrônica Digital 1")
  grafo.add_node("Prática de Eletrônica Digital 1")
  grafo.add_node("Orientação a Objetos")
  grafo.add_node("Matemática Discreta 1")
  grafo.add_node("Gestão da Produção e Qualidade")
  grafo.add_node("Métodos de Desenvolvimento de Software")
  grafo.add_node("Estruturas de Dados 1")
  grafo.add_node("Fundamentos de Arquiteturas de Computadores")
  grafo.add_node("Matemática Discreta 2")
  grafo.add_node("Projeto Integrador de Engenharia 1")
  grafo.add_node("Interação Humano Computador")
  grafo.add_node("Requisitos de Software")
  grafo.add_node("Sistemas de Banco de Dados 1")
  grafo.add_node("Fundamentos de Sistemas Operacionais")
  grafo.add_node("Compiladores 1")
  grafo.add_node("Estruturas de Dados 2")
  grafo.add_node("Qualidade de Software 1")
  grafo.add_node("Testes de Software")
  grafo.add_node("Arquitetura e Desenho de Software")
  grafo.add_node("Fundamentos de Redes de Computadores")
  grafo.add_node("Sistemas de Banco de Dados 2")
  grafo.add_node("Projeto de algoritmos")
  grafo.add_node("Técnicas de Programação em Plataformas Emergentes")
  grafo.add_node("Paradigmas de Programação")
  grafo.add_node("Fundamentos de Sistemas Embarcados")
  grafo.add_node("Programação para Sistemas Paralelos e Distribuídos")
  grafo.add_node("Engenharia de Produto de Software")
  grafo.add_node("Gerência de Configuração e Evolução de Software")
  grafo.add_node("Estágio Supervisionado")
  grafo.add_node("Trabalho de Conclusão de Curso 1")
  grafo.add_node("Projeto Integrador de Engenharia 2")
  grafo.add_node("Trabalho de Conclusão de Curso 2")
  #grafo.add_node("")


  grafo.add_edges_from([("Cálculo 1", "Cálculo 2"), ("Cálculo 1", "Probabilidade e Estatística Aplicada à Engenharia") , ("Cálculo 1", "Projeto e Análisede Algoritmos"),
                          ("Algoritmos e Programação de Computadores", "Orientação a Objetos"), ("Algoritmos e Programação de Computadores", "Estruturas de Dados 1"),
                          ("Desenho Industrial Assistido por Computador", "Interação Humano Computador"),
                          ("Cálculo 2", "Métodos Numéricos para Engenharia"),
                          ("Introdução à Álgebra Linear", "Teoria de Eletrônica Digital 1"), ("Introdução à Álgebra Linear", "Prática de Eletrônica Digital 1"),
                          ("Engenharia Econônica", "Gestão da Produção e Qualidade"),
                          ("Teoria de Eletrônica Digital 1", "Fundamentos de Arquiteturas de Computadores"),
                          ("Orientação a Objetos", "Projeto Integrador de Engenharia 1"), ("Orientação a Objetos", "Paradigmas de Programação"), ("Orientação a Objetos", "Métodos de Desenvolvimento de Software"),
                          ("matemática Discreta 1", "Matemática Discreta 2"),
                          ("Gestão da Produção e Qualidade", "Qualidade de Software 1"),
                          ("Métodos de Desenvolvimento de Software", "Requisitos de Software"), ("Métodos de Desenvolvimento de Software", "Testes de Software"), ("Métodos de Desenvolvimento de Software", "Interação Humano Computador"),
                          ("Estrutura de Dados 1", "Compiladores 1"), ("Estrutura de Dados 1", "Estrutura de Dados 2"), ("Estrutura de Dados 1", "Projeto de Algoritmos"),
                          ("Fundamentos de Arquiteturas de Computadores", "Fundamentos de Sistemas Operacionais"),
                          ])

  #print(nx.shortest_path(grafo, source=grafo, target= "Métodos Numéricos para Engenharia"))
  #print(nx.all_simple_paths(grafo, source="Cálculo 1", target="Métodos Numéricos para Engenharia"))
  materia = "Introdução à Álgebra Linear"
  roots = []
  leaves = []
  caminho = []
  caminhos = []
  for node in grafo.nodes :
    if grafo.in_degree(node) == 0 : # it's a root
      roots.append(node)
    elif grafo.out_degree(node) == 0 : # it's a leaf
      leaves.append(node)

  for root in roots :
    for leaf in leaves :
      for path in nx.all_simple_paths(grafo, root, leaf) :
          if materia in path:
              #print(path)
              caminho = path
              caminhos.append(caminho)

  #print(caminhos)

  G = nx.DiGraph()
  #for j in range(len(caminhos)):
  for i in range(len(caminhos)):
    for j in range(len(caminhos[i]) - 1):
      G.add_edge(caminhos[i][j].replace(" ", "\n"), caminhos[i][j+1].replace(" ", "\n"))
  return G, caminhos