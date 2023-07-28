import os
from typing import Optional, Tuple

import gradio as gr
import pickle
from query_data import get_chain
from threading import Lock

with open("vectorstore.pkl", "rb") as f:
    vectorstore = pickle.load(f)


def set_openai_api_key(api_key: str):
    """Set the api key and return chain.
   If no api_key, then None is returned.
    """
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        chain = get_chain(vectorstore)
