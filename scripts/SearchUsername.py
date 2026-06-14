# Imports
import requests


class SearchUsername:
    def __init__(self , username:str ,  timeout:float=5) -> None:
        self.username = username
        self.timeout = timeout
        self.lookup()

    def lookup(self):
        # sanitize user input
        self.username = self.username.lstrip('/')


        platforms: list =  [
        {"name": "Instagram", "url": f"https://www.instagram.com/{self.username}"},
        {"name": "Twitter", "url": f"https://www.x.com/{self.username}/"},
        {"name": "Facebook", "url": f"https://www.facebook.com/{self.username}/"},
        {"name": "Youtube", "url": f"https://www.youtube.com/{self.username}/"},
        {"name": "Snapchat", "url": f"https://story.snapchat.com/@{self.username}/"},
        {"name": "Spotify", "url": f"https://open.spotify.com/user/{self.username}/"},
        {"name": "Pinterest", "url": f"https://www.pinterest.com/{self.username}/"},
        {"name": "Reddit", "url": f"https://www.reddit.com/{self.username}/"},
        {"name": "Tinder", "url": f"https://www.tinder.com/@{self.username}/"},
        {"name": "Github", "url": f"https://www.github.com/{self.username}/"},
        {"name": "Linkedin", "url": f"https://www.linkedin.com/{self.username}/"}
    ]

        for platform in platforms:
            name = platform["name"]
            url = platform["url"]

            try:
                result =  requests.get(url , timeout=self.timeout)

                match (result.status_code): # should be an 'int'
                    case 200:
                       print(f"[\033[32msuccess\033[0m] {name}: {url}")
                    case 301 | 302:
                        print(f"[\033[33mredirected\033[0m] {name}: {url}")

                    case _: # dont flood the user with unwanted results
                        pass

            except Exception as e:
                print(f"\033[31merror\030m: {e}")
