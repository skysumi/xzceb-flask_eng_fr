import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    """
    This function translates English text to Frenc text
    """
    frenchtext = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    print(json.dumps(frenchtext, indent=2, ensure_ascii=False))
    return frenchtext.get("translations")[0]["translation"]

def french_to_english(frenchtext):
    """
    This function translates French text to English Text
    """
    englishtext = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    print(json.dumps(englishtext, indent=2, ensure_ascii=False))
    return englishtext.get("translations")[0]["translation"]
