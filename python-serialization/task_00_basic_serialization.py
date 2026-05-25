#!/usr/bin/env python3
"""Modul to create basic serialization
"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize and save"""
    with open(filename, mode="w", encoding="utf-8") as file_name:
        json.dump(data, file_name)


def load_and_deserialize(filename):
    """load and deserialize"""
    with open(filename, mode="r", encoding="utf-8") as file_name:
        return json.load(file_name)
