# ChatIA - Assistente de Inteligência Artificial

O ChatIA é um chatbot desenvolvido em Python que utiliza um modelo de inteligência artificial local para responder perguntas e manter o contexto da conversa.

## Tecnologias utilizadas

- Python
- Streamlit
- Ollama
- Qwen 2.5 3B
- Requests

## Funcionalidades

- Interface de chat interativa.
- Respostas geradas por inteligência artificial.
- Histórico de mensagens durante a sessão.
- Uso de um modelo local, sem depender de uma API paga.

## Requisitos

- Python instalado.
- Ollama instalado.
- Modelo Qwen 2.5 3B baixado pelo Ollama.

## Como executar

1. Clone o repositório.
2. Entre na pasta do projeto.
3. Crie e ative um ambiente virtual.
4. Instale as dependências:

   `ash
   pip install -r requirements.txt
   `

5. Baixe o modelo:

   `ash
   ollama pull qwen2.5:3b
   `

6. Inicie o Ollama.
7. Execute a aplicação:

   `ash
   python -m streamlit run app.py
   `

8. Abra o endereço local exibido no terminal.

## Observação

O histórico é mantido na sessão atual do aplicativo. Ele não é salvo permanentemente após o encerramento da sessão.

