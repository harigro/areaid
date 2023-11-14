import json
from typing import List, Dict, Sequence
import os.path as jalur


def jalur_berkas(nama_jalur: str, nama: str) -> str:
    objek = jalur.abspath(__file__)
    utama = jalur.dirname(objek)
    return jalur.join(utama, "{}/{}.json".format(nama_jalur, nama))

def buka_data(nama_berkas: str) -> List[Dict[str, Sequence]]:
    with open(jalur_berkas("data", nama_berkas)) as berkas:
        return json.load(berkas)

def buka_nama() -> List[Dict[str, Sequence]]:
    with open(jalur_berkas("nama", "provinsi")) as berkas:
        return json.load(berkas)