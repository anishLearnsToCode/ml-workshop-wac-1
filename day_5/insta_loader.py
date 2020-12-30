import instaloader

mod = instaloader.Instaloader()
username = input("enter Username ")
mod.download_profile(username, profile_pic_only=True, download_stories=False)
