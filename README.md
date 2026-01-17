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
| ![Home](<img width="1912" height="926" alt="Captura de tela 2026-01-16 222413" src="https://github.com/user-attachments/assets/d54086dd-c763-4a37-bb9b-cb51782825e6" />
) | ![Dashboard](<img width="1919" height="962" alt="Captura de tela 2026-01-16 222633" src="https://github.com/user-attachments/assets/854a2e43-981a-4194-bf67-7b1eda621acb" />
) |
| *Visualização das salas disponíveis* | *Sidebar e controle de gestão* |

| Autenticação | Gestão de Reservas |
| :---: | :---: |
| ![Login](<img width="1403" height="854" alt="Captura de tela 2026-01-16 222713" src="https://github.com/user-attachments/assets/d31dc476-a43e-4c6b-bdd5-5288973858b8" />
) | ![Reservas](<img width="1919" height="950" alt="Captura de tela 2026-01-16 222810" src="https://github.com/user-attachments/assets/35144d7e-38b2-4678-8aae-723ffb145049" />
) |
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
git clone https://github.com/FabricyoSilva/reserva_salas.git
cd reserva_salas
```

### 2. Crie e ative o ambiente virtual
````bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
`````


### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados

```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Compile o CSS (Tailwind)
Para garantir que o estilo visual carregue corretamente:
```bash
python manage.py tailwind build
````
### 7. Execute o Servidor
```bash
python manage.py runserver
```

Acesse no seu navegador: http://127.0.0.1:8000/

---

## 📂 Estrutura Principal

* `reservas/`: App principal contendo Models, Views, Forms e Templates.

* `theme/`: Configuração do Tailwind CSS.

* `core/`: Configurações globais do projeto Django.
