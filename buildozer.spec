[app]

# (str) Uygulama basligi
title = NeonDash

# (str) Paket adi -> uygulama ID: org.oyun.neondash
package.name = neondash
package.domain = org.oyun

# (str) main.py'nin bulundugu klasor
source.dir = .

# (list) APK'ya girecek uzantilar. Bu liste tanimliyken SADECE bunlar paketlenir.
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,wav,ogg,mp3,json,txt

# (list) Haric tutulacaklar
source.exclude_exts = spec,pyc
source.exclude_dirs = tests, bin, venv, __pycache__
source.exclude_patterns = */__pycache__/*,*.pyc

# (list) Gereksinimler.
# Kivy icin python3 surumunu SABITLEMEYE GEREK YOK: p4a'nin kivy recipe'i
# Kivy 2.3.1'i "no-ast-str.patch" ve "use_cython.patch" ile yeni Python
# surumlerine (3.12/3.13/3.14) karsi derlenebilir hale getiriyor.
# Bu kombinasyon p4a'nin kendi CI'inda her push'ta build ediliyor.
requirements = python3,kivy

# (str) Surum
version = 1.0.0

# (list) Yon
orientation = landscape

# (bool) Tam ekran (1 = durum cubugunu gizler)
fullscreen = 0

# (str) Ikon / acilis ekrani (dosyalarin varsa yorumu kaldir)
#icon.filename = %(source.dir)s/data/icon.png
#presplash.filename = %(source.dir)s/data/presplash.png

#
# --- ANDROID ---
#

# (int) Hedef API. 35 = p4a'nin CI'inda test ettigi deger.
# Bos birakirsan buildozer 36 kullanir (o da calisir ama daha az test edildi).
android.api = 35

# (int) Desteklenen en dusuk API (buildozer varsayilani 24, p4a onerisi 24)
android.minapi = 24

# (str) NDK. Bos birakilirsa p4a'nin RECOMMENDED_NDK_VERSION degeri (28c) kullanilir.
# Sorun cikarsa yorumu kaldirip 25b'ye duser:
#android.ndk = 25b

# (list) Sadece 64-bit -> yaklasik 2 kat daha hizli build.
# 32-bit cihaz destegi: android.archs = arm64-v8a, armeabi-v7a
# Emulatorde test:      android.archs = arm64-v8a, x86_64
android.archs = arm64-v8a

# (bool) SDK lisansini otomatik kabul et -> CI'da ZORUNLU.
# Dogru anahtar budur; "android.accept_sdk_license_agreement" diye bir anahtar
# YOKTUR, buildozer onu sessizce yok sayar ve sdkmanager "Accept? (y/N)"
# ekraninda bekleyip job'u kilitler.
android.accept_sdk_license = True

# (bool) Otomatik yedekleme
android.allow_backup = False

# NOT: "android.build_tools_version" diye bir anahtar YOKTUR (buildozer 1.5 ve
# master'da desteklenmiyor). Buildozer SDK'daki en yeni build-tools'u otomatik secer.

#
# --- python-for-android ---
#

# (str) p4a dali. develop = p4a'nin CI'inda test edilen, en guncel dal.
# Daha kararli/degismeyen bir surum istersen: p4a.branch = master
p4a.branch = develop

# (str) Bootstrap. Kivy icin dogru olan sdl2.
p4a.bootstrap = sdl2

[buildozer]

# (int) Log seviyesi (0 = sadece hata, 1 = info, 2 = debug + komut ciktilari)
log_level = 2

# (int) root uyarisi (0 = kapali) -> CI icin dogru
warn_on_root = 0
