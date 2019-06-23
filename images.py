"""
Introduction:
    A script for scraping image thumbnails from the internet using the user's keyword.

Library and Tools:
    google_images_download module is a Selenium based tool for searching and downloading images from Google Images.

How to use?:
    1. To scrape images, run python images.py in the shell.
    2. Enter the keyword in the shell when the prompt appears.
    3. The images will be stored in a subfolder 'downloads' and it will contain another folder <keyword>.
"""

def crawler():
    from google_images_download import google_images_download

    #Getting the search query from the user using a prompt.
    keyword = input("Please enter the keyword. ")

    response = google_images_download.googleimagesdownload()

    # 'keywords' denotes the search query. 'limit' denotes the maximum number of images to be downloaded.
    arguments = {"keywords" : keyword, "limit" : 1, "print_urls" : True}
    try:
        paths = response.download(arguments)
        print(paths)
    except:
        print('Error: File Not Found.')

if __name__ == '__main__':
    crawler()

# Naren Akash, R J| Computer Science Undergrad
# International Institute of Information Technology, Hyderabad| IIIT Hyderabad




