
import streamlit as st
import requests

st.set_page_config(
    page_title="ChatIA",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 ChatIA")
st.caption("Seu assistente de inteligência artificial local")

# Histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de mensagem
prompt = st.chat_input("Digite sua mensagem...")

if prompt:
    # Guardar mensagem do usuário
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Pedir resposta ao modelo local
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                resposta_api = requests.post(
                    "http://localhost:11434/api/chat",
                    json={
                        "model": "qwen2.5:3b",
                        "messages": st.session_state.messages,
                        "stream": False
                    },
                    timeout=180
                )

                resposta_api.raise_for_status()

                resposta = resposta_api.json()["message"]["content"]
                st.markdown(resposta)

                # Guardar resposta no histórico
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": resposta
                })

            except requests.exceptions.ConnectionError:
                st.error(
                    "Não consegui conectar ao Ollama. "
                    "Verifique se ele está aberto no computador."
                )

            except requests.exceptions.RequestException as erro:
                st.error(f"Erro ao consultar a IA: {erro}")

            except (KeyError, ValueError):
                st.error("A IA retornou uma resposta inesperada.")
