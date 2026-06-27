import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes
)

TOKEN = os.environ.get("968281044:AAE×NF3BeWNu6SE8-N21j-sM_QXxa2zc018")
ADMIN_ID = int(os.environ.get("1960975949", "0"))
PRICE_BUY = int(os.environ.get("PRICE_BUY", "29"))

# التحقق من وجود التوكن
if not TOKEN:
    raise ValueError("❌ التوكن غير موجود! تأكد من تعيين متغير البيئة TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ===== رسالة الترحيب =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        keyboard = [
            [InlineKeyboardButton("💵 سعر اليوم", callback_data="price")],
            [InlineKeyboardButton("🛒 كيف أشتري؟", callback_data="how")],
            [InlineKeyboardButton("📩 تواصل مع المشرف", callback_data="contact")],
            [InlineKeyboardButton("❓ الأسئلة الشائعة", callback_data="faq")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "👋 أهلاً بك في *USDRedotpay DZ* 🇩🇿\n\n"
            "نقدم خدمة شراء وبيع USDT بأفضل سعر في الجزائر ✅\n"
            "⚡ التنفيذ خلال أقل من 5 دقائق\n\n"
            "اختر ما تريد من القائمة 👇",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"خطأ في start: {e}")

# ===== معالجة الأزرار =====
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        await query.answer()

        if query.data == "price":
            keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
            await query.edit_message_text(
                f"📊 *سعر اليوم:*\n\n"
                f"🟢 USDT: *{PRICE_BUY} DA*\n\n"
                f"⏱️ التنفيذ: أقل من 5 دقائق\n"
                f"✅ الحد الأدنى: 10 USDT\n\n"
                f"للطلب تواصل معنا مباشرة 👇",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif query.data == "how":
            keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
            await query.edit_message_text(
                "🛒 *طريقة الشراء:*\n\n"
                "1️⃣ تواصل مع المشرف\n"
                "2️⃣ أخبره بالمبلغ الذي تريده\n"
                "3️⃣ أرسل المبلغ بالدينار عبر CCP أو نقداً\n"
                "4️⃣ أرسل له عنوان محفظتك أو حساب RedotPay\n"
                "5️⃣ تستلم USDT خلال 5 دقائق ✅\n\n"
                "⚠️ *ملاحظة:* لا يتم الإرسال إلا بعد تأكيد الاستلام",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif query.data == "contact":
            keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
            await query.edit_message_text(
                "📩 *تواصل مع المشرف:*\n\n"
                "👤 @Oussamabenyahia\n\n"
                "⏰ أوقات العمل: 8 صباحاً - 10 مساءً\n"
                "⚡ متوسط وقت الرد: أقل من 10 دقائق",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif query.data == "faq":
            keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
            await query.edit_message_text(
                "❓ *الأسئلة الشائعة:*\n\n"
                "▪️ *ما هو الحد الأدنى؟*\n10 USDT\n\n"
                "▪️ *كيف أدفع؟*\nCCP / نقداً\n\n"
                "▪️ *هل الخدمة آمنة؟*\nنعم، لدينا سجل صفقات ✅\n\n"
                "▪️ *كم وقت التحويل؟*\nأقل من 5 دقائق ⚡",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif query.data == "back":
            keyboard = [
                [InlineKeyboardButton("💵 سعر اليوم", callback_data="price")],
                [InlineKeyboardButton("🛒 كيف أشتري؟", callback_data="how")],
                [InlineKeyboardButton("📩 تواصل مع المشرف", callback_data="contact")],
                [InlineKeyboardButton("❓ الأسئلة الشائعة", callback_data="faq")],
            ]
            await query.edit_message_text(
                "👋 أهلاً بك في *USDRedotpay DZ* 🇩🇿\n\n"
                "نقدم خدمة شراء وبيع USDT بأفضل سعر في الجزائر ✅\n"
                "⚡ التنفيذ خلال أقل من 5 دقائق\n\n"
                "اختر ما تريد من القائمة 👇",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
    except Exception as e:
        logger.error(f"خطأ في معالجة الزر: {e}")

# ===== أي رسالة نصية =====
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.lower() if update.message.text else ""

        if any(word in text for word in ["سعر", "price", "كم"]):
            await update.message.reply_text(
                f"📊 سعر اليوم: *{PRICE_BUY} DA* للـ USDT\n"
                f"⚡ تنفيذ خلال 5 دقائق\n\n"
                f"اكتب /start للقائمة الكاملة",
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text(
                "👋 اكتب /start لعرض القائمة الكاملة"
            )
    except Exception as e:
        logger.error(f"خطأ في معالجة الرسالة: {e}")

# ===== معالج الأخطاء =====
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"خطأ في البوت: {context.error}")

# ===== تشغيل البوت =====
def main():
    try:
        app = Application.builder().token(TOKEN).build()
        
        # إضافة المعالجات
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button_handler))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
        
        # إضافة معالج الأخطاء
        app.add_error_handler(error_handler)
        
        logger.info("✅ البوت يعمل الآن...")
        print("✅ البوت يعمل...")
        app.run_polling()
    except Exception as e:
        logger.error(f"❌ خطأ في بدء البوت: {e}")
        raise

if __name__ == "__main__":
    main()
