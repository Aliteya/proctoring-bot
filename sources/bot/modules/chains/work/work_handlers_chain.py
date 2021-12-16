from aiogram import types
import validators
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from bot.loggers import LogInstaller
from bot.modules.handlers_chain import HandlersChain
from bot.modules.handlers_registrar import HandlersRegistrar as Registrar


class Work(StatesGroup):
    waiting_for_link = State()


class WorkHandlersChain(HandlersChain):
    _logger = LogInstaller.get_default_logger(__name__, LogInstaller.DEBUG)

    @staticmethod
    @Registrar.message_handler(commands=["lab"], state="*")
    async def lab_start_handler(message: types.Message):
        WorkHandlersChain._logger.debug(f"Start lab conversation state")
        await message.answer("Отправьте ссылку на лабораторную работу")
        await Work.waiting_for_link.set()

    @staticmethod
    @Registrar.message_handler(state=Work.waiting_for_link)
    async def lab_link_send_handler(message: types.Message, state: FSMContext):
        if validators.url(str(message.text)):
            await state.update_data(works=message.text)
            await message.answer("Ссылка успешно добавлена")
            WorkHandlersChain._logger.debug(f"Finite lab conversation state")
            await state.finish()
        else:
            await message.answer("Пожалуйста отправьте действительную ссылку")
