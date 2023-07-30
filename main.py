from booking.booking import Booking
import time
try:
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
        # print(len(bot.report_result()))
        bot.report_result()
        while True:
            pass

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise


