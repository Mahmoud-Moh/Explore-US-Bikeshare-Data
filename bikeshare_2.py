import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

daysofweek = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
months = ['January', 'February', 'March', 'April', 'May', 'June']
FILTER = ""
CITY = ""
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities = ['Chicago', 'New York', 'Washington']
    filters = ['month', 'day', 'both', 'none']
    choices_month = ['January', 'February', 'March', 'April', 'May', 'June'] + ['All']
    choices_day = daysofweek + ['all']
    day = city = month = ""
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in cities:
        print('Would you like to see data for Chicago, New York, or Washington?')
        city = input("").title()
    selected_filter = ""
    while selected_filter not in filters:
        print('Would you like to filter the data by month, day, both, or not at all? '
              'Type "none" for no time filter.')
        selected_filter = input("").casefold()

    # get user input for month (all, january, february, ... , june)
    if selected_filter == 'month' or selected_filter == 'both':
        while month not in choices_month:
            print('Which month? January, February, March, April, May, June, or all.')
            month = input("").title()
    if month=='All':
        month = 'all';
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if selected_filter == 'day' or selected_filter == 'both':
        while day not in choices_day:
            print("Which day? sunday, monday, tuesday...wednesday, or all.")
            day = input("").casefold()

    if selected_filter == 'none':
        month = 'all'
        day = 'all'
    if selected_filter == 'month':
        day = 'all'
    if selected_filter == 'day':
        month = 'all'
    print('-'*40)
    print("city: {}, month: {}, day: {}.".format(city, month, day))
    global FILTER
    global CITY
    FILTER = selected_filter
    CITY = city
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
    if city == 'Chicago':
        df = pd.read_csv(CITY_DATA['chicago'])
    elif city == 'New York':
        df = pd.read_csv(CITY_DATA['new york city'])
    elif city == 'Washington':
        df = pd.read_csv(CITY_DATA['washington'])
    if month != all or day != all:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day'] = df['Start Time'].dt.dayofweek
        if month != 'all':
            df = df[df['month'] == months.index(month)+1]
        if day != 'all':
            df = df[df['day'] == daysofweek.index(day)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    value_counts_month = df['month'].value_counts()
    count = value_counts_month.max()
    month = value_counts_month[value_counts_month == count].index[0]
    print("Most popular month:{}, count:{}, Filter:{}.".format(month, count, FILTER))

    # display the most common day of week
    value_counts_day = df['day'].value_counts()
    count = value_counts_day.max()
    day = value_counts_day[value_counts_day == count].index[0]
    print("Most popular day:{}, count:{}, Filter:{}.".format(daysofweek[day], count, FILTER))

    # display the most common start hour
    hours = df['Start Time'].dt.hour
    value_counts_hour = hours.value_counts()
    count = value_counts_hour.max()
    hour = value_counts_hour[value_counts_hour == count].index[0]
    print("Most popular hour:{}, count:{}, Filter:{}.".format(hour, count, FILTER))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    value_counts_sstation = df['Start Station'].value_counts()
    count = value_counts_sstation.max()
    sstation = value_counts_sstation[value_counts_sstation == count].index[0]
    print("Most popular Start Station:{}, count:{}, Filter:{}.".format(sstation, count, FILTER))

    # display most commonly used end station
    value_counts_estation = df['End Station'].value_counts()
    count = value_counts_estation.max()
    estation = value_counts_estation[value_counts_estation == count].index[0]
    print("Most popular Start Station:{}, count:{}, Filter:{}.".format(estation, count, FILTER))

    # display most frequent combination of start station and end station trip
    combination_series = df['Start Station'] + "   " + df['End Station']
    value_counts_combination = combination_series.value_counts()
    count = value_counts_combination.max()
    combination = value_counts_combination[value_counts_combination == count].index[0]
    print("Most popular Start Station:{}, count:{}, Filter:{}.".format(combination, count, FILTER))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Travel Time: {}.".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("Mean Travel Time: {}.".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of user types: {} \n".format(df['User Type'].value_counts()))
    if CITY != 'Washington':
        # Display counts of gender
        print("Count of user types: {} \n".format(df['Gender'].value_counts()))

        # Display earliest, most recent, and most common year of birth
        value_counts_birth = df['Birth Year'].value_counts()
        count = value_counts_birth.max()
        mostcommon = value_counts_birth[value_counts_birth == count].index[0]
        print("Earliest year of birth:{}\n"
              "Most recent year of birth:{}\n"
              "Most common year of birth:{}".format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(mostcommon)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def displayRawData(df):
    display = ""
    start = 0
    display = input("Do you want to display five rows of Raw Data? (yes/no): ")

    while display.capitalize() != "No":
        if display.capitalize() == 'Yes':
            print(df[start:start+5])
            start += 5
            display = input("Do you want to display another five rows of Raw Data? (yes/no): ")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        displayRawData(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
