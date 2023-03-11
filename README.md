# Inventory Report POO - Computer Science Project

Projeto em **Python** com framework **Flask** para treinar conceitos de POO!
Leitura e extração de dados de arquivos ```.csv```, ```.json``` e ```.xml``` utilizando programação orientada à objetos e aplicando padrões de projetos.

Projeto 31 da [Trybe](https://wwww.betrybe.com), módulo de Ciência da Computação.

## O Projeto

* Implementar uma classe com habilidades de lógica de programação que retorne um relatório simples a partir dos dados recebidos.
* Implementar uma classe herdeira que retorne um relatório completo a partir do relatório simples.
* Implementar classes separadas para leitura dos arquivos ```.csv```, ```.json``` e ```.xml```.
* Refatorar com o padrão de projeto Strategy: criar uma classe abstrata "Importer" para ser a interface da estratégia que terá três classes de estratégias herdeiras ("CsvImporter", "JsonImporter" e "XmlImporter").

## Instalação 


#### 1- Clonar o repositório

```git clone git@github.com:sallybdiament/Project-31-Inventory-Report-Python.git```

#### 2 - Crie o ambiente virtual para o projeto

python3 -m venv .venv && source .venv/bin/activate

#### 3 - Instalar as dependências

python3 -m pip install -r dev-requirements.txt

#### 4 - Executar os testes:

```python3 -m pytest tests/nomedoarquivo.py -k nome_da_func_de_tests```

ou para executar um teste específico:
```python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste```


## Tecnologias
- Python
- Pytest (unittest.mock, fixture, etc)
- Flake8 e Black
- Exceptions (try, except, elsse, finally)
- POO in Python
- Desgin Patterns in Python
- Manipulation of CSV, JSON and XML data (with, open, json, csv, DictReader, etc)
