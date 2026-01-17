# 🏢 Sistema de Reserva de Salas

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-blue)
![Python](https://img.shields.io/badge/Python-3.13-3776AB)
![Django](https://img.shields.io/badge/Django-6.0-092E20)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC)

Um sistema completo para gestão e reserva de espaços físicos, desenvolvido com **Django** e **Tailwind CSS**. O projeto conta com fluxos distintos para usuários comuns (reserva) e administradores (gestão completa via dashboard).

## 🚀 Funcionalidades

### 👤 Para Usuários
* **Autenticação Segura:** Cadastro e login utilizando e-mail como identificador principal.
* **Reserva de Salas:** Visualização de salas disponíveis e agendamento por data/horário.
* **Meus Agendamentos:** Painel para consultar, editar horários ou cancelar reservas.

### 🛡️ Para Administradores (Staff)
* **Dashboard de Gestão:** Sidebar exclusiva para navegação rápida.
* **Gerenciamento de Salas:** Cadastro de novas salas com capacidade e localização (interface personalizada fora do Django Admin).
* **Categorização:** Criação e gestão de categorias (ex: Auditório, Laboratório).
* **Controle de Ocupação:** Visualização global de todas as reservas ativas e usuários responsáveis.

---

## 📸 Demonstração do Projeto

| Página Inicial (Home) | Dashboard do Admin |
| :---: | :---: |
| ![Home](screenshots/home.png) | ![Dashboard](screenshots/dashboard.png) |
| *Visualização das salas disponíveis* | *Sidebar e controle de gestão* |

| Autenticação | Gestão de Reservas |
| :---: | :---: |
| ![Login](screenshots/login.png) | ![Reservas](screenshots/reservas.png) |
| *Login limpo com Tailwind* | *Edição e cancelamento de reservas* |

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.13.9, Django 6.0.1
* **Frontend:** HTML5, Django Templates, Tailwind CSS (via `django-tailwind`)
* **Banco de Dados:** SQLite (Padrão de desenvolvimento)
* **Autenticação:** Custom User Model (E-mail based)

---

## ⚙️ Como Rodar o Projeto Localmente

Siga os passos abaixo para executar o sistema em sua máquina:

### 1. Clone o repositório
```bash
git clone [https://github.com/SEU-USUARIO/reserva_salas.git](https://github.com/SEU-USUARIO/reserva_salas.git)
cd reserva_salas
