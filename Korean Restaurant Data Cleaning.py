import pandas as pd
import numpy as np 

# Import Dataset
df = pd.read_excel('Korean Restaurant Dataset.xlsx')

# Initial Data Exploration
df.head(5)

df.columns.tolist()
'''
    ['Restaurant Name',
    'Rating',
    'Number Of Ratings',
    'Price Range',
    'Address',
    'Reviews']
'''

df.dtypes
'''
    Restaurant Name	object
    Rating	float64
    Number Of Ratings	object
    Price Range	object
    Price Range	object
    Reviews	object
'''

df.describe
'''
    count 151.0
    mean 4.507284768211921
    std	0.2366711749096467
    min	3.7
    25%	4.3
    50%	4.5
    75%	4.7
    max	5.0
'''

df.info
'''
Restaurant Name  Rating  \
    0                                          London Naru     4.7   
    1                    YORI Piccadilly Circus Korean BBQ     4.5   
    2    Bento Bab (Authentic Korea food) - Commercial ...     4.6   
    3                                           Seoul Food     4.7   
    4                                 Bento Bab Bishopgate     4.9   
    ..                                                 ...     ...   
    146                                           DOPI 도피소     4.8   
    147                                            WooJung     4.7   
    148                                             Daebak     4.6   
    149                                      Bibimbap Soho     4.3   
    150                                Korean Dinner Party     4.5   

        Number Of Ratings Price Range                          Address  \
    0               (315)      £20–30  Spread Eagle Yd, 3 Stockwell St   
    1              (5.3K)      £20–40                      6 Panton St   
    2              (1.7K)      £10–20                  4 Commercial St   
    3               (275)       £1–10                  17 Theobalds Rd   
    4               (110)      £10–20                      Bishopsgate   
    ..                ...         ...                              ...   
    146             (191)      £20–30               142 Bethnal Grn Rd   
    147            (1.6K)      £10–20                 73 New Oxford St   
    148            (1.2K)      £20–30            316-318 Kennington Ln   
    149            (2.1K)      £10–20                      11 Greek St   
    150            (1.7K)      £20–40             Top Floor, Kingly Ct   
    ...
    148     " quality food, nice and fast service,  vibe!"  
    149  "The flavour of their Bibimbap is incredible -...  
    150  "Delicious  fusion food - service was friendly...  

'''

df.shape
'''
    (151, 6)
'''

# Data Cleaning

# Dropping rows with null values 
df.dropna() 

# Converting object columns to string
df[['Restaurant Name', 'Address', 'Reviews']] = df[['Restaurant Name', 'Address', 'Reviews']].astype('string')
df.dtypes

# Changing values in 'Number Of Ratings' from object to int
df['Number Of Ratings'] = df['Number Of Ratings'].str.strip('()')

for ratings in df['Number Of Ratings']: 
    if 'K' in ratings: 
        # df.loc[df['Number Of Ratings'] == ratings, 'Number Of Ratings'] = ratings[0::2].strip('K') + '00' # Alternative method using strip
        df.loc[df['Number Of Ratings'] == ratings, 'Number Of Ratings'] = ratings[0:-1:2] + '00' # Uses just indexing
    continue 

df['Number Of Ratings'] = df['Number Of Ratings'].astype('int')

# Identifying Unique values in 'Price Range' column
df['Price Range'].unique().tolist()
'''
    ['£20–30',
    '£20–40',
    '£10–20',
    '£1–10',
    '£10–30',
    nan,
    '££',
    '£30–40',
    '⋅ Opens 6\u202fpm Wed', 
    '£100+',
    '£££',
    '11 Kensington High St']
    
    As we can see, the price ranges for all these restaurants are all over the place and require a fixed system. 
    A common pricing system uses '£' signs to determine how pricey a restaurant can be. 
    
    In our case, we can use £, ££, £££ to indicate the diferent price levels. 
    
    £ : 1-20 
    ££ : 21 - 50
    £££ : 51 and above 
    
    This system is easier to follow but less inidicative of the pricing for the restaurant
'''
 
# Changing the value with '⋅ Opens 6 pm Wed' to fit the system of £, ££, £££
df['Price Range' == '⋅ Opens 6 pm Wed'] = '£30-40'

# Changing the value with '11 Kensington High St' to fit the system of £, ££, £££
df['Price Range' == '11 Kensington High St'] = '£30-40'
'''
    Was able to identify price range by checking their menu online. 
'''

# Identifying rows with null data
null_data = df[df['Price Range'].isnull()]
print(null_data['Restaurant Name'].tolist())
'''
    ['Hanwoo Village - Authentic Korean BBQ', 
    'Keonbae Barbeque & Beer', 
    'Chungdam', 
    'Korean Grill Kensington', 
    'Horangee Pocha Korean BBQ Buffet', 
    'BAB N SUUL, Korean BBQ Restaurant', 
    'Sagye - Imperial Wharf', 
    'Iteaja', 
    'RedFarm', 
    'Korean Food', 
    'Jjang korean inspired food', 
    'Koko Grill Korean BBQ Restaurant', 
    'Miga', 
    'Jang Restaurant']
'''


df.head(50)
df.shape