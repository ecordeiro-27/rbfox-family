# 📘 Como Usar este Projeto (Sem Saber Programar)

Este projeto ajuda a **filtrar e comparar listas de proteínas** de forma automática. Mesmo que você **não saiba programar**, você pode usar este script com facilidade seguindo os passos abaixo.

---

## 🧩 O que você precisa preparar

Antes de tudo, prepare estas **pastas e arquivos** dentro de uma pasta chamada `filtro`:

filtro/

├── arquivos_para_comparar/ → Coloque aqui os arquivos .txt com listas de referência

├── listas_proteinas/ → Coloque aqui os arquivos .txt com suas listas de proteínas

├── listas_proteinas_filtradas/ → Será preenchido automaticamente

├── resultado_comparacao/ → Será preenchido automaticamente

└── filtro.py → O código que faz tudo funcionar


---

## ✅ Passos para usar o projeto

### 👉 1. Abra com GitHub Codespaces (mais fácil)

1. Acesse o repositório no GitHub
2. Clique no botão verde **"Code"** → **"Open with Codespaces"** → **"New codespace"**
3. Após abrir o ambiente, clique no arquivo `filtro.py`
4. Clique com o botão direito no arquivo e escolha **"Abrir com o terminal integrado"** , vai aparecer uma tela preta embaixo e nela você vai digitar: **"python filtro.py"**

Pronto! Os arquivos filtrados e os resultados da comparação aparecerão automaticamente nas pastas:

- `listas_proteinas_filtradas/`
- `resultado_comparacao/`

---

### 🧑‍💻 2. Se quiser rodar no seu computador

Você precisa do **Python instalado**. Depois disso:

1. Abra o terminal ou prompt de comando
2. Vá até a pasta onde está o arquivo `filtro.py`
3. Rode o comando:

```bash
python filtro.py
```

O script vai fazer tudo sozinho.

ℹ️ O que o script faz?

- Lê arquivos .txt com proteínas

- Filtra apenas as linhas importantes

- Compara com arquivos de referência

- Mostra quais proteínas estão nas duas listas