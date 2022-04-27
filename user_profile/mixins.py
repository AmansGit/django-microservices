from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import request
import json
import datatime
from humanfriendly import format_timespan
from django.http import JsonResponse

def FormErrors(*args):
	'''
		Handle form error that are passed back to AJAX calls.
	'''
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message

def reCaptchaValidation(token):
	'''
		Validating reCaptcha
	'''
	result = requests.post(
			'https://www.google.com/recaptcha/api/siteverify',
			data={
				'secret': settings.RECAPTCHA_SECRET_KEY,
				'response': token
			}
		)
	return result.json()

def RedirectParams(**kwargs):
	'''
		Use to append url parameters when redirecting users
	'''
	url = kwargs.get('url')
	params = kwargs.get('params')
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += "?" + query_string

	return response

