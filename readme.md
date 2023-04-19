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
`church`            | GET    | Listar todas as Igrejas
`member_church`     | POST   | Criar um relacionamento entre Membro-Igreja
`member_church/:id` | GET    | Buscar um relacionamento entre Membro-Igreja
`member_church/:id` | PATCH  | Alterar um relacionamento entre Membro-Igreja
`bus`               | GET    | Listar todos os Onibus
`bus/:id`           | GET    | Obter os dados de um ônibus
`bus`               | POST   | Criar um novo ônibus
`bus/:id`           | PATCH  | Editar um ônibus
`bus/:id`           | DELETE | Excluir um ônibus
