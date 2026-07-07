# 🎓 SafeEdu API

API REST desenvolvida em **Django 6 + Django REST Framework** para o projeto **WorldSkills - SafeEdu**.

O projeto disponibiliza endpoints para gerenciamento de escolas, comentários, reações, imagens e autenticação JWT, além de documentação automática com Swagger (OpenAPI).

---
## 🎯 Objetivos Educacionais

Este projeto foi desenvolvido com fins didáticos para demonstrar a construção de uma API REST utilizando Django REST Framework.

Os principais conceitos abordados são:

- Estrutura de projetos Django
- Models e Migrações
- Serializers
- ViewSets
- Rotas
- Autenticação JWT
- Swagger / OpenAPI
- Upload de arquivos
- Deploy no PythonAnywhere
---

## 🚀 Tecnologias

- Python 3.13+
- Django
- Django REST Framework
- DRF Spectacular (Swagger/OpenAPI)
- Simple JWT
- SQLite (desenvolvimento)
- PythonAnywhere (deploy)

---

## 📚 Funcionalidades

- ✅ Autenticação JWT
- ✅ Validação de Token
- ✅ Cadastro de Escolas
- ✅ Comentários
- ✅ Reações
- ✅ Upload de Imagens
- ✅ Mensagem Motivacional (MOTD)
- ✅ Swagger
- ✅ Redoc
- ✅ Health Check

---

## 📂 Estrutura do Projeto

```
safeeduAPI/
│
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── safeeduAPI/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
├── static/
├── requirements.txt
└── manage.py
```

---

# Instalação

## 1 - Clone o projeto

```bash
git clone https://github.com/ProfGregorio/worldskills-api.git
```

Entre na pasta

```bash
cd worldskills-api
```

---

## 2 - Criar ambiente virtual

Windows

```bash
python -m venv .venv
```

Linux

```bash
python3 -m venv .venv
```

Ativar

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## 3 - Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4 - Executar migrações

```bash
python manage.py migrate
```

---

## 5 - Criar superusuário

```bash
python manage.py createsuperuser
```

---

## 6 - Executar servidor

```bash
python manage.py runserver
```

A API estará disponível em

```
http://127.0.0.1:8000
```

---

# Documentação

Swagger

```
http://127.0.0.1:8000/api/docs/
```

Redoc

```
http://127.0.0.1:8000/api/redoc/
```

Schema OpenAPI

```
http://127.0.0.1:8000/api/schema/
```

---

# 📌 Endpoints da API

Abaixo estão os principais endpoints disponíveis na WorldSkills API.


- 🔐 Autenticação utilizando JWT.
- 📖 Documentação automática com Swagger (OpenAPI).
- 💬 Filtro de comentários por escola.
- ❤️ Sistema de reações (Like e Favorito).
- 🖼️ Upload de imagens utilizando `ImageField`.
- 👤 Consulta de imagens por usuário.
- 🎲 Retorno aleatório da Mensagem do Dia (MOTD).
- 📈 Endpoint de Health Check para monitoramento da API.

---

## 🔐 Autenticação

| Método | Endpoint | Descrição | Autenticação |
|---------|----------|-----------|--------------|
| POST | `/api/auth/` | Realiza o login do usuário utilizando e-mail ou nome de usuário e retorna um Access Token e Refresh Token JWT. | ❌ |
| GET | `/api/validate_token/` | Verifica se o Access Token enviado é válido e retorna as informações do usuário autenticado. | ✅ |

---

## 🏫 Escolas

| Método | Endpoint | Descrição | Autenticação |
|---------|----------|-----------|--------------|
| GET | `/api/escolas/` | Lista todas as escolas cadastradas na plataforma. | ❌ |
| GET | `/api/escolas/{id}/` | Retorna os dados completos de uma escola específica. | ❌ |

---

## 💬 Comentários

| Método | Endpoint | Descrição | Autenticação |
|---------|----------|-----------|--------------|
| GET | `/api/comentarios/` | Lista todos os comentários cadastrados. | ✅ |
| GET | `/api/comentarios/?id_escola={id}` | Lista apenas os comentários de uma escola específica. | ✅ |
| GET | `/api/comentarios/escola/{id}/` | Lista os comentários da escola ordenados pela data mais recente. | ✅ |
| POST | `/api/comentarios/` | Cadastra um novo comentário para uma escola. | ✅ |

---

## ❤️ Reações

| Método | Endpoint | Descrição | Autenticação |
|---------|----------|-----------|--------------|
| GET | `/api/reacoes/` | Lista todas as reações registradas. | ✅ |
| POST | `/api/reacoes/` | Adiciona uma reação (Like ou Favorito) a um comentário. | ✅ |

---

## 🖼️ Imagens (Prints)

