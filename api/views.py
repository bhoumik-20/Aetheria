from django.shortcuts import render
import requests

# Create your views here.

#.API Calls

#.YouTube Data API

def fetch_yt_data(search_term):
    base_url =  "https://www.googleapis.com/youtube/v3/search"

    parameters={
        "part": "snippet",
        "type": "video",
        "key": "AIzaSyAXaPi-UpCzSITfawdjj5mECUUjliQSiyw",
        "relevanceLanguage": "en",
        "q": search_term,
        "maxResults": 4
    }
    response = requests.get(base_url, params=parameters)
    print(response.json())


#. Pexels API
base_url="https://api.pexels.com/v1/search?query="

def fetch_pexels(search_term):

    base_url="https://api.pexels.com/v1/search?query="

    headers = {
        "Authorization":"amPic8yDXhAz1IhpxHWOGBw9dVcyYrV8C5FAntfX3NQcucIUB4DSHV2L"
    }
    params={
        "per_page":"4"
    }

    response = requests.get(base_url + search_term, headers=headers, params=params)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code} ")


#. Unsplash API

def fetch_unsplash(search_term):
    base_url="https://api.unsplash.com/search/photos?client_id=bLUQHxVI-T-UOcKo4qOkh636GtioLEADHoFpP7gCtN8&query="

    params={
        "per_page":"4"
    }
    response = requests.get(base_url + search_term, params=params)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code} ")

a = input("\n\nEnter search term: ")
print("\n\n\nYoutube data api response")
fetch_yt_data(a)
print("\n\n\nPexels api response")
fetch_pexels(a)
print("\n\n\nUnsplash api response")
fetch_unsplash(a)

