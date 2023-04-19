# ICM BUS - API
API desenvolvida em Python-Django para o aplicativo de alocação de vagas nos ônibus que levam os membros da congregação para os seminários da Igreja Cristã Maranata.

## Requisitos
- Python 3.8
- Django 4.1.7
- Django Environ
- MongoEngine
- Django REST Framework
- Django REST Framework MongoEngine

## Instalação
Após o repositório ser clonado na máquina local, será necessário definir as variáveis de ambiente na pasta api_bus em um arquivo chamado ".env". As dependências do projeto devem ser instaladas a partir dos seguintes comandos:

```	
sudo apt install python3-pip
```	
```	
pip3 install django
```
```	
pip3 install django-environ
```	
```	
pip3 install mongoengine
```
```	
pip3 install djangorestframework
```
```	
pip3 install django-rest-framework-mongoengine
```

## Iniciando a API
O seguinte comando deverá ser executado para iniciar o servidor.
```
python3 manage.py runserver
```

## Endpoints Disponíveis
Os seguintes endpoints estão disponíveis para utilização nesta API:

Endpoint            | HTTP   | Result
--                  | --     | --
`member`            | GET    | Listar todos os Membros
`member/:id`        | GET    | Obter os dados de um Membro
`member`            | POST   | Cadastrar um novo Membro
`member/:id`        | PATCH  | Editar um Membro
`member/:id`        | DELETE | Excluir um Ônibus
`church`            | GET    | Listar todas as Igrejas
`church/:id/list_members` | GET | Listar os Membros vinculados a uma Igreja
`member_church`     | POST   | Cadastrar um relacionamento entre Membro-Igreja
`member_church/:id` | GET    | Buscar um relacionamento entre Membro-Igreja
`member_church/:id` | PATCH  | Alterar um relacionamento entre Membro-Igreja
`bus`               | GET    | Listar todos os Ônibus
`bus/:id`           | GET    | Obter os dados de um Ônibus
`bus/:id/list_members` | GET | Obter os Membros cadastrados em um Ônibus
`bus`               | POST   | Cadastrar um novo Ônibus
`bus/:id`           | PATCH  | Editar um Ônibus
`bus/:id`           | DELETE | Excluir um Ônibus
`member_bus`        | POST   | Cadastar membro em um Ônibus
`member_bus/:id`    | DELETE | Remover membro de um Ônibus
