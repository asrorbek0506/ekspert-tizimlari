# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O863a-Tsz6s5IfSsvsoDIRjADuVmrok6
"""

def kasallik_tashxisi(alomat):
  if alomat=="bosh ogriq, istma":
    return "sizda girip bor"
  elif alomat=="qorin, og'riq":
    return "sizda spazma bor"
  elif alomat=="istma, charchoq":
    return "sizda shamaollash"
  elif alomat=="bosh ogrigi":
    return "ogriq qoldiruvchi iching"
  elif alomat=="bel ogrigi":
    return "quypen mazi"
  else:
    return "noaniq kassalik shifokorga boring"
alomat=input("Alomatni kiriting ")
natija=kasallik_tashxisi(alomat)
print(natija)