#!/usr/bin/env python3

import os
import datetime
import reports
import emails
def report_mail():
  lista = []
  txt_folder = os.path.join(os.path.expanduser('~'), 'supplier-data/descriptions')
  for txt_file in os.listdir(txt_folder):
    if txt_file.endswith('.txt'):
      with open(os.path.join(txt_folder, txt_file)) as f:
        lines = f.readlines()
      lista.append('name: ' + lines[0] + '<br/>')
      lista.append('weight: ' + lines[1] + '<br/>')
      lista.append('<br/>')

  return ''.join(lista)

def main():
  title = 'Processed Update on ' + datetime.date.today().strftime("%B %d, %Y")
  paragraph = report_mail()
  attachment = '/tmp/processed.pdf'
  reports.generate_report(attachment, title, paragraph)

  message = emails.generate('automation@example.com',
                           'student-00-bbdd69239573@example.com',
                           'Upload Completed - Online Fruit Store',
                           'All fruits are uploaded to our website successfully. A detailed list is atta$
                           attachment)
  emails.send(message)

main()
