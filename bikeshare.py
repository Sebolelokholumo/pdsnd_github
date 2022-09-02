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

    #  get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['washington', 'chicago', 'new york city']
    city = input('choose one of three cities, chicago, new york or washington:').casefold()
    while city not in cities:
        print('sorry! it seems like the city you entered is not among three cities provided')
        city = input('choose one of three cities, chicago, new york or washington:').casefold()
        continue
    else:
        print('You have chosen:', city)






    # get user input for month (all, january, february, ... , june)
    month = input('Enter any one of the first 6 months:').casefold()
    print('month is:', month)



    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('enter day of week:').casefold()
    print('day of week is:', day)

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = df['Start Time'].apply(pd.to_datetime)


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
 # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

    df = load_data('chicago', 'march', 'friday')



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # extract month from Start Time to create new column
    df['month'] = df['Start Time'].dt.month

    # extract day of week from Start Time to create new column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The  most common month is:', most_common_month)

    # convert the Start Time column to datetime
    df['Start Time'] = df['Start Time'].apply(pd.to_datetime)

    # display the most common day of week
    most_common_day_week = df['day_of_week'].mode()[0]
    print(most_common_day_week, 'is the most common day of the week')


    #  display the most common start hour

    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is:', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', commonly_used_start_station)

    # display most commonly used end station

    commonly_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', commonly_used_end_station)





    #  display most frequent combination of start station and end station trip

    frequent_start_end_station = df[['Start Station','End Station']].mode().loc(0)
    print("The most commonly used start station and end station : {}, {}"\
            .format(frequent_start_end_station[0], frequent_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time is:', total_travel_time, 'seconds')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()



    #  Display counts of user types
    user_types = df.groupby(['User Type']).count()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df.groupby(['Gender']).count()
        print(gender)

    #  Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('the earliest birth year is:', earliest_birth_year)

    if 'Birth Year' in df.columns:
        most_recent_year = df['Birth Year'].max()
        print('the most recent year is:', most_recent_year)

    if 'Birth Year' in df.columns:
        most_common_year = df['Birth Year'].mode()[0]
        print('the most common year is:', most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ displays bikeshare data."""

    print('\nGetting 5 rows data...\n')

    #get user input
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input('do you wish to continue?:').lower()
        if view_data == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
