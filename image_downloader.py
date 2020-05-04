import os
import re
import requests
from urllib.parse import urlparse


def images_downloader(
    source_folder,
    goal_folder,
    image_folder,
    newsite_name,
    old_site_name="img.auctiva.com",
    list_ext=None,
):
    if list_ext is None:
        list_ext = ["jpg", "jpeg", "gif", "png", "bmp", "svg"]

    # Truncate leading slashes before a folder name
    def _slash_truncate(s: str):
        return s.lstrip("/").lstrip("//")

    # Create missing downloaded images and goal folders
    def _create_folder(folder):
        access_rights = 0o755
        try:
            if not os.path.exists(os.path.abspath(folder)):
                os.makedirs(os.path.abspath(folder), access_rights)
        except OSError:
            print("Create directory %s failed" % os.path.abspath(folder))

    # Regular expressions to search for URLs
    def _compile_regex(list_extensions):
        pattern_protocol = r"(?:http[s]?://)?(?:w{3}\.)?"
        pattern_path = r"\S+\."
        pattern_ext = "(?:" + "|".join(list_extensions) + ")"
        return re.compile(
            r"{0}{1}{2}{3}".format(
                pattern_protocol, old_site_name, pattern_path, pattern_ext
            )
        )

    # Parsing a separate source file with the search for the specified URLs,
    # downloading the corresponding images to the specified folder and
    # updating the URL in the goal html file
    def _download_url_create_goal_files(file_name):
        # Opening / creating source and goal html files
        source_file = open(os.path.join(source_folder, file_name), "r")
        goal_file = open(os.path.join(goal_folder, file_name), "w")
        # Reading source html file
        content_source = source_file.read()
        content_goal = content_source
        # Search all links with a given domain name for image files using regular expression
        search = pattern.finditer(content_source)
        # Processing found url images
        for match in reversed(list(search)):
            # Change URL addresses to reflect the new site domain in the content of the target html file
            content_goal = (
                content_goal[: match.start()]
                + content_goal[match.start() : match.end()].replace(
                    old_site_name, newsite_name
                )
                + content_goal[match.end() :]
            )
            # Getting url link
            url_file = match.group(0)
            # Create missing folders for storing downloaded images
            download_folder = os.path.abspath(
                image_folder + "/" + os.path.dirname(urlparse(match.group(0)).path)
            )
            _create_folder(download_folder)
            # Download and save images by URL
            filename_url = os.path.join(
                download_folder, os.path.basename(urlparse(match.group(0)).path)
            )
            content_url = requests.get(url_file)
            f = open(filename_url, "wb")
            f.write(content_url.content)
            f.close()
            # Output the file name of the downloaded image to the console. Can be deleted
            print(filename_url)
        # Saving and closing source and goal html files
        goal_file.write(content_goal)
        source_file.close()
        goal_file.close()

    # Truncate leading slashes before a folder name
    source_folder = _slash_truncate(source_folder)
    image_folder = _slash_truncate(image_folder)
    goal_folder = _slash_truncate(goal_folder)
    # Regular expressions to search for URLs
    pattern = _compile_regex(list_ext)
    # Create missing downloaded images and goal folders
    _create_folder(goal_folder)
    _create_folder(image_folder)
    # Search and processing of all html resource files in the resource folder
    for name in os.listdir(source_folder):
        if os.path.isfile(os.path.abspath(os.path.join(source_folder, name))):
            _download_url_create_goal_files(name)


images_downloader(
    source_folder="/data/1",
    goal_folder="/data/2",
    image_folder="/data/img/",
    old_site_name="img.auctiva.com",
    newsite_name="test.com",
    list_ext=["jpg", "jpeg", "gif", "png", "bmp", "svg"],
)
