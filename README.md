# TextAugmentationToolkit
A small toolkit for augmenting text data for downstream NLP tasks

Supported text augmentation techniques:
- Backtranslation
- [EDA](https://arxiv.org/abs/1901.11196) - Easy Data Augmentation 
  - Synonym replacement
  - Random insertion
  - Random swap
  - Random deletion

Usage:

```
from text_augmentation.back_translate import BackTranslator

translator = BackTranslator(orig_lang='en')

translator.back_translate("This is a test of the translation system", target_langs=["ja", "ar", "zh-CN"])
```
