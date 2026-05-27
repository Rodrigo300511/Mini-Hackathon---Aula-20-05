# 📊 ETL - Dados do IBGE para MongoDB Atlas

## 📌 Descrição do Projeto

Este projeto tem como objetivo implementar um pipeline simples de ETL (Extract, Transform, Load) utilizando dados públicos da API do IBGE.  

Os dados são extraídos via requisição HTTP, organizados por indicador e armazenados em um banco de dados MongoDB Atlas, separados em coleções específicas.

---

## 🚀 Objetivo

- Extrair dados da API do IBGE
- Realizar tratamento mínimo dos dados
- Armazenar no MongoDB Atlas
- Organizar os dados em coleções separadas por indicador
- Aplicar boas práticas de organização de código

---

## 📊 Indicadores Utilizados

Os seguintes indicadores foram utilizados no projeto:

| Código | Descrição |
|--------|----------|
| 4099 | Taxa de desocupação |
| 4096 | Taxa de participação na força de trabalho |
| 12466 | Taxa de informalidade |

---

## 🌐 Fonte de Dados

API oficial do IBGE:

```
https://servicodados.ibge.gov.br/api/v3/
```

Endpoint utilizado:

```
https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/-50/variaveis/4096%7C4099%7C12466?localidades=N1[all]|N3[all]&classificacao=2[all]
```

---

## 🏗️ Estrutura do Projeto

```
ETL_UNI/
│
├── src/
│   ├── extract.py
│   ├── load.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── .env
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3
- Requests
- PyMongo
- MongoDB Atlas
- Python-dotenv

---

## 🔄 Pipeline ETL

### 1. Extract (Extração)

Responsável por consumir a API do IBGE e retornar os dados em formato JSON.

### 2. Transform (Tratamento)

Os dados são organizados por código de variável e preparados para separação em coleções.

### 3. Load (Carregamento)

Os dados são armazenados no MongoDB Atlas, separados por coleção:

- taxa_desocupacao
- taxa_participacao
- taxa_informalidade

---

## ☁️ Banco de Dados

**Banco utilizado:**

```
ibge_database
```

**Collections:**

- taxa_desocupacao  
- taxa_participacao  
- taxa_informalidade  

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Rodrigo300511/Mini-Hackathon---Aula-20-05.git
```

### 2. Acessar a pasta

```bash
cd Mini-Hackathon---Aula-20-05
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

```bash
venv\Scripts\activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o projeto

```bash
python main.py
```

---

## 📌 Exemplo de Execução

```
STATUS CODE: 200

Processando variável 4099 → taxa_desocupacao
Sucesso! Dados inseridos no MongoDB

Processando variável 4096 → taxa_participacao
Sucesso! Dados inseridos no MongoDB

Processando variável 12466 → taxa_informalidade
Sucesso! Dados inseridos no MongoDB
```

---

## ✅ Boas Práticas Aplicadas

- Separação em módulos (extract / load)
- Uso de MongoDB Atlas (cloud)
- Uso de variáveis de ambiente
- Estruturação por collections
- Tratamento básico de erros
- Código organizado e reutilizável

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos na disciplina de Engenharia de Dados.
