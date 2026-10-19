# Avaliação Institucional

## Descrição

Projeto desenvolvido para a Mini Avaliação Institucional da disciplina de Laboratório de Programação Back-end. O sistema utiliza Django para disponibilizar uma API que permite consultar alunos, disciplinas e avaliações institucionais.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- Git

## Estrutura do projeto

- `backend/config/`: configurações principais do projeto Django.
- `backend/alunos/`: cadastro e consulta de alunos.
- `backend/disciplinas/`: cadastro e consulta de disciplinas.
- `backend/avaliacoes/`: cadastro e consulta de avaliações.
- `backend/requirements.txt`: dependências do projeto.

## Endpoints da API

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/alunos/` | Lista os alunos cadastrados. |
| GET | `/api/disciplinas/` | Lista as disciplinas cadastradas. |
| GET | `/api/avaliacoes/` | Lista todas as avaliações. |
| GET | `/api/avaliacoes/pendentes/` | Lista somente as avaliações pendentes. |

## Como executar o projeto

1. Entre na pasta `backend`.
2. Crie e ative um ambiente virtual Python.
3. Instale as dependências com `pip install -r requirements.txt`.
4. Execute as migrações com `python manage.py migrate`.
5. Inicie o servidor com `python manage.py runserver`.

## Conceitos

### Por que utilizar um ambiente virtual?

O ambiente virtual mantém as dependências do projeto isoladas das de outros projetos Python. Isso reduz conflitos entre versões de bibliotecas.

### Por que dividir o projeto em três aplicativos?

A divisão em `alunos`, `disciplinas` e `avaliacoes` organiza o código por responsabilidade, facilitando a manutenção e a evolução do sistema.

### Qual é a diferença entre `makemigrations` e `migrate`?

`makemigrations` cria arquivos que registram as alterações nos modelos. `migrate` aplica essas alterações ao banco de dados. Primeiro criamos as migrações; depois as aplicamos.

## Banco de dados

O projeto utiliza SQLite durante o desenvolvimento. O banco de dados local não deve ser enviado ao repositório Git.
