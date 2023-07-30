from booking.booking import Booking
import time
with Booking() as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.select_place_to_go('New York')
    time.sleep(2)
    bot.select_date(check_in_date='2023-08-09',
                    check_out_date='2023-08-10')
    time.sleep(2)
    bot.select_adults(5)
    time.sleep(2)
    bot.click_search()
    time.sleep(2)
    bot.apply_filtrations()

while True:
    pass
