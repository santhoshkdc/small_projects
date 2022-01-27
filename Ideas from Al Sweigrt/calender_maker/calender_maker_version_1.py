import datetime as dt
import pandas as pd

class Calender_Maker:
    year = 0
    month = 0
    def list_of_days():
        days = []
        for i in range(1,8):
            day = dt.datetime(1,1,i)
            days.append(day.strftime('%A'))
        return days

    def list_of_months():
        months = []
        for i in range(1,13):
            month = dt.datetime(1,i,1)
            months.append(month.strftime('%B'))
        return months

    def get_dates():
        days = Calender_Maker.list_of_days()
        months = Calender_Maker.list_of_months()

        while True:
            print("What year do you want to look for?")
            response = input('> ')

            if not response.isdecimal:
                print("Incorrect format. Please entire a number greater than 0")
                continue
            year = int(response)
            if year > 0:
                Calender_Maker.year = year
                break

            print("Incorrect format. Please entire a number greater than 0")


        while True: # Loop to get a month from the user.
            print('Enter the month for the calendar, 1-12:')
            response = input('> ')

            if not response.isdecimal():
                print('Please enter a numeric month, like 3 for March.')
                continue

            month = int(response)
            if 1 <= month <= 12:
                Calender_Maker.month = month
                break

            print('Please enter a number from 1 to 12.')

        dates = {
            'Month':[],
            'Days':[],
            'Date':[],
            'Day_Number':[]
                }

        d = 1
        while d <= 31:
            try:
                a = dt.datetime(Calender_Maker.year,Calender_Maker.month,d)
                month,day,date,day_number = a.strftime('%B %A %d %w').split(' ')
                dates['Month'] += [month]
                dates['Days'] += [day]
                dates['Date'] += [date]
                dates['Day_Number'] += [day_number]
            except ValueError:
                pass
            d += 1

        flag = True
        a = dt.datetime(Calender_Maker.year,Calender_Maker.month,1)    
        while flag and a.strftime('%w') != '1':
            a -= dt.timedelta(days=1)    
            month,day,date,day_number = a.strftime('%B %A %d %w').split(' ')
            dates['Month'].insert(0,month)
            dates['Days'].insert(0,day)
            dates['Date'].insert(0,date)
            dates['Day_Number'].insert(0,day_number)
        else:
            flag = False
        Dates = pd.DataFrame(dates)
        return Dates
    
    def print_calender(self):
        Dates = Calender_Maker.get_dates()
        grid = ''
        week_seperator = ('+----------' * 7) + '+\n'
        day_seperator =  ('|          ' * 7) + '|\n'
        months = Calender_Maker.list_of_months()
        grid += ' ' * 34 + months[Calender_Maker.month -1] + ', ' + str(Calender_Maker.year) + ' ' * 34 +'\n'
        grid += '..' +"....".join(Calender_Maker.list_of_days()) +'..\n'
        length = len(Dates)
        idx = 0
        for j in range(5):
            grid += week_seperator
            date_row = ''
            for i in range(7):
                if idx < length:
                    day = str(Dates.iloc[idx,2]).rjust(2)
                else:
                    day = str(' ').rjust(2)
                date_row += '|' + day + (' '*8)
                idx += 1
            grid += date_row
            grid += '|\n' + (day_seperator * 4)
        grid += week_seperator
        print(grid)