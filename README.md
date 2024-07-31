Anotações sobre django:

# Primeiramente

Criando um ambiente virtual:

```bash
python3 -m venv venv
```

Ativando um ambiente virtual

```bash
source venv/bin/activate
```

Desativando um ambiente virtual

```bash
deactivate
```

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

2. **Criar um projeto django**

É uma boa prática chamar o projeto de setup ou config

```bash
django-admin startproject setup
```

**Iniciar uma aplicação/projeto em django**

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

### Como eu faço que o Django reconheça o app ?

Passando a referÊncia do settings.py, passando o caminho como boa prática:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'galeria.apps.GaleriaConfig'
]
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

## Enviando dados via render

- Para enviar dados como um dicionário para a página principal, basta por, abrir chaves e os anotar

```python
dados = {
        1: {"nome": "nebulosa de carina",
            "legenda": "webbtelecope.org / NASA / James Webb"
            },
        2: {"nome": "Galáxia NGC 1079",
            "legenda": "nasa.or / NASA / Hubble"
            }
}
        return render(request, 'galeria/index.html', {"cards": dados})
```

- Para renderizar isso em um html, deve-se usar da seguinte maneira, se for laço for:

```html
<!-- Key e value-->
{% for foto_id, info in cards.items %}
<li class="card">
  <a href="{% url 'imagem' %}">
    <img
      class="card__imagem"
      src="{% static '/assets/imagens/galeria/carina-nebula.png' %}"
      alt="foto"
    />
  </a>
  <span class="card__tag">Estrelas</span>
  <div class="card__info">
    <p class="card__titulo">{{info.nome}}</p>
    <div class="card__texto">
      <p class="card__descricao">{{info.legenda}}</p>
      <span>
        <img
          src="{% static '/assets/ícones/1x/favorite_outline.png' %}"
          alt="ícone de coração"
        />
      </span>
    </div>
  </div>
</li>
{% endfor %}
```

## Banco de dados

Pode criar models dentro do arquivo models.py, com uma classe e valores dados pela orm do django, além de uma função que retorne o valor, molezinha.

```python
class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descrição = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
       return f'Fotografia nome=[{self.nome}]'
```

Ao fim de cada criação, deve-se rodar o comando de migração "traduzir para o projeto que o model é um banco de dados, onde o projeto fara a sua inserção":

```bash
 python manage.py makemigrations
```

Esse comando cria um documento dentro da pasta migrate, onde especifica as alterações, em seguida, se estiver tudo ok, faça o seguinte comando:

```bash
 python manage.py migrate
```

**Inserindo dados via shell**

```bash
python manage.py shell
from galeria.models import Fotografia
foto = Fotografia(nome="Nebulosa de Carina", legenda="webbtelescope.org / NASA / James Webb", foto="carina-nebula.png")
foto.save()
Fotografia.objects.all()
```

**Inserindo os dados no views.py**

```python
def index(request):
        fotografias = Fotografia.objects.all()
        return render(request, 'galeria/index.html', {"cards": fotografias})
```

```html
<ul class="cards__lista">
  {% if cards %}
  <!-- Key e value-->
  {% for fotografia in cards %}
  <li class="card">
    <a href="{% url 'imagem' %}">
      <img
        class="card__imagem"
        src="{% static '/assets/imagens/galeria/'%}{{fotografia.foto}}"
        alt="foto"
      />
    </a>
    <span class="card__tag">Estrelas</span>
    <div class="card__info">
      <p class="card__titulo">{{fotografia.nome}}</p>
      <div class="card__texto">
        <p class="card__descricao">{{fotografia.legenda}}</p>
        <span>
          <img
            src="{% static '/assets/ícones/1x/favorite_outline.png' %}"
            alt="ícone de coração"
          />
        </span>
      </div>
    </div>
  </li>
  {% endfor %} {% else %} {% endif %}
</ul>
```

## Passando referência

Deve-se passar como referência:

```html
<a href="{% url 'imagem' fotografia.id %}"></a>
```

Agora na rota:

```python
 path('imagem/<int:foto_id>', imagem, name='imagem'),
```

Passa-se o parâmetro na view.js

```python
from django.shortcuts import render, get_object_or_404
///código
def imagem(request, foto_id):
        fotografia = get_object_or_404(Fotografia, pk=foto_id)
        return render(request, 'galeria/imagem.html', {"fotografia": fotografia})
```

parâmetro referência

```html
<a href="{% url 'imagem' fotografia.id %}">></a>

Em seguida passo na rota:

<ul class="cards__lista">
  {% if cards %}
  <!-- Key e value-->
  {% for fotografia in cards %}
  <li class="card">
    <a href="{% url 'imagem' fotografia.id %}">
      <img
        class="card__imagem"
        src="{% static '/assets/imagens/galeria/'%}{{fotografia.foto}}"
        alt="foto"
      />
    </a>
    <span class="card__tag">Estrelas</span>
    <div class="card__info">
      <p class="card__titulo">{{fotografia.nome}}</p>
      <div class="card__texto">
        <p class="card__descricao">{{fotografia.legenda}}</p>
        <span>
          <img
            src="{% static '/assets/ícones/1x/favorite_outline.png' %}"
            alt="ícone de coração"
          />
        </span>
      </div>
    </div>
  </li>
  {% endfor %} {% else %} {% endif %}
</ul>
```

## Django Admin

Acessando o Django Admin

O Django Admin já está ativo por padrão. Para acessálo, basta inserir /admin no final da URL do seu projeto e pressionar "Enter".
bash: **127.0.0.1:8000/admin**

Criando um Superusuário

Para entrar no Django Admin, você precisa criar um superusuário com credenciais de administrador.

```bash
    python manage.py createsuperuser

    O comando irá te guiar pelas etapas de criação, solicitando:
        Nome de usuário: Digite o nome de usuário desejado.
        Email: Digite o email desejado.
        Senha: Digite a senha desejada.
        Confirmação da senha: Digite a senha novamente para confirmar.
```

Após criar o superusuário, acesse o Django Admin através da URL: **http://127.0.0.1:8000/admin**

Utilize o nome de usuário e a senha que você definiu durante a criação do superusuário para fazer login.
Documentação do [Django Admin](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/) .

## Manipulando admin

Posso manipular a busca, como será mostrado a tabela, quais são linkaveis:

```python
from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
  class ListandoFotografias(admin.ModelAdmin):
  list_display = ("id", "nome", "legenda")
  list_display_links = ("id", "nome")
  search_fields = ("nome",)
  list_filter = ("categoria",)
  list_per_page = 10
# Register your models here.
admin.site.register(Fotografia, ListandoFotografias)
```

## Alterando o banco de dados e novos campos

Para adicionar novos campos é só fazer as novas datas e em seguida fazer migrate

#### É importante entender os filtros do object, como no exemplo:

```python
 fotografias = Fotografia.objects.filter(publicada=True)
```
