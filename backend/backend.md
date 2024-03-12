# Backend 

neste readme estará todo o passo a passo de como eu fiz a API usando o djangorestframework

## inicializando o backend

primeiramente precisamos criar um ambiente virtual em python e ativa-ló:

```bash
$ python3 -m venv venv
$ source ./venv/bin/activate
```

agora precisamos instalar o django e o djangorestframewok:

```bash
$ pip install django
$ pip install djangorestframework
```

criaremos um projeto em **django** chamado `backend`:

```bash
$ django-admin startproject backend
```

no arquivo de configurações `settings.py` do diretorio backend coloremos:

```python
    INSTALLED_APPS = [
    ...
    'rest_framework',
    ]
```

## Criando os modelos e aplicações do projeto