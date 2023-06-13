import tqdm
import numpy as np

from googletranslatepy import Translator

class BackTranslator(object):
	"""docstring for ClassName"""
	def __init__(self, orig_lang):
		super(BackTranslator, self).__init__()
		self.trans_orig = orig_lang

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
            
		if isinstance(docs, list) or isinstance(docs, (np.ndarray, np.generic)):
			for i in tqdm.tqdm(range(len(docs))):
				for (lang, translator) in translators:
					translated.append((lang, translator.translate(docs[i])))
		elif isinstance(docs, str):
			for (lang, translator) in translators:
				translated.append((lang, translator.translate(docs)))
		else:
			raise TypeError("Input type not supported, \
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