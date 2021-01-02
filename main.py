from aiogram import executor, types
from misc import dp, bot
import hashlib


@dp.inline_handler()
async def welcome_to_the_cum_zone(inline_query: types.InlineQuery):
    text = "/WELCOME /TO /THE /CUM /ZONE /ONLY /CUM /INSIDE /ANIME /GIRLS"
    input_content = types.InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = types.InlineQueryResultArticle(
        id=result_id,
        title=f'/WELCOME /TO /THE /CUM /ZONE',
        input_message_content=input_content,
    )
    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=300)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)