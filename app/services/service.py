import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).parent.parent / "data" / "instruments.json"

instruments: List[Dict] = []

def load_instruments():
    global instruments
    with open(DATA_FILE, "r") as f:
        instruments = json.load(f)

def sort_instruments(instruments, sort):
    return sorted(instruments, key=lambda x: x["pnl"], reverse=sort=="desc")

def fetch_all_instruments(sort: str|None):
    if sort:
        return sort_instruments(instruments,sort)
    return instruments 

def fetch_instruments_by_symbol(symbol: str, sort: str|None):
    filtered_instruments = [ins for ins in instruments if ins["symbol"] ==  symbol]
    if sort:
        return sort_instruments(filtered_instruments,sort)
    return filtered_instruments 
    