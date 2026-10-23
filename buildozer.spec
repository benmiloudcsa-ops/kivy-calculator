
[app]

# (str) عنوان أو اسم التطبيق الذي سيظهر للمستخدم
title = My Calculator

# (str) اسم الحزمة (يجب أن يكون بالإنجليزية وبدون مسافات أو رموز خاصة)
package.name = mycalculator

# (str) النطاق أو الدومين الخاص بالحزمة
package.domain = org.calc

# (list) الملفات المصدرية المضمنة في التطبيق
source.include_exts = py,png,jpg,kv,atlas

# (str) إصدار التطبيق
version = 0.1

# (list) المكتبات والحزم البرمجية التي يعتمد عليها تطبيقك
requirements = python3,kivy

# (str) اتجاه الشاشة (portrait للشاشة العمودية، landscape للأفقية)
orientation = portrait

# (list) الأذونات المطلوبة للتطبيق (إذا لزم الأمر)
android.permissions = INTERNET

[buildozer]
# (int) مستوى تفاصيل سجل الأخطاء (0 إلى 2)
log_level = 2
