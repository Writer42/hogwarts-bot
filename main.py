import hashlib
from aiogram import Dispatcher, Bot, executor
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle, MessageEntity, InlineKeyboardButton, InlineKeyboardMarkup
from scripts.env import TOKEN
from scripts.wizard import Wizard


bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.inline_handler()
async def main(inline_query: InlineQuery):

    user_id = inline_query.from_user.id
    wizard_string = str(Wizard(user_id))
    wizard_info = InputTextMessageContent(wizard_string)
    
    button = InlineKeyboardButton("Узнать свои статы", switch_inline_query_current_chat="")
    markup = InlineKeyboardMarkup().add(button)

    result_id: str = hashlib.md5(wizard_string.encode()).hexdigest()

    item = InlineQueryResultArticle(
        id=result_id,
        title='А какой волшебник ты сегодня?',
        input_message_content=wizard_info,
        reply_markup=markup,
        thumb_url="https://images.fineartamerica.com/images/artworkimages/medium/3/harry-potter-hogwarts-school-crest-enxu-effie-transparent.png"

    )

    # don't forget to set cache_time=1 for testing (default is 300s or 5m)

    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)



