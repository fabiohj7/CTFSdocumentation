import instaloader


def posts(url):
    L = instaloader.Instaloader()

    try:
        print(f"Downloading from: {url}")
        post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
        L.download_post(post, target=post.owner_username)
        print("Download Completed")
    except Exception as e:
        print(f"An error has ocurred: {e}")


if __name__ == "__main__":
    posts("https://www.instagram.com/p/C8tFdRcNb9i/")
