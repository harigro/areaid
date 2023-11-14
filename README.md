# Ucapan Sambutan
Terima kasih telah memilih pustaka ini untuk menangani kesulitan dalam mengisi formulir yang membutuhkan data alamat secara lengkap berserta kode posnya. Pustaka ini memiliki data yang lengkap perihal wilayah administrasi di indonesia, mulai data nama provinsi, kabupaten, kecamatan, dan kelurahan/desa berserta kode posnya.

## Cara Instalasi
Cukup mudah tinggal salin teks dibawah ini dan tempelkan diterminal
```
pip install areaid
```

## Cara Menggunakan Dan Contoh Program
Ada dua fungsi utama di pustaka ini, **buka_data** dan **buka_nama**\
**buka_data** berfungsi untuk membuka berkas json berdasarkan nama berkas json\n
**buka_nama** berfungsi unutk membuka berkas json untuk melihat nama - nama provinsi\
berikut contoh cara menggunakan kedua fungsi\

---

contoh **buka_data**
```python
from areaid import buka_data

# di contoh ini menggunakan aceh
bb = buka_data("aceh")
print(bb)
```
---
contoh **buka_nama**
```python
from areaid import buka_nama, buka_data

# fungsi buka_nama() berguna untuk melihat nama provinsi yang digunakan sebagai parameter buka_data()
bb = buka_nama()
print(bb)

# menggunakan buka_nama sebagai parameter
dd = buka_data(bb["himpunan"][3].lower())
print(dd)
```

## Sumber 
Data pada repositori ini diolah dan dibuat berdasarkan [github.com/ichadhr/db-wilayah-indonesia](https://github.com/ichadhr/db-wilayah-indonesia)


