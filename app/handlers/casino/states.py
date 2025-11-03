from aiogram.fsm.state import State, StatesGroup


class SlotStates(StatesGroup):
    waiting_for_bet = State()
