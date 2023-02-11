#!/usr/bin/python3
"""
File that declare a package
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
