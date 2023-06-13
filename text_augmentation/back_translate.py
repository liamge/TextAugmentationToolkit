import tqdm
import numpy as np

from googletranslatepy import Translator

class BackTranslator(object):
	"""docstring for ClassName"""
	def __init__(self, orig_lang, method='nmt'):
		super(BackTranslator, self).__init__()
		self.trans_orig = orig_lang
		self.method = method
		assert self.method in ('nmt', 'google')

	def translate(self, docs, orig_lang, target_langs=["ja"]):
		"""
		Returns an array of tuples of format (lang, translated_sent)
		lang = string, target language translation
		translated_sent = string, translated input in target language

		Parameters
		----------

		docs : 
		orig_lang : 
		target_langs : 
		"""
		if self.method == "nmt":
			print("Loading in MarianMT Model...")
			if orig_lang == "en":
				# download model for English -> Romance
				en_tokenizer, en_model = download('Helsinki-NLP/opus-mt-en-ROMANCE')
				formatter_fn = lambda txt: f"{txt}" # empty function
			else: 
				# Naive assumption that if it's not english, it's a romance language
				rom_tokenizer, rom_model = download('Helsinki-NLP/opus-mt-ROMANCE-en')
				if isinstance(orig_lang, list):
					formatter_fn = lambda txt: f">>{orig_lang[0]}<< {txt}"
				else:
					formatter_fn = lambda txt: f">>{orig_lang}<< {txt}"
			print("Model loaded!")

			if isinstance(docs, list) or isinstance(docs, (np.ndarray, np.generic)):
				original_texts = [formatter_fn(txt) for txt in docs]
			elif isinstance(docs, str):
				original_texts = formatter_fn(docs)

			# Tokenize (text to tokens)
    		tokens = tokenizer.prepare_seq2seq_batch(original_texts, return_tensors='pt')

    		# Translate
    		translated = model.generate(**tokens)

    		# Decode (tokens to text)
    		translated_texts = tokenizer.batch_decode(translated, skip_special_tokens=True)

    		return translated_texts

		if self.method == "google":
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

		translated = self.translate(docs, self.orig_lang, target_langs)
		back_translated = self.translate([y for (x, y) in translated], target_langs, target_langs=[self.trans_orig])

		if return_lang_ind:
			return back_translated
		else:
			return [y for (x,y) in back_translated]

	def _download_model(self, model_name):
		from transformers import MarianMTModel, MarianTokenizer
		tokenizer = MarianTokenizer.from_pretrained(model_name)
	    model = MarianMTModel.from_pretrained(model_name)
	    return tokenizer, model