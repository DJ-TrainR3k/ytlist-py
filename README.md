# ytlist-py
ytlist is a python script to get a YouTube user's playlists and save to a text file for use with Youtube-DL. This program is licensed under the GNU General Public License v3.0.



## To Run:


 * **You need a Youtube API key, you can get one [here](https://developers.google.com/youtube/v3/getting-started)**
**If you keep getting a 400 error when running, it probably means you didn't enter your API key**


Running the script is simple, all you need to do is run it with python3:

`python3 ytlist.py`


Once ran, it prompts for a YouTube channel ID (Channel IDs are 24 characters long beginning with UC) or a channel username. If playlists are found, the script saves them to a text file called `playlists.txt` with the following formatting:

>#Build Logs
>
>PL8mG-RkN2uTy5zBlQstuTnIUEQPe5rDHx

The first line contains the actual text name of the playlist below as a comment that will not interfere with Youtube-DL. Playlists with ASCII characters or emoji in them are supported. Below it is the aformentioned playlist's alphanumeric ID.

The way I intended this program to be used is in conjunction with the custom Youtube-DL commands that I've found after doing some previous research.


___

Below are the two commands I use when archiving channels.

`youtube-dl -ciw -o '%(playlist)s/%(playlist_index)s_%(title)s_%(id)s.%(ext)s' -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mkv" --yes-playlist --download-archive archive.txt -R 10000 -a playlists.txt`

This one downloads the best quality video and audio into the corresponding playlist folder and uses ffmpeg to merge them into an MKV file.

`youtube-dl -ciw --extract-audio --audio-format mp3 -o '%(playlist)s/%(playlist_index)s_%(title)s_%(id)s.%(ext)s' --download-archive archive.txt --yes-playlist --embed-thumbnail -R 10000 -a playlists.txt`

This one extracts the video audio, converts it to MP3, embeds the thumbnail of the video into the MP3 file and also puts the files into the orresponding playlist folders.
