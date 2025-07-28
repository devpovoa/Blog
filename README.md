Blog Pessoal - Projeto em Django
================================

Este projeto é um blog completo desenvolvido com Django, com foco em boas práticas de desenvolvimento web. O sistema foi estruturado para ser uma aplicação robusta, modular e escalável, com uso de Class-Based Views (CBV), arquitetura MVT e organização profissional de templates, URLs, views e modelos.

## Objetivo

--------

Desenvolver uma aplicação completa para portfólio, que reflita domínio prático com Django, incluindo autenticação, sistema de comentários, envio de e-mails, paginação, filtros e estrutura modular de templates e código.

* * *

Funcionalidades
---------------

* Publicação de posts com título, autor, conteúdo, categoria e data

* Sistema de comentários com moderação (`active_at=True`)

* Cadastro, login e logout de usuários

* Edição de perfil com upload de foto

* Recuperação e redefinição de senha via e-mail

* Página de contato com envio de e-mail e integração com WhatsApp

* Paginação de posts com tratamento de exceções

* Templates modulares e reutilizáveis

* Separação de views e URLs por responsabilidade

* * *

Tecnologias utilizadas
----------------------

* **Linguagem:** Python 3.12

* **Framework:** Django 5.2

* **Template engine:** Django Templates

* **Banco de Dados:** SQLite (modo desenvolvimento)

* **Estilização:** HTML5, CSS3, Bootstrap

* **Gerenciamento de ambiente:** `django-environ`

* **Validação de segurança:** reCAPTCHA v2

* **Manipulação de imagens:** Pillow

* **Envio de e-mails:** SMTP com variáveis de ambiente

* **Organização modular:** Separação por `views/`, `urls/`, `forms/`, `models/`, `templates/` em cada app

* * *

Dependências principais
-----------------------

    asgiref==3.9.1
    Django==5.2.4
    django-environ==0.12.0
    django-ranged-response==0.2.0
    django-recaptcha==4.1.0
    pillow==11.3.0
    sqlparse==0.5.3

* * *

Estrutura modular do projeto
----------------------------

    ├── accounts/
    │   ├── models/profile.py          # Modelo Profile com upload de imagem
    │   ├── forms/                     # Formulários de cadastro e edição de perfil
    │   ├── views/                     # Views divididas: autenticação e perfil
    │   ├── urls/user_urls.py          # URLs do módulo de usuários
    │   └── templates/accounts/        # Templates divididos por função: auth, password, profile
    
    ├── blog/
    │   ├── models/                    # Post, Comment, Category, About
    │   ├── forms/                     # Comentário e formulário de contato
    │   ├── views/                     # Views separadas por responsabilidade (posts, páginas)
    │   ├── urls/                      # URLs para posts e páginas estáticas
    │   ├── static/blog/               # CSS e imagens estáticas
    │   └── templates/blog/            # Templates de listagem, detalhe, sobre, contato
    
    ├── blogAdmin/
    │   ├── settings/                  # Configurações separadas por ambiente
    │   └── urls.py                    # Rotas principais do projeto
    
    ├── media/                         # Uploads organizados por pasta de usuário
    ├── manage.py                     # Entrada principal do projeto
    └── requirements.txt              # Dependências do projeto

* * *

Como executar localmente
------------------------

    # Crie e ative o ambiente virtual
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    
    # Instale as dependências
    pip install -r requirements.txt
    
    # Configure seu .env com SECRET_KEY, SMTP, etc.
    # Aplique as migrações e inicie o servidor
    python manage.py migrate
    python manage.py runserver

* * *

Considerações
-------------

Este projeto foi desenvolvido com foco em clareza de código, modularização e estruturação profissional. Ele reflete um padrão de qualidade que pode ser estendido para aplicações reais de blog, portfólio ou CMS simples. A arquitetura segue o padrão MVT do Django com organização orientada por funcionalidade e responsabilidade.

* * *


