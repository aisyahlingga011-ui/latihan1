"""
REGISTRASI KARTU KELUARGA (Python, terminal)
Fitur: tambah KK, tambah anggota, lihat, cari, ubah, hapus
Data disimpan di data_kk.json (satu folder dengan file ini)
"""

import json
import os
from datetime import datetime

FILE_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_kk.json")

JENIS_KELAMIN = ["Laki-laki", "Perempuan"]
AGAMA = ["Islam", "Kristen", "Katolik", "Hindu", "Buddha", "Konghucu"]
STATUS_KAWIN = ["Belum Kawin", "Kawin", "Cerai Hidup", "Cerai Mati"]
HUBUNGAN = ["Istri", "Anak", "Orang Tua", "Famili Lain"]  # kepala keluarga diisi otomatis

FIELD_KK = {
    "1": ("alamat", "Alamat"),
    "2": ("rt_rw", "RT/RW"),
    "3": ("kelurahan", "Desa/Kelurahan"),
    "4": ("kecamatan", "Kecamatan"),
    "5": ("kota", "Kabupaten/Kota"),
    "6": ("provinsi", "Provinsi"),
    "7": ("kode_pos", "Kode Pos"),
}

FIELD_ANGGOTA = {
    "1": ("nama", "Nama Lengkap"),
    "2": ("jenis_kelamin", "Jenis Kelamin"),
    "3": ("tempat_lahir", "Tempat Lahir"),
    "4": ("tanggal_lahir", "Tanggal Lahir"),
    "5": ("agama", "Agama"),
    "6": ("pendidikan", "Pendidikan"),
    "7": ("pekerjaan", "Pekerjaan"),
    "8": ("status_kawin", "Status Perkawinan"),
    "9": ("hubungan", "Hubungan dalam Keluarga"),
    "10": ("nama_ayah", "Nama Ayah"),
    "11": ("nama_ibu", "Nama Ibu"),
}


