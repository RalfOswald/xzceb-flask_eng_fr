'''This is my translator'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-02-04',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def englishToFrench(englishText):
    '''Translate english to french'''
    try:
        translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
        frenchText = translation["translations"][0]["translation"]
        return frenchText
    except ValueError:
        return None

def frenchToEnglish(frenchText):
    '''Translate french to english'''
    try:
        translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
        englishText = translation["translations"][0]["translation"]
        return englishText
    except ValueError:
        return None
