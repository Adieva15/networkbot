from aiogram.fsm.state import StatesGroup, State


class StyleTransferStates(StatesGroup):
    waiting_content = State()
    waiting_style = State()

class MemeState(StatesGroup):
    waiting_text=State()