from fastapi import APIRouter, HTTPException, Query
from app.services.service import fetch_all_instruments, fetch_instruments_by_symbol

router = APIRouter()

@router.get("/instruments")
def get_all_instruments(sort: str | None = Query(None, regex="^(asc|desc)$")):
    """
    Returns all instruments. Optional query param `sort`:
    - sort=asc  → sort by pnl ascending
    - sort=desc → sort by pnl descending
    """
    return fetch_all_instruments(sort)


@router.get("/instruments/{symbol}")
def get_instruments_by_symbol(symbol: str, sort: str | None = Query(None, regex="^(asc|desc)$")):
    """
    Returns instruments by symbol. Optional query param `sort`:
    - sort=asc  → sort by pnl ascending
    - sort=desc → sort by pnl descending
    """
    instruments = fetch_instruments_by_symbol(symbol, sort)
    if not instruments:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return instruments