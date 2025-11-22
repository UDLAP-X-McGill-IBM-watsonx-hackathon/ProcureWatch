import os
import json
import base64
import pandas as pd
from typing import List, Optional, Literal
from pydantic import BaseModel, Field
import pymupdf
from openai import OpenAI

def convert_to_image(pdf_path: str, page_num: int) -> str:
    """Convert a PDF page to an image and return it as a base64 encoded string."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")
    else:   
        doc = pymupdf.open(pdf_path)
        page = doc[page_num]
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
        img_data = pix.tobytes('png')
        doc.close()
        img_base64 = base64.b64encode(img_data).decode('utf-8')

        return img_base64


