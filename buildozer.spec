[app]

# (str) Title of your application
title = Calculator App

# (str) Package name
package.name = calcapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.calc

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
log_level = 2
