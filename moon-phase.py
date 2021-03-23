#!/usr/bin/python3

from datetime import datetime
import math

current_day = datetime.now()
def get_julian_day_number(date: datetime) -> int:
    year, month, day = current_day.year, current_day.month, current_day.day
    
    if month == 1 or month == 2:
        year = year - 1
        month = month + 12

    centuries = year // 100
    quarter_centuries = centuries // 4
    c = 2 - centuries + quarter_centuries
    days_from_years = math.floor(365.25 * (year + 4716))
    days_from_months = math.floor(30.6001 * (month + 1))

    julian_day = c + day + days_from_years + days_from_months - 1524.5
    
    return math.floor(julian_day)
    
def moon_phase_on_julian_day(julian_day: int) -> float:
    # The magic number here is the julian day number of the new moon on 
    # 1/6/2000
    days_since_known_new = julian_day - 2451549.5
    
    moon_phase = (days_since_known_new / 29.53) % 1

    return moon_phase

def get_emoji_for_moon_phase(moon_phase: float) -> str:
    moon_phase_index = math.floor(moon_phase * 8)
    
    return [
        "🌑",
        "🌒",
        "🌓", 
        "🌔",
        "🌕",
        "🌗",
        "🌘"
    ][moon_phase_index]
    
if __name__ == "__main__":
    julian_day = get_julian_day_number(current_day)
    current_phase = moon_phase_on_julian_day(julian_day)
    emoji = get_emoji_for_moon_phase(current_phase)

    print(emoji)