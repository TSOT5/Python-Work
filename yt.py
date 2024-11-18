import pytube

def progress_func(stream, chunk, bytes_remaining):
    # Calculate the percentage of the video that has been downloaded
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    # Update the progress bar
    print(f"Downloaded {percent:.2f}% of the video...", end="\r")

# Enter the URL of the YouTube video you want to download
url = input("Enter the YouTube video URL: ")

# Create a YouTube object with progress and completion callbacks
yt = pytube.YouTube(url, on_progress_callback=progress_func)

# Get the highest resolution video stream
video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()


# Download the video
print("Downloading...")
video_stream.download()
print("Video downloaded successfully!")
