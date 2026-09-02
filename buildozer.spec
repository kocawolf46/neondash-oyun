[app]

# (str) Title of your application
title = NeonDash

# (str) Package name
package.name = neondash

# (str) Package domain (needed for android packaging)
package.domain = org.oyun

# (list) Source files to include (let it include all)
source.dir = .

# (list) Source files to exclude (let it be empty)
source.exclude_exts = spec

# (list) List of extensions to include in source files
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,ogg

# (list) Application requirements
# (If your project uses pygame instead of kivy, make sure requirements match)
requirements = python3,pygame

# (str) Version of the application
version = 0.1

# (list) Supported orientations
orientation = landscape

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# Android SDK ve NDK ayarları (Buildozer hata yapmasın diye sabitlendi)
android.sdk = 33
android.min_api = 21
android.ndk = 25b
android.accept_sdk_license = True

# (list) Permissions
# android.permissions = INTERNET

[buildozer]

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
