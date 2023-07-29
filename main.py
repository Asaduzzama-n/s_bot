from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.select_place_to_go('New York')
    bot.select_date(check_in_date='2023-08-09',
                    check_out_date='2023-08-10')
    bot.select_adults(5)
    bot.click_search()
    bot.apply_filtrations()

while True:
    pass
