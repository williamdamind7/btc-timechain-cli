# ⚡ BTC Timechain CLI

![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)
![Platform: Linux](https://img.shields.io/badge/Platform-Linux-blue.svg)
![Python: 3.x](https://img.shields.io/badge/Python-3.x-green.svg)

Uma ferramenta minimalista, rápida e direta de linha de comando (CLI) para Linux que consulta dados em tempo real da **Timechain do Bitcoin** diretamente do seu terminal, sem necessidade de chaves de API (API Keys) ou autenticação.

---

## 🖥️ Demonstração no Terminal

Ao executar o comando `btc`, você terá a seguinte saída instantânea:

```text
⚡ BITCOIN TIMECHAIN STATUS ⚡
-----------------------------------
🧱 Bloco Atual:  885420
-----------------------------------
💵 USD / BTC:    $95,430.00
🇧🇷 BRL / BTC:    R$ 548.722,50
-----------------------------------
⛽ Taxas (sat/vByte):
   🚀 Alta Prioridade:  12 sat/vB
   🚶 Média Prioridade: 8 sat/vB
   🐢 Baixa Prioridade: 4 sat/vB
-----------------------------------
```

---

## ✨ Funcionalidades

* **Altura do Bloco (Block Height):** Consulta o último bloco minerado na Timechain em tempo real.
* **Cotação Dual:** Exibe o preço atual do Bitcoin em Dólar Americano (`USD`) e Real Brasileiro (`BRL`).
* **Estimativa de Taxas (Mempool):** Mostra o custo atual da rede em `sat/vByte` para prioridades alta (próximo bloco), média (~30 min) e baixa (~1 hora).
* **Zero Configuração:** Não exige cadastro, conta ou configuração de tokens de API.

---

## 🛠️ Pré-requisitos

* **Sistema Operacional:** Linux (qualquer distribuição)
* **Python:** Versão 3.6 ou superior
* **Gerenciador de pacotes:** `pip`

---

## 🚀 Instalação

### Método 1: Instalação Automática (Recomendado)

Clone o repositório e execute o script de instalação:

```bash
git clone [https://github.com/WilliamdeSouzaM7/btc-timechain-cli.git](https://github.com/WilliamdeSouzaM7/btc-timechain-cli.git)
cd btc-timechain-cli
chmod +x install.sh
./install.sh
```

### Método 2: Instalação Manual

Caso prefira executar passo a passo:

```bash
# 1. Clone o repositório
git clone [https://github.com/WilliamdeSouzaM7/btc-timechain-cli.git](https://github.com/WilliamdeSouzaM7/btc-timechain-cli.git)
cd btc-timechain-cli

# 2. Instale a biblioteca necessária
pip3 install -r requirements.txt

# 3. Torne o script executável e mova para o seu PATH global
chmod +x btc.py
sudo cp btc.py /usr/local/bin/btc
```

---

## 💻 Como Usar

Após a instalação, abra qualquer janela do terminal e digite apenas:

```bash
btc
```

> **Dica Linux:** Para monitorar a Timechain continuamente no terminal (atualizando a cada 30 segundos), você pode combiná-lo com o comando nativo `watch`:
> ```bash
> watch -n 30 -c btc
> ```

---

## 🗑️ Desinstalação

Para remover o comando global do seu sistema Linux, basta deletar o binário:

```bash
sudo rm /usr/local/bin/btc
```

---

## 📡 Fontes de Dados (APIs Públicas)

Esta ferramenta consome dados públicos e abertos fornecidos por:
* **[Mempool.space API](https://mempool.space/docs/api/rest):** Para dados da Timechain (altura do bloco e taxas de sat/vByte).
* **[CoinGecko API](https://www.coingecko.com/en/api):** Para conversão fiduciária em tempo real (USD e BRL).

---

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Se você quiser adicionar novas métricas (como Hashrate, Dificuldade da rede, Halving Countdown ou suporte ao próprio nó local):

1. Faça um **Fork** do projeto.
2. Crie uma Branch para sua modificação (`git checkout -b feature/nova-metrica`).
3. Faça o Commit das suas alterações (`git commit -m 'feat: adiciona contagem regressiva do halving'`).
4. Faça o Push para a Branch (`git push origin feature/nova-metrica`).
5. Abra um **Pull Request**.

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais informações.

---
*Don't Trust, Verify.* ₿
