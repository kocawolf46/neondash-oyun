[app]

# (str) Title of your application
title = NeonDash

# (str) Package name
package.name = neondash

# (str) Package domain (needed for android packaging)
package.domain = org.oyun

# (list) Source files to include
source.dir =.

source.exclude_dirs = tests, bin, venv,.git,.github,.buildozer, __pycache__

source.include_patterns = assets/*,images/*,fonts/*,sounds/*

# (list) Source files to exclude
source.exclude_exts = spec

# (list) List of extensions to include
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,ogg

# (list) Application requirements
requirements = python3,pygame

# (str) Version of the application
version = 1.0.0

# (list) Supported orientations
orientation = landscape

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
#android.permissions = INTERNET

#
# Android Specific
#
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

# Pygame icin SDL2 kullanimi sart
p4a.bootstrap = sdl2

[buildozer]

# (int) Display warning if buildozer is run as root
warn_on_root = 1

log_level = 2
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True

# BU SATIR COZUMUN KILIDI
android.build_tools_version = 33.0.2

p4a.bootstrap = sdl2
p4a.local_recipes =
