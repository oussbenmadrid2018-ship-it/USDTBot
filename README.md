
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes
)

# توكن البوت من BotFather
TOKEN = "8968281044:AAExNF3BeWNu6SE8-N21j-sM_QXxa2zcO18"

# رقم حسابك في تيليغرام (لاستقبال إشعارات الطلبات)
ADMIN_ID = 1960975949

# السعر اليومي — غيّره كل يوم
PRICE_BUY = 29  # سعر البيع للعميل

logging.basicConfig(level=logging.INFO)

# ===== رسالة الترحيب =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

# ===== معالجة الأزرار =====
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

# ===== أي رسالة نصية =====
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

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

# ===== تشغيل البوت =====
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    print("✅ البوت يعمل...")
    app.run_polling()

if __name__ == "__main__":
    main()