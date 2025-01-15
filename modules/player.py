import streamlit as st

class Player:

    def __init__(self):

        self.money: float = 1000
        self.cards: list = []
        self.bet: int = 0
    
    def __repr__(self):
        return f"money: {self.money}, cards: {self.cards}, bet: {self.bet}"