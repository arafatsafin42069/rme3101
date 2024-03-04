import pywhatkit as kt
import random

def get_random_youtube_video():
    # List of example video IDs
    video_ids = ["video_id_1", "video_id_2", "video_id_3", "video_id_4"]  # Add more video IDs as needed

    # Choose a random video ID from the list
    random_video_id = random.choice(video_ids)

    # Construct the YouTube video URL
    video_url = f"https://www.youtube.com/watch?v={random_video_id}"

    return video_url

# Get a random YouTube video and play it
random_video_url = get_random_youtube_video()
kt.playonyt(random_video_url)
