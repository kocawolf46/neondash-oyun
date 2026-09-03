[app]
title = NeonDash
package.name = neondash
package.domain = org.oyun
source.dir =.
source.exclude_dirs = tests, bin, venv,.git,.github,.buildozer, __pycache__
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,ogg
source.exclude_exts = spec
requirements = python3,pygame
version = 1.0.0
orientation = landscape
fullscreen = 0

# ANDROID - KESIN CALISAN AYAR
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2

[buildozer]
warn_on_root = 0
log_level = 2
