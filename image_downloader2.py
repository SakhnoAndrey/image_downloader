import os
import re
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup


# Create missing downloaded images and goal folders
def create_folder(folder):
    access_rights = 0o755
    try:
        if not os.path.exists(os.path.abspath(folder)):
            os.makedirs(os.path.abspath(folder), access_rights)
    except OSError:
        print("Create directory %s failed" % os.path.abspath(folder))


# Regular expressions to search for URLs
def compile_regex(list_extensions, old_site_name):
    pattern_protocol = r"(?:http[s]?://)?(?:w{3}\.)?"
    pattern_path = r"\S+\."
    pattern_ext = "(?:" + "|".join(list_extensions) + ")"
    return re.compile(
        r"{0}{1}{2}{3}".format(
            pattern_protocol, old_site_name, pattern_path, pattern_ext
        )
    )


class ImageDownloader:
    def __init__(self, source_folder, goal_folder, image_folder, new_site_name, old_site_name="img.auctiva.com",
                 list_ext=None):
        # Activating class variables
        self.source_folder = source_folder
        self.goal_folder = goal_folder
        self.image_folder = image_folder
        self.new_site_name = new_site_name
        self.old_site_name = old_site_name
        self.list_ext = ["jpg", "jpeg", "gif", "png", "bmp", "svg"] if list_ext is None else list_ext
        # Regular expressions to search for URLs
        self.pattern = compile_regex(self.list_ext, self.old_site_name)
        # Create missing downloaded images and goal folders
        create_folder(self.goal_folder)
        create_folder(self.image_folder)
        # Search and processing of all html resource files in the resource folder
        for name in os.listdir(self.source_folder):
            if os.path.isfile(os.path.abspath(os.path.join(self.source_folder, name))):
                # Opening / creating source and goal html files
                source_file = open(os.path.join(self.source_folder, name), "r")
                goal_file = open(os.path.join(self.goal_folder, name), "w")
                # Reading source html file
                self.content = source_file.read()
                # Parsing html file
                # Parse with using Regex
                # self.parse_and_download_images_by_regex()
                # Create BeautefulSoup object
                self.soup = BeautifulSoup(self.content, 'html.parser')
                # Parse and download images with using BeautefulSoup
                self.parse_and_download_images_bs4()
                # Save content from BeautefulSoup
                self.content = self.soup.prettify()
                # Saving and closing source and goal html files
                goal_file.write(self.content)
                source_file.close()
                goal_file.close()

    # Function download image from url
    def image_download_from_url(self, url_file):
        # Create missing folders for storing downloaded images
        download_folder = os.path.abspath(
            self.image_folder + "/" + os.path.dirname(urlparse(url_file).path)
        )
        create_folder(download_folder)
        # Download and save images by URL
        filename_url = os.path.join(
            download_folder, os.path.basename(urlparse(url_file).path)
        )
        content_url = requests.get(url_file)
        f = open(filename_url, "wb")
        f.write(content_url.content)
        f.close()
        # Output the file name of the downloaded image to the console. Can be deleted
        print(filename_url)

    # Parsing a separate source file with the search for the specified URLs,
    # downloading the corresponding images to the specified folder and
    # updating the URL in the goal html file. Parsing with using regular expressions
    def parse_and_download_images_by_regex(self):
        # Search all links with a given domain name for image files using regular expression
        search = self.pattern.finditer(self.content)
        # Processing found url images
        for match in reversed(list(search)):
            # Download founded file from url
            self.image_download_from_url(match.group(0))
            # Change URL addresses to reflect the new site domain in the content of the target html file
            self.content = (
                    self.content[: match.start()]
                    + self.content[match.start(): match.end()].replace(
                self.old_site_name, self.new_site_name
            )
                    + self.content[match.end():]
            )

    # Parsing, download and changed links of file with using BeautifulSoup
    def parse_and_download_images_bs4(self):
        # Handle tags img, download images from site and change links
        for image in self.soup.find_all('img'):
            if self.old_site_name in image['src']:
                self.image_download_from_url(image['src'])
                image['src'] = str(image['src']).replace(self.old_site_name, self.new_site_name)
                # Can be deleted
                print(image['src'])


# Initializing custom values for parsing
image_downloader = ImageDownloader(
    source_folder="data/1/",
    goal_folder="data/2/",
    image_folder="data/img",
    old_site_name="img.auctiva.com",
    new_site_name="test.com",
    list_ext=["jpg", "jpeg", "gif", "png", "bmp", "svg"],
)