# ======================= FILE =======================
def muat_data():
    if not os.path.exists(FILE_DATA):
        return {}
    try:
        with open(FILE_DATA, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Peringatan: file data rusak, memulai dengan data kosong.")
        return {}


def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# ======================= INPUT & VALIDASI =======================
def input_teks(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("  ! Tidak boleh kosong.")


def input_angka(pesan, panjang):
    while True:
        nilai = input(pesan).strip()
        if nilai.isdigit() and len(nilai) == panjang:
            return nilai
        print(f"  ! Harus tepat {panjang} digit angka.")


def input_tanggal(pesan):
    while True:
        nilai = input(f"{pesan} (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(nilai, "%d-%m-%Y")
            return nilai
        except ValueError:
            print("  ! Format salah. Contoh: 17-08-2000")


def input_pilihan(judul, daftar):
    print(judul)
    for i, item in enumerate(daftar, 1):
        print(f"  {i}. {item}")
    while True:
        nomor = input("  Pilih nomor: ").strip()
        if nomor.isdigit() and 1 <= int(nomor) <= len(daftar):
            return daftar[int(nomor) - 1]
        print("  ! Pilihan tidak valid.")


def konfirmasi(pesan):
    while True:
        jawab = input(f"{pesan} (y/n): ").strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  ! Ketik y atau n.")


# ======================= PENCARIAN =======================
def nik_terdaftar(data, nik):
    """Return No. KK tempat NIK terdaftar, atau None."""
    for no_kk, kk in data.items():
        for a in kk["anggota"]:
            if a["nik"] == nik:
                return no_kk
    return None


def cari_anggota(kk, nik):
    for a in kk["anggota"]:
        if a["nik"] == nik:
            return a
    return None


def pilih_kk(data):
    """Tampilkan daftar KK, lalu user pilih dengan nomor urut ATAU No. KK."""
    if not data:
        print("\nBelum ada data Kartu Keluarga. Tambahkan dulu lewat menu 1.")
        return None

    daftar = list(data.keys())
    print("\nDaftar KK:")
    for i, no_kk in enumerate(daftar, 1):
        print(f"  {i}. {no_kk} - {data[no_kk]['kepala_keluarga']}")

    pilihan = input("Pilih nomor urut atau ketik No. KK: ").strip()
    if pilihan in data:
        return pilihan
    if pilihan.isdigit() and 1 <= int(pilihan) <= len(daftar):
        return daftar[int(pilihan) - 1]
    print("Data tidak ditemukan.")
    return None


# ======================= INPUT ANGGOTA =======================
def input_anggota(data, hubungan_tetap=None):
    print("\n--- Data Anggota Keluarga ---")
    while True:
        nik = input_angka("NIK (16 digit)       : ", 16)
        ada = nik_terdaftar(data, nik)
        if ada:
            print(f"  ! NIK sudah terdaftar di KK {ada}.")
        else:
            break

    a = {"nik": nik}
    a["nama"] = input_teks("Nama lengkap         : ")
    a["jenis_kelamin"] = input_pilihan("Jenis kelamin:", JENIS_KELAMIN)
    a["tempat_lahir"] = input_teks("Tempat lahir         : ")
    a["tanggal_lahir"] = input_tanggal("Tanggal lahir")
    a["agama"] = input_pilihan("Agama:", AGAMA)
    a["pendidikan"] = input_teks("Pendidikan           : ")
    a["pekerjaan"] = input_teks("Jenis pekerjaan      : ")
    a["status_kawin"] = input_pilihan("Status perkawinan:", STATUS_KAWIN)
    if hubungan_tetap:
        a["hubungan"] = hubungan_tetap
    else:
        a["hubungan"] = input_pilihan("Hubungan dalam keluarga:", HUBUNGAN)
    a["kewarganegaraan"] = "WNI"
    a["nama_ayah"] = input_teks("Nama ayah            : ")
    a["nama_ibu"] = input_teks("Nama ibu             : ")
    return a


# ======================= TAMPILAN =======================
def tampil_kk(no_kk, kk):
    garis = "=" * 78
    print("\n" + garis)
    print("KARTU KELUARGA".center(78))
    print(f"No. KK : {no_kk}".center(78))
    print(garis)
    print(f"Kepala Keluarga : {kk['kepala_keluarga']}")
    print(f"Alamat          : {kk['alamat']}")
    print(f"RT/RW           : {kk['rt_rw']}")
    print(f"Kelurahan       : {kk['kelurahan']}")
    print(f"Kecamatan       : {kk['kecamatan']}")
    print(f"Kab/Kota        : {kk['kota']}")
    print(f"Provinsi        : {kk['provinsi']}")
    print(f"Kode Pos        : {kk['kode_pos']}")
    print(f"Dikeluarkan     : {kk['tanggal_dikeluarkan']}")
    print("-" * 78)
    print(f"{'No':<4}{'NIK':<18}{'Nama':<24}{'JK':<11}{'Hubungan'}")
    print("-" * 78)
    for i, a in enumerate(kk["anggota"], 1):
        print(f"{i:<4}{a['nik']:<18}{a['nama'][:22]:<24}"
              f"{a['jenis_kelamin']:<11}{a['hubungan']}")
    print(garis)


def tampil_detail_anggota(a):
    print("\n--- Detail Anggota ---")
    print(f"NIK               : {a['nik']}")
    print(f"Nama              : {a['nama']}")
    print(f"Jenis kelamin     : {a['jenis_kelamin']}")
    print(f"Tempat, tgl lahir : {a['tempat_lahir']}, {a['tanggal_lahir']}")
    print(f"Agama             : {a['agama']}")
    print(f"Pendidikan        : {a['pendidikan']}")
    print(f"Pekerjaan         : {a['pekerjaan']}")
    print(f"Status kawin      : {a['status_kawin']}")
    print(f"Hubungan          : {a['hubungan']}")
    print(f"Kewarganegaraan   : {a['kewarganegaraan']}")
    print(f"Nama ayah         : {a['nama_ayah']}")
    print(f"Nama ibu          : {a['nama_ibu']}")


# ======================= FITUR =======================
def tambah_kk(data):
    print("\n=== TAMBAH KARTU KELUARGA ===")
    while True:
        no_kk = input_angka("No. KK (16 digit)   : ", 16)
        if no_kk in data:
            print("  ! No. KK sudah terdaftar.")
        else:
            break

    kk = {
        "kepala_keluarga": "",
        "alamat": input_teks("Alamat              : "),
        "rt_rw": input_teks("RT/RW (cth 001/002) : "),
        "kelurahan": input_teks("Desa/Kelurahan     : "),
        "kecamatan": input_teks("Kecamatan          : "),
        "kota": input_teks("Kabupaten/Kota     : "),
        "provinsi": input_teks("Provinsi           : "),
        "kode_pos": input_angka("Kode pos (5 digit) : ", 5),
        "tanggal_dikeluarkan": input_tanggal("Tanggal dikeluarkan"),
        "anggota": [],
    }

    print("\nSekarang isi data Kepala Keluarga.")
    kepala = input_anggota(data, hubungan_tetap="Kepala Keluarga")
    kk["kepala_keluarga"] = kepala["nama"]
    kk["anggota"].append(kepala)

    data[no_kk] = kk
    simpan_data(data)
    print("\nData KK berhasil disimpan.")


def tambah_anggota(data):
    print("\n=== TAMBAH ANGGOTA KELUARGA ===")
    no_kk = pilih_kk(data)
    if no_kk is None:
        return
    anggota = input_anggota(data)
    data[no_kk]["anggota"].append(anggota)
    simpan_data(data)
    print("\nAnggota berhasil ditambahkan.")


def lihat_semua(data):
    print("\n=== DAFTAR KARTU KELUARGA ===")
    if not data:
        print("Belum ada data.")
        return
    print("-" * 70)
    print(f"{'No':<4}{'No. KK':<20}{'Kepala Keluarga':<30}{'Jml Anggota'}")
    print("-" * 70)
    for i, (no_kk, kk) in enumerate(data.items(), 1):
        print(f"{i:<4}{no_kk:<20}{kk['kepala_keluarga'][:28]:<30}{len(kk['anggota'])}")
    print("-" * 70)


def lihat_detail(data):
    print("\n=== DETAIL SATU KK ===")
    no_kk = pilih_kk(data)
    if no_kk is None:
        return
    tampil_kk(no_kk, data[no_kk])


def cari_data(data):
    print("\n=== CARI DATA ===")
    if not data:
        print("Belum ada data.")
        return
    print("1. Berdasarkan No. KK")
    print("2. Berdasarkan NIK")
    print("3. Berdasarkan nama")
    pilih = input("Pilih: ").strip()

    if pilih == "1":
        no_kk = input("No. KK: ").strip()
        if no_kk in data:
            tampil_kk(no_kk, data[no_kk])
        else:
            print("Data tidak ditemukan.")
    elif pilih == "2":
        nik = input("NIK: ").strip()
        no_kk = nik_terdaftar(data, nik)
        if no_kk:
            tampil_detail_anggota(cari_anggota(data[no_kk], nik))
            print(f"\n(Terdaftar di KK {no_kk})")
        else:
            print("Data tidak ditemukan.")
    elif pilih == "3":
        kata = input("Nama (boleh sebagian): ").strip().lower()
        hasil = [(no_kk, a) for no_kk, kk in data.items()
                 for a in kk["anggota"] if kata and kata in a["nama"].lower()]
        if not hasil:
            print("Data tidak ditemukan.")
        else:
            print(f"\nDitemukan {len(hasil)} data:")
            for no_kk, a in hasil:
                print(f"- {a['nama']} | NIK {a['nik']} | {a['hubungan']} | KK {no_kk}")
    else:
        print("Pilihan tidak valid.")


def ubah_data(data):
    print("\n=== UBAH DATA ===")
    no_kk = pilih_kk(data)
    if no_kk is None:
        return
    kk = data[no_kk]
    tampil_kk(no_kk, kk)

    print("\n1. Ubah data KK (alamat, dll.)")
    print("2. Ubah data anggota")
    pilih = input("Pilih: ").strip()

    if pilih == "1":
        for kode, (_, label) in FIELD_KK.items():
            print(f"  {kode}. {label}")
        kode = input("Pilih data yang diubah: ").strip()
        if kode not in FIELD_KK:
            print("Pilihan tidak valid.")
            return
        kunci, label = FIELD_KK[kode]
        if kunci == "kode_pos":
            kk[kunci] = input_angka("Kode pos baru (5 digit): ", 5)
        else:
            kk[kunci] = input_teks(f"{label} baru: ")
        simpan_data(data)
        print("Data berhasil diubah.")

    elif pilih == "2":
        nik = input("NIK anggota: ").strip()
        a = cari_anggota(kk, nik)
        if a is None:
            print("Anggota tidak ditemukan di KK ini.")
            return
        tampil_detail_anggota(a)
        print()
        for kode, (_, label) in FIELD_ANGGOTA.items():
            print(f"  {kode}. {label}")
        kode = input("Pilih data yang diubah: ").strip()
        if kode not in FIELD_ANGGOTA:
            print("Pilihan tidak valid.")
            return
        kunci, label = FIELD_ANGGOTA[kode]

        if kunci == "jenis_kelamin":
            a[kunci] = input_pilihan("Jenis kelamin baru:", JENIS_KELAMIN)
        elif kunci == "agama":
            a[kunci] = input_pilihan("Agama baru:", AGAMA)
        elif kunci == "status_kawin":
            a[kunci] = input_pilihan("Status baru:", STATUS_KAWIN)
        elif kunci == "tanggal_lahir":
            a[kunci] = input_tanggal("Tanggal lahir baru")
        elif kunci == "hubungan":
            if a["hubungan"] == "Kepala Keluarga":
                print("Hubungan kepala keluarga tidak bisa diubah.")
                return
            a[kunci] = input_pilihan("Hubungan baru:", HUBUNGAN)
        else:
            a[kunci] = input_teks(f"{label} baru: ")

        if kunci == "nama" and a["hubungan"] == "Kepala Keluarga":
            kk["kepala_keluarga"] = a["nama"]

        simpan_data(data)
        print("Data berhasil diubah.")
    else:
        print("Pilihan tidak valid.")


def hapus_data(data):
    print("\n=== HAPUS DATA ===")
    no_kk = pilih_kk(data)
    if no_kk is None:
        return
    kk = data[no_kk]
    tampil_kk(no_kk, kk)

    print("\n1. Hapus seluruh KK")
    print("2. Hapus satu anggota")
    pilih = input("Pilih: ").strip()

    if pilih == "1":
        if konfirmasi("Yakin ingin menghapus seluruh KK ini?"):
            del data[no_kk]
            simpan_data(data)
            print("KK berhasil dihapus.")
        else:
            print("Dibatalkan.")
    elif pilih == "2":
        nik = input("NIK anggota: ").strip()
        a = cari_anggota(kk, nik)
        if a is None:
            print("Anggota tidak ditemukan di KK ini.")
            return
        if a["hubungan"] == "Kepala Keluarga":
            print("Kepala keluarga tidak bisa dihapus satuan. Hapus seluruh KK jika perlu.")
            return
        if konfirmasi(f"Yakin ingin menghapus {a['nama']}?"):
            kk["anggota"].remove(a)
            simpan_data(data)
            print("Anggota berhasil dihapus.")
        else:
            print("Dibatalkan.")
    else:
        print("Pilihan tidak valid.")


# ======================= MENU UTAMA =======================
def tampil_menu():
    print("\n" + "=" * 40)
    print("   REGISTRASI KARTU KELUARGA")
    print("=" * 40)
    print("1. Tambah Kartu Keluarga")
    print("2. Tambah Anggota Keluarga")
    print("3. Lihat Semua Kartu Keluarga")
    print("4. Cari Data")
    print("5. Ubah Data")
    print("6. Hapus Data")
    print("7. Lihat Detail Satu KK")
    print("0. Keluar")


def main():
    data = muat_data()
    while True:
        tampil_menu()
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            tambah_kk(data)
        elif pilih == "2":
            tambah_anggota(data)
        elif pilih == "3":
            lihat_semua(data)
        elif pilih == "4":
            cari_data(data)
        elif pilih == "5":
            ubah_data(data)
        elif pilih == "6":
            hapus_data(data)
        elif pilih == "7":
            lihat_detail(data)
        elif pilih == "0":
            print("Terima kasih. Data tersimpan di", FILE_DATA)
            break
        else:
            print("Menu tidak valid. Pilih 0-7.")


if __name__ == "__main__":
    main()