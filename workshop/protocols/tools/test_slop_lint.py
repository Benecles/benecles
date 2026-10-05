"""Table-driven behavioral coverage for the Portuguese slop linter."""
import os
import json
import subprocess
import tempfile
import unittest
import sys

sys.path.insert(0, os.path.dirname(__file__))
from slop_lint import HARD, RATE, lint

# Varied, deliberately neutral filler makes every RATE fixture eligible without
# accidentally repeating a rule trigger. 56 short sentences exceed all gates.
FILLER = " ".join(
    f"{start} consta no processo e orienta a leitura dos autos."
    for start in ["A norma", "O juízo", "A parte", "O pedido", "A prova", "O prazo", "A decisão"] * 8
)

RATE_CASES = {
    "colon-reveal": (
        "A regra define o alcance. O ponto central é este: a decisão limita o pedido. "
        "A norma organiza o exame. A consequência é esta: o juiz verifica o prazo. " + FILLER,
        "A lei fixa o prazo aplicável ao pedido. O juiz examina os documentos juntados. " + FILLER,
    ),
    "denial-restatement": (
        "A medida não elimina o dever, mas desloca o momento do cumprimento. "
        "O ato não extingue o direito, mas altera o modo de exercício. " + FILLER,
        "A medida preserva o dever e define outro momento para o cumprimento. "
        "O ato mantém o direito e disciplina seu exercício. " + FILLER,
    ),
    "rather-than": (
        "A parte age em vez de aguardar. O juízo decide ao invés de suspender. " + FILLER,
        "A parte aguarda a intimação. O juízo suspende o feito. " + FILLER,
    ),
    "triad-density": (
        "A lei exige registro, publicação e comunicação. A norma prevê prazo, forma e recurso. "
        "O pedido exige identificação, assinatura e protocolo. " + FILLER,
        "A lei exige registro e publicação. A norma prevê prazo e recurso. " + FILLER,
    ),
    "stance-adverb": (
        "A medida é meramente formal. O ato foi simplesmente comunicado. " + FILLER,
        "A medida tem forma definida. O ato foi comunicado às partes. " + FILLER,
    ),
    "negation-chain": (
        "O pedido foi feito sem prazo, sem assinatura, sem comprovante. "
        "O ato ocorreu sem aviso, sem registro, sem justificativa. " + FILLER,
        "O pedido foi feito com prazo, assinatura e comprovante. "
        "O ato ocorreu após aviso e registro. " + FILLER,
    ),
    "same-opener-run": (
        "Norma define o prazo. Norma indica a forma. Norma delimita o efeito. "
        "A sentença foi juntada aos autos. "
        "Norma define outro prazo. Norma indica outra forma. Norma delimita outro efeito. " + FILLER,
        "A lei define o prazo. O juízo indica a forma. A parte delimita o pedido. " + FILLER,
    ),
    "semicolon-correction": (
        "A norma fixa o prazo; mas a decisão altera a contagem. "
        "O ato reconhece o pedido; na verdade, limita seu alcance. " + FILLER,
        "A norma fixa o prazo e o juízo conta os dias úteis. "
        "O ato reconhece o pedido e a decisão delimita seu alcance. " + FILLER,
    ),
    "colon-appositive": (
        "O requisito é: prova documental suficiente. A competência consiste em: julgamento do recurso. " + FILLER,
        "O requisito exige prova documental suficiente. A competência permite julgar o recurso. " + FILLER,
    ),
    "load-bearing-adverb": (
        "A prova demonstra claramente o fato. O prazo é obviamente aplicável. " + FILLER,
        "A prova demonstra o fato. O prazo está previsto no artigo. " + FILLER,
    ),
    "nominalisation-pileup": (
        "A implementação da verificação da execução cabe ao órgão. "
        "A realização da análise da aplicação depende do relator. " + FILLER,
        "O órgão implementa a verificação da execução. O relator analisa a aplicação. " + FILLER,
    ),
}

HARD_CASES = {
    "negative-parallelism": ("A decisão não é definitiva neste ponto.", "A decisão permanece provisória neste ponto."),
    "puffery": ("A regra desempenha papel fundamental no sistema.", "A regra define o prazo do recurso."),
    "significance-gerund": ("A regra foi aplicada, evidenciando a importância do tema.", "A regra foi aplicada ao caso concreto."),
    "formulaic-metatext": ("Vale destacar que o prazo começou ontem.", "O prazo começou ontem."),
    "vague-attribution": ("Muitos autores afirmam que o prazo é curto.", "O prazo é de quinze dias."),
    "reader-address": ("Perceba que o prazo termina hoje.", "O prazo termina hoje."),
    "AI-calque": ("A decisão oferece abordagem robusta para navegar pelo cenário atual.", "A decisão organiza o exame dos fatos."),
    "backstage": ("Os slides apresentam o tema nesta leitura.", "O tema aparece no primeiro capítulo."),
    "rhetorical-triad": ("A regra protege forma, prazo e, sobretudo, segurança.", "A regra protege forma, prazo e segurança."),
}


