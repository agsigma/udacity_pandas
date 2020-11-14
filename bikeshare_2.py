import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_ENUM = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12,
    'all': None
}

DAY_ENUM = {
    'monday': 0, 
    'tuesday': 1,
    'wednesday': 2, 
    'thursday': 3, 
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
    'all': None
}


def input_options(options):
  s = input().lower()
  while s not in options:
    s = input().lower()
  return s


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_options(CITY_DATA.keys())
    # get user input for month (all, january, february, ... , june)
    month = input_options(MONTH_ENUM.keys())
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_options(DAY_ENUM.keys())
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
    datetime_series = pd.to_datetime(df['Start Time'])
    df['Timestamp'] = datetime_series
    df['Month'] = df['Timestamp'].dt.month
    df['Day of week'] = df['Timestamp'].dt.dayofweek

    if month != 'all':
        df = df[df['Month'] == MONTH_ENUM[month]]

    if day != 'all':
        df = df[df['Day of week'] == DAY_ENUM[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    tmp_df = df
    tmp_df['Station combination'] = df['Start Station'] + ' - ' + df['End Station']

    # display most commonly used start station
    most_popular_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    most_popular_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    most_popular_route = df['Station combination'].mode()[0]

    print('Most popular start station: {}'.format(most_popular_start_station))
    print('Most popular end station: {}'.format(most_popular_end_station))
    print('Most popular route: {}'.format(most_popular_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = ('chicago', 'january', 'monday')  # get_filters()
        df = load_data(city, month, day)

        # print(df)        
        # print(df['Month'])        

        # time_stats(df)
        station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
