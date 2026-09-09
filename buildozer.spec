[app]
title = NeonDash
package.name = neondash
package.domain = org.oyun

source.dir = .
source.exclude_dirs = tests, bin, venv, .git, .github, .buildozer, __pycache__
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,ogg
source.exclude_exts = spec

requirements = python3,kivy

version = 1.0.0
orientation = landscape
fullscreen = 0

#
# Android ayarlari
#
# NOT: android.api / android.minapi / android.ndk pinlemeyi birak;
# guncel buildozer imaji saglikli varsayilanlari kullanir
# (api 36, minapi 24, ndk 28c). Istersen asagidakileri ac:
#
# android.api = 36
# android.minapi = 24
# android.ndk = 28c

# Sadece 64-bit cihazlar icin derler (yaklasik 2 kat daha hizli build).
# 32-bit cihaz destegi gerekirse: android.archs = arm64-v8a, armeabi-v7a
android.archs = arm64-v8a

# SDK lisansini otomatik kabul eder (CI'da zorunlu).
# DIKKAT: dogru anahtar "android.accept_sdk_license".
# "android.accept_sdk_license_agreement" diye bir anahtar YOK, yok sayilir!
android.accept_sdk_license = True

p4a.bootstrap = sdl2

[buildozer]
warn_on_root = 0
log_level = 2
