mkdir -p ~/.streamlit/
echo "[general]
email = \"amaury.civrac@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
enabledTransports = ['ws', 'wss']
baseUrlPath = 'app-65'
" > ~/.streamlit/config.toml