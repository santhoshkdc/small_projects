import datetime as dt
try:
    import pandas as pd
except ImportError:
    import pip
    pip.main(['install', '--user', 'pandas'])
    import pandas as pd


class Calender_Maker:

    """
    This class will return a calender for the input year and month.

    Attributes
        ----------
    None
        
    Methods
    ----------
    list_of_days()
        Return a list of all seven days of a week in English

    list_of_month()
        Return a list of all twelve months of a year in English

    get_month()
        returns a Pandas dataframe where each column in month name, day name,
        date and day number orderly, and each row corresponds to a date in the
        given year and month.
    
    print_calender()
        return a neatly formatted string that contains the calender for the input
        year and month.
    """

    year = 0
    month = 0
    def list_of_days():
        """The function will return a list of all seven days of a week in English

        Parametrs
        ---------
            None.
        """
        days = []
        for i in range(1,8):  #a loop to add all the days of a week to an empty list
            day = dt.datetime(1,1,i)
            days.append(day.strftime('%A'))
        return days

    def list_of_months():
        """
        The function will create a list of twelve months of a year in English

        Parametrs
        ---------
        None

        Returns:
        --------
            days: A list of strings, containg all the days of a week in English.
        """
        months = []
        for i in range(1,13):  #a loop to add all months of a year to an empty list
            month = dt.datetime(1,i,1)
            months.append(month.strftime('%B'))
        return months
        
    def get_dates():
        """Returns a pandas dataframe containing dates of the requested month and year.
            
        The function will prompt the user to input the values for the year and month
        for which the user needs to get a calender. If the input are valid, the function
        will continue to add values to a dictionary where the values of each key is a list
        that corresponds month_name, day of the week, date, and day number which is 0 for 
        sunday and 1 for mondays and so on. Besides the dates of the requested month, the
        function might also add a few dates from the month previous to the requested one and
        few dates from the month next to the requested one. This is to ensure that the calender
        is neatly formatted when printed. And fially, the dictionry will be transformed into a
        pandas dataframe thus making it easier to locate a specific value whenever necessary.

        """
        days = Calender_Maker.list_of_days()
        months = Calender_Maker.list_of_months()
        last_date = 0
        while True:  #loop to get a correct and valid year from the user
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


        while True:  #Loop to get a correct and valid month from the user.
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

        # the dictionary will be storing the necessary details such as dates of the 
        # user specified months and likely, also a few dates from adjacent months.
        # The dicionary can also contain info like day number such that 0 is for 
        # sunday and 1 is for sunday and so on.
        dates = {
            'Month':[],
            'Days':[],
            'Date':[],
            'Day_Number':[]
                }

        d = 1 #will be used as a flag to break the upcoming while loop
        while d <= 31: #loop to add values to various keys of the dates dictionary.
            try:
                a = dt.datetime(Calender_Maker.year,Calender_Maker.month,d)
                month,day,date,day_number = a.strftime('%B %A %d %w').split(' ')
                dates['Month'] += [month]
                dates['Days'] += [day]
                dates['Date'] += [date]
                dates['Day_Number'] += [day_number]
            except ValueError: # since different months have different number of dates.
                break
            d += 1

        flag = True #will be used as a flag to break the upcoming while loop
        a = dt.datetime(Calender_Maker.year,Calender_Maker.month,1)    
        while flag and a.strftime('%w') != '1':
            #a while loop to possibly insert dates from the previous month in order to nearly
            # print the final ouput            
            a -= dt.timedelta(days=1)    
            month,day,date,day_number = a.strftime('%B %A %d %w').split(' ')
            dates['Month'].insert(0,month)
            dates['Days'].insert(0,day)
            dates['Date'].insert(0,date)
            dates['Day_Number'].insert(0,day_number)
        else:
            flag = False
        
        if Calender_Maker.month == 12:
            a = dt.datetime(Calender_Maker.year + 1,1,1)
        else:
            a = dt.datetime(Calender_Maker.year,Calender_Maker.month + 1,1)
        
        flag = True
        while flag and a.strftime('%w') != '1':
            #a while loop to possibly append dates from th next month in order to nearly print
            #the final ouput
            month,day,date,day_number = a.strftime('%B %A %d %w').split(' ')
            dates['Month'].append(month)
            dates['Days'].append(day)
            dates['Date'].append(date)
            dates['Day_Number'].append(day_number)
            a += dt.timedelta(days=1)    
        else:
            flag = False
        
        Dates = pd.DataFrame(dates)
        return Dates
    
    def print_calender(self):
        """The calender will have a 7 cell by
        6 cell layout with each column corres
                Besides the dates on the requested
        month, the calender will also have """
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
        return grid