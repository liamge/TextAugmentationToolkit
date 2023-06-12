import faiss
import pandas as pd

from sentence_transformers import SentenceTransformer

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