| Método | Endpoint | Descrição | Autenticação |
|---------|----------|-----------|--------------|
| GET | `/api/imagens/` | Lista todas as imagens enviadas pelos usuários. | ✅ |
| GET | `/api/imagens/usuario/{email}/` | Lista apenas as imagens enviadas por um determinado usuário. | ✅ |
| POST | `/api/imagens/` | Realiza o upload de uma nova imagem (print). | ✅ |

---

## 💡 Mensagem Motivacional

| Método | Endpoint | Descrição | Autenticação |
|---------|----------|-----------|--------------|
| GET | `/api/motd/` | Retorna aleatoriamente uma mensagem motivacional cadastrada no banco de dados. | ❌ |

---

## ❤️ Health Check

| Método | Endpoint | Descrição | Autenticação |
|---------|----------|-----------|--------------|
| GET | `/health` | Endpoint utilizado para verificar se a API está online e respondendo corretamente. | ❌ |

---


## 🔑 Fluxo de Autenticação

```text
POST /api/auth/
        │
        ▼
Recebe Access Token + Refresh Token
        │
        ▼
Swagger → Authorize
        │
Bearer <access_token>
        │
        ▼
Consumir os endpoints protegidos
```

### Legenda

| Símbolo | Significado |
|----------|-------------|
| ✅ | Requer autenticação JWT |
| ❌ | Acesso público |

---

# Fluxo de autenticação - Exemplo

1. Faça login em

```
POST /api/auth/
```

Exemplo

```json
{
    "email":"gregmaster",
    "password":"123456"
}
```

A API retornará

```json
{
    "access":"...",
    "refresh":"..."
}
```

Clique em **Authorize** no Swagger e informe

```
Bearer seu_access_token
```

Agora todos os endpoints protegidos estarão disponíveis.

---
---

# ▶️ Executando Localmente

Após iniciar o servidor:

```bash
python manage.py runserver
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

ou

```
http://localhost:8000
```

---

## 🌐 Acessando pela rede local

Para permitir que outros dispositivos da mesma rede (computadores ou celulares) acessem a API, execute:

```bash
python manage.py runserver 0.0.0.0:8000
```

Descubra o endereço IP da máquina.

### Windows

```bash
ipconfig
```

Procure pelo **Endereço IPv4**, por exemplo:

```
192.168.1.105
```

### Linux / macOS

```bash
ip addr
```

ou

```bash
ifconfig
```

Depois acesse pelo navegador ou aplicativo utilizando:

```
http://192.168.1.105:8000
```

Exemplos:

```
http://192.168.1.105:8000/api/docs/
```

```
http://192.168.1.105:8000/api/redoc/
```

```
http://192.168.1.105:8000/api/escolas/
```

---

> **Importante**
>
> Certifique-se de que:
>
> - Os dispositivos estejam conectados à mesma rede.
> - O firewall do sistema permita conexões na porta **8000**.
> - O Django permita o acesso pelo endereço IP configurando o `ALLOWED_HOSTS` no arquivo `settings.py`.

Exemplo:

```python
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "192.168.1.105",
]
```

Durante o desenvolvimento também é possível utilizar:

```python
ALLOWED_HOSTS = ["*"]
```

> **Atenção:** utilize `["*"]` apenas em ambiente de desenvolvimento. Em produção, informe explicitamente os domínios ou endereços IP permitidos.
---


# 🌐 Executando em Produção (Opcional)

Este projeto foi desenvolvido para ser facilmente publicado em serviços de hospedagem para aplicações Python.

Uma das opções utilizadas durante o desenvolvimento foi o **PythonAnywhere (plano gratuito)**.

Caso deseje publicar sua própria instância da API, siga os passos descritos na seção **Deploy no PythonAnywhere**.

> **Observação:** O plano gratuito do PythonAnywhere pode suspender a aplicação após um período de inatividade. Por esse motivo, este repositório não disponibiliza uma instância pública permanente da API.

> 💡 **Dica:** Caso utilize o plano gratuito do PythonAnywhere, lembre-se de alterar o nome da aplicação, criar seu próprio superusuário e configurar o `ALLOWED_HOSTS` de acordo com o domínio fornecido pelo serviço.

## Deploy no PythonAnywhere
Após criar a aplicação:

Instalar dependências

```bash
pip install -r requirements.txt
```

Executar migrações

```bash
python manage.py migrate
```

Coletar arquivos estáticos

```bash
python manage.py collectstatic
```

Configurar o arquivo **WSGI**

```python
import os
import sys

path = '/home/SEU_USUARIO/safeedu-api-2025'

if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'safeeduAPI.settings'
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Depois basta clicar em **Reload**.

---

# Health Check

```
GET /health
```

Resposta

```json
{
    "api":"SafeEdu API",
    "version":"1.0",
    "status":"online"
}
```

---

# Autor

**Gregório Queiroz**

Professor • Desenvolvedor • Especialista em Desenvolvimento Web

GitHub

https://github.com/ProfGregorio

---

# Licença

MIT