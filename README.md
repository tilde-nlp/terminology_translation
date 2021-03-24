# Facilitating Terminology Translation with Target Lemma Annotations
## Abstract 
Most of the recent work on terminology integration in machine translation has assumed that terminology translations are given already inflected in forms that are suitable for the target language sentence. In day-to-day work of professional translators, however, it is seldom the case as translators work with bilingual glossaries where terms are given in their dictionary forms; finding the right target language form is part of the translation process. We argue that the requirement for apriori specified target language forms is unrealistic and impedes the practical applicability of previous work. In this work, we propose to train machine translation systems using a source-side data augmentation method\footnote{Relevant materials and code:  that annotates randomly selected source language words with their target language lemmas. We show that systems trained on such augmented data are readily usable for terminology integration in real-life translation scenarios. 
Our experiments on terminology translation into the morphologically complex Baltic and Uralic languages show an improvement of up to 7 BLEU points over baseline systems with no means for terminology integration and an average improvement of 4 BLEU points over the previous work.
Results of the human evaluation indicate a 47.7 absolute improvement over the previous work in term translation accuracy when translating into Latvian.

Cite:
```
@article{bergmanis2021facilitating,
  title={Facilitating Terminology Translation with Target Lemma Annotations},
  author={Bergmanis, Toms and Pinnis, M{\=a}rcis},
  booktitle={Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers},
  year={2021}
}
```


## Corrections

In Section 3 **Experimental Setup**, we say that *“For lemmatization and POS tagging, we use pre-trained Stanza (Qi et al., 2020) models.”* This is true for all languages except Latvian, for which Stanza is inaccurate. Thus for Latvian, we used our in-house rule bassed lemmatizer, which is not publically available. This means that **Table 3: Results of automatic evaluation metrics EN-LV Acc.** collum can not be replicated with Stanza. Recalculating lemmatized exact match accuracy with Stanza yields lower results: **0.547** and **0.849** for the baseline and the system using TLA respectively.
