Anotações sobre django:

# Visão Geral e Configuração do Django

## O que é Django?

Django é um framework web de alto nível escrito em Python, que promove o desenvolvimento rápido e um design limpo e pragmático. Ele é conhecido por sua simplicidade e capacidade de ajudar desenvolvedores a criarem aplicativos web complexos de forma rápida e eficiente.

### Principais Características do Django:

- **Interface Administrativa**: Interface administrativa gerada automaticamente.
- **ORM (Object-Relational Mapping)**: Mapeia modelos de dados para tabelas de banco de dados.
- **Segurança**: Fornece proteção integrada contra ameaças de segurança comuns.
- **Escalabilidade**: Escalável para aplicativos web simples e complexos.
- **Sistema de Templates**: Utiliza um sistema de templates poderoso e flexível.

## Instalação e Configuração

### Documentação oficial: https://docs.djangoproject.com/en/5.0/

### Pré-requisitos

Certifique-se de ter o Python instalado. O Django requer o Python 3.6 ou superior.

### Passo a Passo da Instalação

1. **Instalar Django**

   Abra o terminal e execute o seguinte comando para instalar o Django usando `pip`:

   ```bash

   pip install django

   ```

### Iniciciar uma aplicação django

```bash
python manage.py runserver
```

### Algumas anotações importantes:

**startapp x start projetc**

O projeto é o conjunto de todas as aplicações, já o app seria uma funcionalidade, podendo existir vários em projeto.

#### Como eu o crio ?

```bash
python manage.py startapp "nome"

```

### Trabalhando dentro de um app

**views.py**:
Responsável por verificar as rotas, seguindo exemplo de aplicação:

```Python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        return HttpResponse('<h1>Alura Space</h1>')
```

Porém, se quiser que ela seja vista na rota do projeto, deve mexer adicionar a rota no **urls.py** do arquivo de configuração.

```Python
from django.contrib import admin
from django.urls import path
from galeria.views import index
urlpatterns = [
        path('admin/', admin.site.urls),
        path('', index),
]
```

**Isolando urls e boa prática**

primeiramente, crias o arquivo urls.py no app, nele ficarão todas as rotas do app, assim como no original, em seguida, importa o método includes junto com o path o aplica a seguinte configuração do urls.py do setup:

```Python
from django.contrib import admin
from django.urls import path, include
from galeria.views import index
urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('galeria.urls')),
]
```

### Criando templates

Para criar um template, basta criar um diretório, de preferência no nível da pasta original, em e passá-lo no dir:

```Python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Em seguida deve-se passar o template na o arquivo view.py na rota que deseja:

from django.shortcuts import render

```Python
# Create your views here.
def index(request):
        return render(request, 'index.html')
```

### Criando arquivos estáticos

O procedimento é o mesmo, mas agora vamos no STATICFILES_DIR

```Python
//caminho de onde estarão os arquivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]
//onde o python vai coletar
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

```

depois usa-se os seguintes comandos estáticos: **python manage.py collectstatic**

Em seguida, deve-se colocar no topo da página o seguinte comando: **{% load static %}**

Por fim, onde tem o arquivo css, indica-se o static:

```html
<link rel="stylesheet" href="{% static '/styles/style.css' %}" />
```

IMPORTANTE: para todos os arquivos statics que temos, deve-se por o {% static %}, como no exemplo:

```html
<img
  src="{% static '/assets/ícones/1x/favorite_outline.png' %}"
  alt="ícone de coração"
/>
```

### URL name

Definindo nome da urls para alterar rotas de imagem, dá um nome à rota

```python
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]
```

Depois altera no url:

```html
<a href="{% url 'imagem' %}"></a>
```

### DRY - Don't repeat yourself e Base

Não repita o código, para isso o django permite que você crie uma blocos, para evitar repetição, segundo a sua aplicação feita da seguinte maneira:

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    //código head
  </head>

  <body>
    //necessário para deniir as partes {% block content %} {% endblock %}
  </body>
</html>
```

```html
- depois, nas partes que for adicionar, só usar as seguintes tags {% extends
'galeria/base.html' %} {% load static %} {% block content %} /*Conteúdo html*/
{% endblock%}
```

- ATENÇÃO: Deve-se ficar atento ao encerramento das tags.

### Partials

- Pedaços do código que são repetidos, imagino que seja como o dry, deve-se criar um artigo da seguinte maneira "\_nome_do_arquivo".

por preferÊncia, o coloca no base:

```html
<body>
  {% block content %} {% endblock %} {% include 'galeria/partials/_footer.html'
  %}
</body>
```
