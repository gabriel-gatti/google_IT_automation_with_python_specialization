#!/usr/bin/env python3

from PIL import Image
import os

def process_image(old_path, new_path):
  im = Image.open(old_path).convert('RGB').resize((600, 400))
  im.save(new_path)

def main():
  base_path = home = os.path.expanduser("~") + '/supplier-data/images'
  for file in os.listdir(base_path):
    if file.endswith('.tiff'):
      process_image(os.path.join(base_path, file), os.path.join(base_path,
        file.replace('.tiff', '.jpeg')))

main()
