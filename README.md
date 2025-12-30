# Ultimate Team FIFA CLI

Uma aplicação de Linha de Comando (CLI) em Python para gerenciar um banco de dados estilo FIFA Ultimate Team. Este projeto permite aos usuários gerenciar jogadores, times, ligas, países e criar táticas personalizadas com cálculos de química.

## Funcionalidades

- **Gestão de Entidades (CRUD):**
  - **Países:** Criar, ler, atualizar e deletar países.
  - **Ligas:** Gerenciar ligas vinculadas a países específicos.
  - **Times:** Gerenciar times dentro de ligas.
  - **Jogadores:** Criar jogadores com associações a times e países.
  - **Usuários:** Gerenciar usuários, incluindo sua coleção de cartas de jogadores e táticas personalizadas.

- **Gestão Tática:**
  - Criar e gerenciar táticas personalizadas (elencos) para usuários.
  - Adicionar/Remover cartas de jogadores da coleção de um usuário.
  - Calcular química do elenco com base nas conexões dos jogadores.

## Tecnologias

- **Python 3.x**
- **MongoDB** (Banco de Dados)
- **PyMongo** (Driver Python para MongoDB)

## Estrutura do Projeto

- `main.py`: O ponto de entrada da aplicação. Inicializa a conexão com o banco de dados e inicia a CLI.
- `database/`: Contém a lógica de conexão com o banco de dados (`database.py`) e a interface do menu CLI (`menuCLI.py`).
- `DAO/`: Objetos de Acesso a Dados (DAOs) que lidam com as interações do banco de dados para cada entidade.
- `entity/`: Classes Python representando os modelos de dados (Player, Team, User, etc.).
- `data/`: Arquivos JSON contendo dados iniciais (seed) para o banco de dados.

## Pré-requisitos

- Python 3.x instalado.
- Instância do MongoDB rodando localmente em `mongodb://localhost:27017/`.
- Pacotes Python necessários:
  ```bash
  pip install pymongo
  ```

## Como Executar

1. Certifique-se de que o MongoDB está rodando localmente.
2. Instale as dependências necessárias (se ainda não estiverem instaladas).
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Siga o menu na tela para interagir com o sistema.

## Modelos de Dados

- **Country (País):** Nome.
- **League (Liga):** Nome, País.
- **Team (Time):** Nome, Liga.
- **Player (Jogador):** Nome, Posição, Time, País.
- **User (Usuário):** Nome de usuário, Nome do time, Coleção de Cartas, Táticas.
- **Tactic (Tática):** Nome, Lista de Jogadores, Pontuação de Química.