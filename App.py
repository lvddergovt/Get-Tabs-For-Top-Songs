import requests
from bs4 import BeautifulSoup
import base64
import re  # Regular expressions module
import webbrowser
from urllib.parse import urlencode, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Spotify API credentials
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-top-read'
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'

def get_auth_code():
    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': SCOPE
    }
    url = f"{AUTH_URL}?{urlencode(params)}"
    webbrowser.open(url)

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.server.path = self.path

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.handle_request()
    query = parse_qs(httpd.path.split('?', 1)[-1])
    code = query.get('code')
    return code[0] if code else None

def get_access_token(code):
    auth_str = f'{CLIENT_ID}:{CLIENT_SECRET}'
    b64_auth_str = base64.urlsafe_b64encode(auth_str.encode()).decode()

    headers = {
        'Authorization': f'Basic {b64_auth_str}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None
    
def get_top_tracks(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get('https://api.spotify.com/v1/me/top/tracks?limit=15', headers=headers)
    if response.status_code == 200:
        return [(track['name'], track['artists'][0]['name']) for track in response.json()['items']]
    else:
        return []

def construct_base_ug_url(artist, song):
    artist_formatted = '-'.join(artist.lower().split())
    song_formatted = '-'.join(song.lower().split())
    return f"https://www.ultimate-guitar.com/search.php?search_type=title&value={artist_formatted}+{song_formatted}"

def find_exact_ug_url(base_url, song):
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Use regex to match the song URL pattern
        regex_pattern = re.compile(rf'href="(https://tabs.ultimate-guitar.com/tab/.+/{song.lower()}-[a-z]+-\d+)"')
        match = regex_pattern.search(str(soup))
        return match.group(1) if match else None
    return None

def check_url_exists(url):
    response = requests.head(url)
    return response.status_code == 200

# Main execution
if __name__ == "__main__":
    code = get_auth_code()
    if code:
        access_token = get_access_token(code)
        if access_token:
            top_tracks = get_top_tracks(access_token)
            for track, artist in top_tracks:
                url = construct_base_ug_url(artist, track)
                if check_url_exists(url):
                    webbrowser.open(url)
                    print(f"Opened tab for {track} by {artist}: {url}")
                else:
                    print(f"Tab not found for {track} by {artist}")
        else:
            print("Failed to obtain access token")
    else:
        print("Failed to obtain authorization code")