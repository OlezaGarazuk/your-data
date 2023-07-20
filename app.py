import os
from typing import Optional, Tuple

import gradio as gr
import pickle
from query_data import get_chain
from threading import Lock

with open("vectorstore.pkl", "rb") as f:
