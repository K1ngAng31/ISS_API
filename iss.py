# Python program that uses iss api to find the current people in the ISS
# and when the ISS will pass next depending on your state.


import requests as rq
import json
from datetime import datetime
import pandas as pd


def welcome():
    welcome = '''
    Welcome to data about the International Space Station,
    Here you will find the current people in the ISS.
    And you will be able to find when the ISS will pass depending on your state.


    =======================================================================


    This was done using APIs from the ISS.
    Simple, yet very informative.

    =======================================================================


    API --> Current people in ISS: http://api.open-notify.org/astros.json
    API --> Time that ISS will pass: http://api.open-notify.org/iss-pass.json

    =======================================================================

                    CURRENT PEOPLE IN SPACE

    '''
    print(welcome)

#=======================================================================

#this function will take in the response from requests (rfr) we made
def json_print(rfr):
    #lets format the string of our python json object
    rfr_text = json.dumps(rfr, sort_keys = True, indent = 4)
    #print the formatted the string
    return(rfr_text)


#Now lets get the current status of the people in the ISS
def current_people():
    response_astros = rq.get("http://api.open-notify.org/astros.json")
    #print(json_print(response_astros.json()))
    json_print(response_astros.json())

    people = response_astros.json()['people']
    # print(json_print(people))

    #get the craft name
    craft_name = []#store the craft name
    for i in people:
        craft_name.append(i['craft'])
    # print(craft_name)
    print("     Craft Name: ", craft_name[0])

    #get the people on the craft
    names = [] #store the name of the people
    for i in people:
        names.append(i['name'])
    # print(names)
    print("     Current People on board the", craft_name[0], ":")
    for i in range(len(names)):
        print("             ", names[i])

# print(df_states.head(2))
# print(df_states['state'])


#now lets find when the ISS will pass next depending on the state.
def iss_pass(user_state):

    #lets read in our csv file of states and their lats and long
    df_states = pd.read_csv('states.csv', usecols = ['state', 'lat', 'lon'])
    #get the index of the state
    row = df_states[df_states['state'] == user_state].index[0]

    #get the lat and lon
    parameters = {'lat':df_states.at[row,'lat'], 'lon':df_states.at[row,'lon']}

    #now lets read in our API
    response_iss_pass = rq.get('http://api.open-notify.org/iss-pass.json', params = parameters)
    json_print(response_iss_pass.json())#get the pass times

    #extract pass times
    pass_times = response_iss_pass.json()['response']#we use response because that is where the dates are stored
    # json_print(pass_times)

    # Now we create a for loop to extract the rise times values
    risetimes = []# this will store the values
    for i in pass_times:
        risetimes.append(i['risetime'])
    # print(risetimes)


    #From the output, we still can't tell what the times are
    #That is because it is in a format known as timestamp
    #to fix this we can use our python library datetime and convert it to
    #more comprehensible time

    from datetime import datetime as dt

    times = []#store our time values
    print("     The pass times for ", user_state, "are:\n")
    for i in risetimes:
        t = dt.fromtimestamp(i) #convert from time stamp to datetime
        print("     ",t) #print our time





if __name__ == '__main__':
    welcome()
    current_people()
    print("\n \n")
    print("     =======================================================================")
    print("\n")
    print("                    Passing times of the ISS")
    print("\n")
    x = input("     Which state would you like to see when ISS will pass? Please enter in abreviated form.\n       ")
    iss_pass(x)
