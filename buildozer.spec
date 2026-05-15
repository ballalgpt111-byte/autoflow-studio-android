[app]

# Application title
title = AutoFlow Studio

# Package name
package.name = autoflowstudio

# Package domain (needed for android/ios packaging)
package.domain = com.bigtotalapps

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf

# Version
version = 1.0.0

# Application requirements
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,plyer,android

# Supported orientations
orientation = portrait

# Android specific
[app:android]

# Android API level
android.api = 31

# Minimum API level
android.minapi = 21

# Android SDK version
android.sdk = 31

# Android NDK version
android.ndk = 25b

# Android permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,CAMERA,RECORD_AUDIO

# Android features
android.features = android.hardware.camera,android.hardware.camera.autofocus

# Application icon
#icon.filename = %(source.dir)s/assets/icon.png

# Presplash background color
#presplash.color = #FFFFFF

# Presplash image
#presplash.filename = %(source.dir)s/assets/presplash.png

# Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# Android app theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# Copy library instead of making a symlink
android.copy_libs = 1

# Android logcat filters
android.logcat_filters = *:S python:D

# Android architecture
android.archs = arm64-v8a,armeabi-v7a

[buildozer]

# Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1

# Build directory
build_dir = ./.buildozer

# Binary directory
bin_dir = ./bin
