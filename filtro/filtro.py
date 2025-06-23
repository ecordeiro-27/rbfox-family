from pathlib import Path

# Palavras-chave que queremos preservar nas linhas
PALAVRAS_CHAVE = [
    "(RBFOX 1 )", "(RBFOX1)", "(FX 1 )", "(1)",
    " - 1", "-1", " - RBFOX1DANRE", "- RBFOX1DANRE",
    " -RBFOX1 HUMANA", "-RBFOX1 HUMANA", "-rfox1 human", " -rfox1 human",
    "-RBFOX 1MOUSE", " -RBFOX 1MOUSE", " -rbfox 1 mouse", "-rbfox 1 mouse",
    "- LOC", " - LOC", "--1", " --1", "-homologo", " -homologo"
]

def filtro(caminho_listas: Path, caminho_filtradas: Path):
    caminho_filtradas.mkdir(exist_ok=True)
    for arquivo in caminho_listas.glob("*.txt"):
        linhas_filtradas = []
        with arquivo.open("r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha.startswith(">") or any(chave in linha for chave in PALAVRAS_CHAVE):
                    linhas_filtradas.append(linha)
        caminho_saida = caminho_filtradas / f"FILTRADO-{arquivo.name}"
        with caminho_saida.open("w", encoding="utf-8") as f_out:
            f_out.write("\n".join(linhas_filtradas))


def extrair_ids(arquivo: Path) -> set:
    with arquivo.open("r", encoding="utf-8") as f:
        return {linha.strip().split()[0].strip(",") for linha in f if linha.strip().startswith(">")}


def comparacao(caminho_comparar: Path, caminho_filtradas: Path, caminho_resultado: Path):
    caminho_resultado.mkdir(exist_ok=True)

    # Juntar todos os IDs dos arquivos filtrados
    ids_filtrados = set()
    for arquivo in caminho_filtradas.glob("FILTRADO-*.txt"):
        ids_filtrados.update(extrair_ids(arquivo))

    # Comparar com arquivos de comparação
    for arquivo in caminho_comparar.glob("*.txt"):
        ids_para_comparar = extrair_ids(arquivo)
        ids_comuns = sorted(ids_filtrados & ids_para_comparar)

        if ids_comuns:
            caminho_saida = caminho_resultado / f"COMPARACAO-{arquivo.name}"
            with caminho_saida.open("w", encoding="utf-8") as f_out:
                f_out.write("\n".join(ids_comuns))


def main(quero_fazer_comparacao=True, quero_filtrar=True):
    base = Path(__file__).parent
    listas = base / "listas_proteinas"
    filtradas = base / "listas_proteinas_filtradas"
    comparar = base / "arquivos_para_comparar"
    resultado = base / "resultado_comparacao"

    if quero_filtrar:
        filtro(listas, filtradas)
    if quero_fazer_comparacao:
        comparacao(comparar, filtradas, resultado)


if __name__ == "__main__":
    main()
