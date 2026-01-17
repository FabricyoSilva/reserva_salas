## 🏢 Sistema de Reserva de Salas
Este é um projeto de gestão de espaços desenvolvido em Django e Tailwind CSS. O sistema permite que usuários se cadastrem e reservem salas para reuniões ou estudos, enquanto administradores possuem um painel exclusivo para gerenciar salas, categorias e visualizar todas as ocupações através de uma barra lateral de controle.

---

## 🚀 Funcionalidades
Para Usuários Comuns
Cadastro e Login Personalizado: Autenticação baseada em e-mail e senha.

Reserva de Salas: Interface intuitiva para escolher data e horário.

Gestão de Reservas: Página "Minhas Reservas" para visualizar, alterar horário ou cancelar agendamentos.

Para Administradores (Staff)
Dashboard Exclusivo: Sidebar lateral para navegação rápida entre as ferramentas de gestão.

Gestão de Salas: Cadastro de novas salas diretamente pela interface do site (sem precisar do Django Admin).

Gestão de Categorias: Criação de categorias (ex: Reunião, Auditório) para organizar o catálogo.

Relatório de Ocupação: Visão geral de quem reservou cada sala e em qual horário.

---

## 📸 Demonstração

---
## 🛠️ Tecnologias Utilizadas
Python 3.13.9

Django 6.0.1

Tailwind CSS (via django-tailwind)

SQLite (Banco de dados padrão)

---
## ⚙️ Como Rodar o Projeto
Siga os passos abaixo para configurar o ambiente em sua máquina (Windows 11 ou Linux):

1. Clonar o Repositório
   
git clone https://github.com/seu-usuario/reserva_salas.git
cd reserva_salas

2. Configurar o Ambiente Virtual

python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux:
source venv/bin/activate

---

3. Instalar Dependências

pip install -r requirements.txt

4. Configurar o Banco de Dados

python manage.py makemigrations
python manage.py migrate

5. Criar um Administrador

python manage.py createsuperuser

6. Iniciar o Servidor

python manage.py runserver

Acesse: http://127.0.0.1:8000/
