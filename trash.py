import urllib.request

def download_mp4(url, filename):
    urllib.request.urlretrieve(url, filename)

# Example usage
mp4_url = "https://www.playphrase.me/video/62a0f1180502e54f654c4d78/62a6341fd12c8718fb1d8fc3.mp4"
download_mp4(mp4_url, "video.mp4")
