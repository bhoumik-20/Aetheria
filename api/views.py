from django.shortcuts import render
import requests

# Create your views here.

#.API Calls


#. YOUTUBE DATA API V3

#> Fetcing data from Youtube API

#.fetch_yt_data()

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
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")


#> Displaying data from Youtube API

#. yt_display()

def yt_display(request):
    yt_data=fetch_yt_data("<search_term>")
    
    videos = []
    
    for item in yt_data.get("items",[]):
        title = item["snippet"]["title"]
        thumbnail_url = item["snippet"]["thumbnails"]["medium"]["url"]
        videos.append({
            "title": title,
            "thumbnail": thumbnail_url,
            "video_url": f"https://www.youtube.com/watch?v={items['id']['videoId']}"
            })
        
    return render(request, "youtube_videos.html", {"videos": videos})




#. PEXELS API

#. Fetching data from Pexels API

#> fetch_pexels_data()

def fetch_pexels_data(search_term):

    base_url="https://api.pexels.com/v1/search?query="

    headers = {
        "Authorization":"amPic8yDXhAz1IhpxHWOGBw9dVcyYrV8C5FAntfX3NQcucIUB4DSHV2L"
    }
    params={
        "per_page":"4"
    }

    response = requests.get(base_url + search_term, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} ")

#. Displaying data from Pexels API

#> pexels_display()

def pexels_display(request):

    data = fetch_pexels_data("<search_term>")

    photos = []

    for item in data.get("photos",[]):
        title = f"By {item['photographer']}"
        image_url = item["src"]["small"]
        page_url = item["url"]
        photos.append({
            "title": title,
            "image_url": image_url,
            "page_url": page_url
        })

    return render(request, "pexels_photos.html", {"photos": photos})




#. UNSPLASH API

#. Fetching data from Unsplash API

#> fetch_unsplash_data()

def fetch_unsplash_data(search_term):
    base_url="https://api.unsplash.com/search/photos?client_id=bLUQHxVI-T-UOcKo4qOkh636GtioLEADHoFpP7gCtN8&query="

    params={
        "per_page":"4"
    }
    response = requests.get(base_url + search_term, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} ")

#. Displaying data from Unsplash API

#> unsplash_display()

def unsplash_display(request):

    data = fetch_unsplash_data("<search_term>")

    photos = []

    for item in data.get("results",[]):
        title = item["alt_description"]
        image_url = item["urls"]["thumb"]
        page_url = item["links"]["html"]
        photos.append({
            "title": title,
            "image_url": image_url,
            "page_url": page_url
        })

    return render(request, "unsplash_photos.html", {"photos": photos})


#. PIXABAY API

#. Fetching data from Pixabay API

#> fetch_pixabay_data()

def fetch_pixabay_data(search_term):
    base_url="https://pixabay.com/api/?key=52233955-a825ef619beefc18095887193&pretty=true&"

    response = requests.get(base_url + "q=" + search_term + "&per_page=4")

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error : {response.status_code}")

#. Displaying data from Pixabay API

#> pixabay_display()

def pixabay_display(request):
    data = fetch_pixabay_data("<search_term>")

    photos = []

    for item in data.get("hits",[]):
        title = item["tags"]
        image_url = item["previewURL"]
        page_url = item["pageURL"]
        photos.append({
            "title": title,
            "image_url": image_url,
            "page_url": page_url
        })

    return render(request, "pixabay_photos.html", {"photos": photos})


'''
a = input("\n\nEnter search term: ")
print("\n\n\nYoutube data api response")
fetch_yt_data(a)
print("\n\n\nPexels api response")
fetch_pexels(a)
print("\n\n\nUnsplash api response")
fetch_unsplash(a)
print("\n\n\nPixaby api response")
fetch_pixaby(a)
'''


