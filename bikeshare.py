import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter city (chicago, new york city, washington): ').lower()
    while city not in CITY_DATA:
        print('Sorry, you chose the wrong city')
        city= input('Enter city (chicago, new york city, washington): ').lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6, 'All':0}
    month= input('Enter month from January to June or all: ')
    while month.title() not in months:
        print('Sorry, you entered the wrong input')
        month= input('Enter month from January to June or all: ')
    month = months[month.title()]
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = {'Sunday':1, 'Monday':2, 'Tuseday':3, 'Wednesday':4, 'Thursday':5, 'Friday':6, 'Saterday':7, 'All':0}
    day= input('Enter day from Monday to Sunday or All: ')
    while day.title() not in days:
        print('Sorry, you entered the wrong input')
        day= input('Enter day from Monday to Sunday or All: ')
    day= days[day.title()]
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    df['month']= df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.dayofweek
    
    if month != 0:
        df = df[df['month'] == month]
        
    if day != 0:
        df = df[df['day'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    print("The most common month is: " , df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('The most common day of the week is: ' , df['day'].mode()[0])

    # TO DO: display the most common start hour
    print('The most common start hour is: ' , (df['Start Time'].dt.hour).mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print( 'The most common start station used is: ',  df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station is: ' , df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most commonly used combination of start station and end station is: ', (df['Start Station'] + ", " + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: ' , df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The mean travel time is: ' , df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types is: ' , df['User Type'].value_counts())
    
    if 'Gender' in df:
        # TO DO: Display counts of gender
        print('counts of gender is: ' , df['Gender'].value_counts().to_frame())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is: ' , df['Birth Year'].min())
        print('The most recent year of birth is: ' , df['Birth Year'].max())
        print('The most common year of birth is: ' , df['Birth Year'].mode()[0])
    else:
        print("This data does not have Gender and Birth year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        df.head(5)
        data=input('Would you like to display five more lins of data? Enter yes or no')
        while data.lower() = 'yes' :
            df.head(5)
        data.lower() != 'yes' :
               break
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
