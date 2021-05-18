#!/usr/bin/env python3
import requests
import os

def upload_images(url, im_folder):
  for image in os.listdir(im_folder):
    if image.endswith('.jpeg'):
      with open(os.path.join(im_folder, image), 'rb') as opened:
        r = requests.post(url, files={'file': opened})


def main():
  url = "http://localhost/upload/"
  image_folder = os.path.join(os.path.expanduser("~"), 'supplier-data/images')
  upload_images(url, image_folder)


main()
