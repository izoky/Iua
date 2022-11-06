"""
انشاء قاعدة بيانات
"""
from db import make, insert

if __name__ == '__main__':
    make()
    insert(table_name='message', args=("start", "اهلا مع هذا البوت تستطيع المحادثة بسرية تامة مع شخص عشوائي ومجهول الهوية\nلمعرفة طريقة استخدام البوت: /help\nيمكنك الاطلاع على قناة السورس t.me/R125R\n\nعند ادخال اسم مستعار واستخدم البوت فأنت توافق على سياسة الخصوصية والشروط والاحكام\nالشروط والاحكام: /terms_and_conditions\nسياسة الخصوصية: /privacy_policy"))
    insert(table_name='message', args=("help", "اهلا طريقة استخدام البوت بسيطة جدا\nيمكنك بدا جلسة عبر هذا الامر /search\nويمكنك تغير الاسم المستعار الخاص بك عبر هذا الامر /new_name\nويمكنك قطع الجلسة التي بينك وبين العضو الاخر عبر هذا الامر /kill\nلمعرفة اسمك المستعار /my_name\nوللتبليغ على عضو ارسل هذا الامر بالجلسة: /report\nلمسح رسالة في الجلسة سوي ربلي على الرسالة المراد مسحها بـ'مسح'"))
    insert(table_name='message', args=("no_user", "اهلا بك، قبل البدء في دخول الجلسات يجب عليك اختيار اسم مستعار لك  \n \n تنويه: \n سوف يتم عرض الاسم المستعار للشخص المشارك معك بالجلسة"))
    insert(table_name='message', args=("not_private", "عذرا لحفظ خصوصية المستخدمين لايمكن انشاء جلسة في محادثة عامة"))