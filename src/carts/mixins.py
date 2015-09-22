import ast
import base64


class TokenMixin(object):
	token = None
	def create_token(self, data_dict):
		if type(data_dict) == type(dict()):
			token = base64.b64encode(str(data_dict))
			self.token = token
			return token
		else:
			raise ValueError("Creating a token must be a Python dictionary.")


	def parse_token(self, token=None):
		if token is None:
			return {}
		try:
			token_decoded = base64.b64decode(token)
			token_dict = ast.literal_eval(token_decoded)
			return token_dict
		except:
			return {}