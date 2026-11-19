> **⚠️ Aviso Ético (*Disclaimer*):** Este repositório tem fins **estritamente educacionais e defensivos**, desenvolvido como parte de um desafio prático de Cibersegurança em ambiente local isolado e controlado. Não utilize estes estudos ou conceitos fora de ambientes autorizados e controlados.

---

## 📌 Sobre o Projeto

Este projeto documenta o estudo técnico e comportamental de **keyloggers** em Python dentro de um ambiente de laboratório isolado, abordando como mecanismos de captura de eventos de teclado funcionam, quais sinais ou indicadores podem ser observados e quais medidas de defesa (*Blue Team*) ajudam a prevenir, detectar e mitigar esse tipo de ameaça.

> **Nota sobre a estrutura atual:** A pasta local encontra-se nomeada como `ransomware` e contém o ficheiro `keylogger.pyw` e o ambiente virtual `.venv/`. Caso pretenda cobrir também a simulação controlada de *ransomware* prevista no enunciado do desafio ou alinhar o nome do diretório ao tema, basta adicionar os respetivos módulos/documentação ou renomear o diretório antes da entrega final.

---

## 📂 Estrutura Atual do Projeto

```text
ransomware/
├── .venv/               # Ambiente virtual Python local (ignorado via .gitignore)
├── keylogger.pyw        # Script Python do laboratório em ambiente isolado
├── .gitattributes       # Configurações de atributos do Git
├── .gitignore           # Ficheiros e pastas ignorados pelo controlo de versões
├── LICENSE              # Licença MIT
└── README.md            # Documentação principal do projeto