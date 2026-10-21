#!/usr/bin/env python3
import sys
import requests

# Cores ANSI para o terminal Linux
LARANJA = "\033[38;5;214m"
VERDE = "\033[92m"
CIANO = "\033[96m"
NEGRITO = "\033[1m"
RESET = "\033[0m"


def obter_dados_bitcoin():
    try:
        # 1. Preço em USD e BRL (via CoinGecko API Pública)
        url_preco = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,brl"
        res_preco = requests.get(url_preco, timeout=5).json()
        btc_usd = res_preco["bitcoin"]["usd"]
        btc_brl = res_preco["bitcoin"]["brl"]

        # 2. Altura do Bloco Atual (Timechain Tip via Mempool.space)
        url_bloco = "https://mempool.space/api/blocks/tip/height"
        bloco_atual = requests.get(url_bloco, timeout=5).text

        # 3. Taxas da Rede em sat/vB (via Mempool.space)
        url_taxas = "https://mempool.space/api/v1/fees/recommended"
        res_taxas = requests.get(url_taxas, timeout=5).json()
        taxa_alta = res_taxas["fastestFee"]
        taxa_media = res_taxas["halfHourFee"]
        taxa_baixa = res_taxas["hourFee"]

        # Exibição no Terminal
        print(f"\n{LARANJA}{NEGRITO}⚡ BITCOIN TIMECHAIN STATUS ⚡{RESET}")
        print("-" * 35)
        print(f"🧱 {NEGRITO}Bloco Atual:{RESET}  {CIANO}{bloco_atual}{RESET}")
        print("-" * 35)
        print(
            f"💵 {NEGRITO}USD / BTC:{RESET}    {VERDE}${btc_usd:,.2f}{RESET}"
        )
        print(
            f"🇧🇷 {NEGRITO}BRL / BTC:{RESET}    {VERDE}R$ {btc_brl:,.2f}{RESET}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
        print("-" * 35)
        print(f"⛽ {NEGRITO}Taxas (sat/vByte):{RESET}")
        print(f"   🚀 Alta Prioridade:  {LARANJA}{taxa_alta} sat/vB{RESET}")
        print(f"   🚶 Média Prioridade: {taxa_media} sat/vB")
        print(f"   🐢 Baixa Prioridade: {taxa_baixa} sat/vB")
        print("-" * 35 + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a Timechain: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    obter_dados_bitcoin()