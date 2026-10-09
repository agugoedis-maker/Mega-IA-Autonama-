
import json
import random
from pathlib import Path

ARQUIVO = Path("historico.json")


def carregar_historico():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text(encoding="utf-8"))
    return {"concursos": [], "previsoes": []}


def salvar_historico(dados):
    ARQUIVO.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def gerar_jogos(quantidade=5):
    jogos = set()
    while len(jogos) < quantidade:
        jogo = tuple(sorted(random.sample(range(1, 61), 6)))
        jogos.add(jogo)
    return [list(jogo) for jogo in sorted(jogos)]


def avaliar_jogo(jogo, resultado):
    return len(set(jogo) & set(resultado))


def main():
    dados = carregar_historico()
    jogos = gerar_jogos(5)

    concurso = {
        "tipo": "sugestao",
        "jogos": jogos
    }
    dados["previsoes"].append(concurso)
    salvar_historico(dados)

    print("MEGA IA - SUGESTOES PARA O PROXIMO CONCURSO")
    for i, jogo in enumerate(jogos, 1):
        print(f"Jogo {i}: " + " - ".join(f"{n:02}" for n in jogo))

    print("\nSugestoes registradas no historico.")
    print("As combinacoes nao garantem premio.")


if __name__ == "__main__":
    main()
