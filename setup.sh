mkdir -p ~/.streamlit/
echo "[general]
email = \"amaury.civrac@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
baseUrlPath = 'app-65'
" > ~/.streamlit/config.toml