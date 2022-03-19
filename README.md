### About package

_This allows you to add a calendar to your telegram bot._

### Get Started

**Install package**

    pip install SACalendar 

**Simple example**

    from aiogram.contrib.fsm_storage.memory import MemoryStorage
    from aiogram.types import Message, CallbackQuery
    from CalendarBot import CalendarBot
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())
    my_calendar = CalendarBot()

    @dp.message_handler(CommandStart())
    async def start_working_with_bot(message: Message) -> None:
        await message.answer('YAHOO!', reply_markup=await my_calendar.enable())

    @dp.callback_query_handler(my_calendar.callback.filter())
    async def birthday_simple_calendar(call: CallbackQueryt) -> None:
        pass

### Demo
    
![image_calendar.webp](examples/image_calendar.webp)

### Description

This simple calendar supports 2 languages RU and EN.
To select a language, use:
    
    my_calendar = CalendarBot(language='EN')

Also, to improve the quality of the calendar display, you can transfer your time zone (default UTC)

    my_calendar = CalendarBot(tz='Europe/Vienna')

### Try it in action

-> `@my_Yuuko_bot`