def run_text(text, budget=None):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", encoding="utf-8", delete=False) as f:
        f.write(text)
        path = f.name
    try:
        return lint(path, budget)
    finally:
        os.unlink(path)


class LinterRulesTest(unittest.TestCase):
    def test_rule_inventory_has_examples(self):
        self.assertEqual(set(HARD), set(HARD_CASES))
        self.assertEqual(set(RATE) - {"paren-scarcity"}, set(RATE_CASES))

    def test_hard_rules_positive_and_negative(self):
        for rule, (positive, negative) in HARD_CASES.items():
            with self.subTest(rule=rule):
                self.assertIn(rule, {f["rule"] for f in run_text(positive)["findings"]})
                self.assertNotIn(rule, {f["rule"] for f in run_text(negative)["findings"]})

    def test_rate_rules_positive_and_negative(self):
        for rule, (positive, negative) in RATE_CASES.items():
            with self.subTest(rule=rule):
                result = run_text(positive)
                self.assertGreaterEqual(result["words"], 250)
                self.assertGreaterEqual(result["sentences"], 5)
                self.assertGreaterEqual(sum(f["rule"] == rule for f in result["findings"]), 2)
                self.assertNotIn(rule, {f["rule"] for f in run_text(negative)["findings"]})

    def test_paren_scarcity_absence_signal(self):
        no_parens = run_text(FILLER)
        with_parens = run_text("Esta regra (com explicação útil) orienta a leitura. " + FILLER)
        self.assertGreaterEqual(no_parens["words"], 250)
        self.assertGreaterEqual(no_parens["sentences"], 5)
        self.assertIn("paren-scarcity", {f["rule"] for f in no_parens["findings"]})
        self.assertNotIn("paren-scarcity", {f["rule"] for f in with_parens["findings"]})

    def test_d9_hard_and_rate_patterns_match_natural_examples(self):
        rhetorical = run_text("A lei prevê três requisitos e, sobretudo, organiza seu exame.")["findings"]
        self.assertIn("rhetorical-triad", {f["rule"] for f in rhetorical})


    def test_minimum_gates_and_explicit_failure_budget(self):
        one_hit = "A medida não elimina o dever, mas desloca o cumprimento. " + FILLER
        two_short = "A medida não elimina o dever, mas desloca o cumprimento. " * 2
        two_few_sentences = ("A medida não elimina o dever, mas desloca o cumprimento, "
                             "e a norma define o prazo. " * 2)
        self.assertNotIn("denial-restatement", {f["rule"] for f in run_text(one_hit)["findings"]})
        self.assertNotIn("denial-restatement", {f["rule"] for f in run_text(two_short)["findings"]})
        self.assertNotIn("denial-restatement", {f["rule"] for f in run_text(two_few_sentences)["findings"]})
        review = run_text(FILLER, budget=0)
        self.assertGreater(review["finding_count"], 0)
        self.assertEqual(review["status"], "FAIL")

    def test_json_cli_includes_density_summary(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", encoding="utf-8", delete=False) as f:
            f.write("A medida não elimina o dever, mas desloca o cumprimento. "
                    "O ato não extingue o direito, mas altera o modo de exercício. " + FILLER)
            path=f.name
        try:
            result=subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "slop_lint.py"), path, "--json"],
                                  check=True, capture_output=True, text=True)
            data=json.loads(result.stdout)["files"][0]
            self.assertIn("denial-restatement", data["density"])
            self.assertIn("per_1000", data["density"]["denial-restatement"])
            self.assertEqual(data["status"], "PASS")
        finally:
            os.unlink(path)

    def test_false_positive_contexts_remain_flagged_for_review(self):
        # These are intentional legal constructions; lint findings are prompts.
        legal = run_text("A regra não reduz o dano, mas desloca o ônus. O ato não extingue o direito, mas muda seu exercício. " + FILLER)
        statutory = run_text("A lei exige registro, publicação e comunicação. "
                             "A norma exige prazo, forma e recurso. " + FILLER)
        enumerated = run_text("O pedido requer identificação, assinatura e protocolo. "
                              "O procedimento exige presença, declaração e assinatura. " + FILLER)
        self.assertIn("denial-restatement", {f["rule"] for f in legal["findings"]})
        self.assertIn("triad-density", {f["rule"] for f in statutory["findings"]})
        self.assertIn("triad-density", {f["rule"] for f in enumerated["findings"]})


if __name__ == "__main__":
    unittest.main()
