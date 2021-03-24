# Facilitating Terminology Translation with Target Lemma Annotations
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
