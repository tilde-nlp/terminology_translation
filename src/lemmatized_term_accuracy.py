#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Toms Bergmanis
# Created Date: July 2020
# =============================================================================
"""Script fof computting lemmatized term accuracy.
Positional parameters:
src - annotated source file such as in data/ats.tagged.lv.en
hyp - translation hypothesis
lang - target language """


import re
import stanza
import sys

src = sys.argv[1]
hyp = sys.argv[2]
lang = sys.argv[3]


stanza.download(lang=lang, processors='tokenize,pos,mwt,lemma')
nlp = stanza.Pipeline(lang=lang, processors='tokenize,pos,lemma', tokenize_pretokenized=True,  use_gpu=True, pos_batch_size=1, lemma_batch_size=1, tokenize_batch_size=1)

prog = r'<t> ([^<]+) <\\t>'

total = 0.0
correct = 0.0
with open(src, "r") as srcF, open(hyp, "r") as hypF:
    for src_line in srcF:
        terms = [term for term in re.findall(prog, src_line.replace("@@ ", ""))]
        hyp_line = hypF.readline().strip()
        if terms == []:
            continue

        lemmatized_terms = [" ".join([w.lemma for w in nlp(term).sentences[0].words]) for term in terms]

        hyp_lemmas = " ".join([w.lemma for w in nlp(hyp_line).sentences[0].words])
        for  term in lemmatized_terms:
            if term in hyp_lemmas:
                correct += 1.0
            total += 1.0

print(f'{correct / total:.3f} Lemmatized term accuracy')

