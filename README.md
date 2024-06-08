# ProLife Manager

## Descrição

O **ProLife Manager** é uma aplicação web desenvolvida com Django, projetada para ajudar usuários a aumentarem sua produtividade e organização em diversas áreas da vida. A plataforma oferece uma interface intuitiva e funcionalidades abrangentes para facilitar o gerenciamento de tarefas diárias, agendas, listas de compras, rotinas de academia e planos de dieta. 

## Funcionalidades

- **Aumento de Produtividade no Trabalho**: Ferramentas para gerenciar e priorizar tarefas profissionais, mantendo o foco e a eficiência.
- **Organização de Tarefas**: Criação e monitoramento de listas de tarefas personalizadas, com opções de categorização e prazos.
- **Agenda de Tarefas**: Integração com um calendário para agendar e acompanhar compromissos e eventos importantes.
- **Lista de Compras**: Funcionalidade para criar e compartilhar listas de compras, facilitando a organização das necessidades diárias.
- **Dia a Dia na Academia**: Registro e acompanhamento de treinos, metas e progressos físicos.
- **Dieta**: Planejamento e monitoramento de dietas, com sugestões de refeições e controle de ingestão nutricional.

## Tecnologias Utilizadas

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Banco de Dados**: Mysql
- **Outras Ferramentas**: Coolors para paleta de cores

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/prolife-manager.git
cd prolife-manager
```

2. Crie um dataframe vazio no Mysql Workbenck com nome "prolifemanager"

3. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute as migrações do banco de dados:
```bash
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.