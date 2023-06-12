import faiss
import pandas as pd

from googletranslatepy import Translator
from sentence_transformers import SentenceTransformer

__version__ = "0.0.1"

class BackTranslator(object):
	"""docstring for ClassName"""
	def __init__(self, orig_lang):
		super(BackTranslator, self).__init__()
		self.trans_orig = orig_lang

	def test(self):
		print("Test successful!")

	def translate(self, docs, target_langs=["ja"]):
		"""
		Returns an array of tuples of format (lang, translated_sent)
		lang = string, target language translation
		translated_sent = string, translated input in target language
		"""
		translated = []

		translators = []
		for lang in target_langs:
			translators.append((lang, Translator(target=lang)))
            
		if type(docs) == list:
			for sent in docs:
				for (lang, translator) in translators:
					translated.append((lang, translator.translate(sent)))
		elif type(docs) == str:
			for (lang, translator) in translators:
				translated.append((lang, translator.translate(docs)))
		else:
			raise TypeError("Input of type {} not supported, \
							 please input either an array of strings or\
							 a string")

		return translated

	def back_translate(self, docs, target_langs=["ja"], return_lang_ind=False):

		translated = self.translate(docs, target_langs)
		back_translated = self.translate([y for (x, y) in translated], target_langs=[self.trans_orig])

		if return_lang_ind:
			return back_translated
		else:
			return [y for (x,y) in back_translated]

class EDATransformer(object):
	"""docstring for ClassName"""
	def __init__(self, spacy_nlp):
		"""
		Parameters
		----------
		spacy_nlp : spacy Language object for performing POS tagging/vectorization
		"""
		super(EDATransformer, self).__init__()

	def build_dataset(self, docs):
		"""
		Stores the documents as a pandas dataframe containing 
		the processed documents using spacy.

		Builds a vocabulary DataFrame that allows for
		fast querying of word synonyms using FAISS.

		Parameters
		----------
		docs : iterable of documents to process
		"""

		return

	def synonym_replacement(self):
		return

	def random_insertion(self):
		return

	def random_swap(self):
		return

	def random_deletion(self):
		return