# Spotify Top Tracks Tab Finder

This Python script allows you to find the Ultimate Guitar tabs for your top tracks on Spotify. It authenticates with the Spotify API to retrieve your top tracks and then searches for the corresponding tabs on the Ultimate Guitar website.

## Features

- **Spotify Authentication:** The script uses OAuth2 to authenticate with Spotify and retrieve your top tracks.
- **Top Tracks Retrieval:** Fetches your top 15 tracks from Spotify.
- **Ultimate Guitar Tab Search:** Searches for guitar tabs for each track on the Ultimate Guitar website.
- **Tab URL Validation:** Checks if the found URLs for tabs are valid and accessible.
- **Formatted Output:** Displays the artist, track, and URL for each found tab.

## Prerequisites

- Python 3.x
- Spotify Developer Account
- Ultimate Guitar account (optional)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/spotify-top-tracks-tab-finder.git
    cd spotify-top-tracks-tab-finder
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables:**

    Create a `.env` file in the root directory and add your Spotify API credentials:

    ```plaintext
    SPOTIFY_CLIENT_ID=your_spotify_client_id
    SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
    ```

## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **Authentication:**

    The script will open a browser window prompting you to log in to your Spotify account and authorize the app.

3. **Retrieving Top Tracks:**

    After successful authentication, the script will retrieve your top 15 tracks.

4. **Tab Search:**

    The script will search for the guitar tabs of your top tracks on Ultimate Guitar and display the results.

5. **Output:**

    The output will be a list of found tabs with the following format:

    ```
    Artist              Song                          URL
    ------------------------------------------------------------
    Artist Name         Track Name                    https://example.com/tab
    ```

## Example Output

```plaintext
3 tabs found.

Artist              Song                          URL
----------------------------------------------------------------------
The Beatles         Here Comes The Sun            https://tabs.ultimate-guitar.com/tab/the_beatles/here_comes_the_sun-123456
Led Zeppelin        Stairway to Heaven            https://tabs.ultimate-guitar.com/tab/led_zeppelin/stairway_to_heaven-123456
Pink Floyd          Wish You Were Here            https://tabs.ultimate-guitar.com/tab/pink_floyd/wish_you_were_here-123456
```

## Limitations

- Limited to Top 15 Tracks: Currently, the script only retrieves the top 15 tracks from your Spotify account.
- Accuracy of Tab Search: The script attempts to find the most accurate tab based on the track and artist name, but the results may not always be perfect.
- Environment Setup: Make sure to correctly set up your environment variables for the script to work.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.
