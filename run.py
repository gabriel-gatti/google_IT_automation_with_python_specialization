#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import json

def process_txts(txt_folder):
  data = []
  for txt in os.listdir(txt_folder):
    if txt.endswith('.txt'):
      with open(os.path.join(txt_folder, txt), 'r') as f:
        lines = f.readlines()
      temp_dict = {"name": lines[0].replace("\n", ""),
        "weight": int(lines[1].replace(" lbs\n", "")),
        "description": lines[2].replace("\n", ""),
        "image_name": txt.replace(".txt", ".jpeg")}
      data.append(json.dumps(temp_dict))

  return data

def main():
  fruits = process_txts(os.path.join(os.path.expanduser('~'), 'supplier-data/descriptions'))
  for fruit in fruits:
    x = requests.post( 'http://34.122.201.204/fruits', data=fruit)
    print(fruit)
    print(str(x.status_code))

main()
