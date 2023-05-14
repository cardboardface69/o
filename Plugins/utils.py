import re
import asyncio
from pyrogram import Client
from math import floor
import os
import cv2, random
from string import ascii_letters, ascii_uppercase, digits
from pyrogram.types import Message, MessageEntity
from pyrogram.errors import FloodWait
from base64 import standard_b64encode, standard_b64decode

def b64_to_str(b64: str) -> str:
    bytes_b64 = b64.encode('ascii')
    bytes_str = standard_b64decode(bytes_b64)
    __str = bytes_str.decode('ascii')
    return __str
