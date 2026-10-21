#!/bin/bash
echo "Instalando dependências..."
pip3 install -r requirements.txt

echo "Configurando o comando 'btc'..."
chmod +x btc.py
sudo cp btc.py /usr/local/bin/btc

echo "✅ Instalação concluída! Digite 'btc' no seu terminal."