"""
  Ini adalah script sederhana,
  boleh untuk dipelajari.
  
  Terima kasih.
"""
from __future__ import print_function
import os
import json
import time
import shutil
import requests

def clearConsole():
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")
	else:
		pass

def main():
	clearConsole()
	print("\t\t\t[ I N F O R M A S I - G E M P A ]\n")
	url = f"https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
	req = requests.get(url).text
	res = json.loads(req)
	result = res['Infogempa']['gempa']

	print(f"[#] Tanggal   : {result['Tanggal']}, {result['Jam']}")
	print(f"[#] Source    : https://data.bmkg.go.id")
	print(f"\n[#] Kordinat  : {result['Coordinates']}")
	print(f"[#] Detail    : ({result['Lintang']}) ({result['Bujur']})")
	print(f"[#] Lokasi    : {result['Wilayah']}")
	print(f"[#] Magnitudo : {result['Magnitude']}")
	print(f"[#] Kedalaman : {result['Kedalaman']}")
	print(f"\n[#] Potensi   : {result['Potensi']}")
	print(f"[#] Dirasakan : {result['Dirasakan']}")

	img = f"https://ews.bmkg.go.id/TEWS/data/{result['Shakemap']}"
	filename = img.split("/")[-1]
	r = requests.get(img, stream = True)

	if r.status_code == 200:
	    r.raw.decode_content = True
	    with open(filename,'wb') as f:
	        shutil.copyfileobj(r.raw, f)
	    print('\n[#] Sukses download peta gempa : ',filename)
	else:
	    # print('\n[!] Gagal download peta gempa')
	    pass

	os.system(f"{filename}")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		clearConsole()
		print("[!] Have a nice day ...")
		time.sleep(2)
		exit()
