import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://scontent-bom1-1.xx.fbcdn.net"
                   "/v/t1.0-9/10152380_1438998506346425_"
                   "4680004882453098026_n.jpg?oh=c2ddeccd"
                   "98355ed4d81eb4d3ee89cc67&oe=59F04408")