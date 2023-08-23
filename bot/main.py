import os

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from ml_model_class import RobertaBaseSquad2
from keyboards import main_menu_keyboard, back_to_the_main_menu_keyboard

load_dotenv()

storage = MemoryStorage()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot,
                storage=storage)


class ClientStatesGroup(StatesGroup):
    question = State()
    context = State()


ml_model = RobertaBaseSquad2()

START_TEXT = (
    'Welcome to the DeviA\'nts bot! '
    'In this bot, you can ask a question to the RobertaBaseSquad2 model. '
    'The model accepts the question itself as input, as well as the context '
    'in which the model will search for the answer. '
    'To start, click "Ask a question".'
)


async def on_startup(_):
    print('Бот успешно запущен!')


@dp.message_handler(commands=['start'], state=None)
async def start_command(message: types.Message) -> None:
    await message.answer(text=START_TEXT,
                         reply_markup=main_menu_keyboard)


@dp.message_handler(Text(equals='Back to the main menu'), state='*')
async def back_main_menu(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('Welcome back to the main menu',
                         reply_markup=main_menu_keyboard)
    await state.finish()


@dp.message_handler(Text(equals='Ask a question'), state=None)
async def ask_command(message: types.Message) -> None:
    await ClientStatesGroup.question.set()
    await message.answer('Please send us a question',
                         reply_markup=back_to_the_main_menu_keyboard)


@dp.message_handler(state=ClientStatesGroup.question)
async def save_question(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['question'] = message.text
    await message.answer('Ok! Please send the context')
    await ClientStatesGroup.context.set()


@dp.message_handler(state=ClientStatesGroup.context)
async def save_context_and_send_answer(message: types.Message,
                                       state: FSMContext) -> None:
    async with state.proxy() as data:
        question = data['question']
    context = message.text
    answer = ml_model.get_answer(question=question, context=context)
    await message.answer('Ok! This is your answer:')
    await message.answer(answer,
                         reply_markup=main_menu_keyboard)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
