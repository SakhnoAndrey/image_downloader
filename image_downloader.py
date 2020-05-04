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
):
    pattern = re.compile(
        "(?:http[s]?://)?(?:w{3}\.)?img.auctiva.com\S+(?:jpe?g|gif|png|bmp|svg)"
    )

    def _slash_trip(s: str):
        return s.lstrip("/").lstrip("//")

    def _create_folder(folder):
        access_rights = 0o755
        try:
            if not os.path.exists(os.path.abspath(folder)):
                os.makedirs(os.path.abspath(folder), access_rights)
        except OSError:
            print("Create directory %s failed" % os.path.abspath(folder))

    def _download_url_create_goal_files(file_name):
        source_file = open(os.path.join(source_folder, file_name), "r")
        goal_file = open(os.path.join(goal_folder, file_name), "w")
        # temp_file = open(os.path.join(goal_folder, "temp.txt"), "a")
        content_source = source_file.read()
        content_goal = content_source
        search = pattern.finditer(content_source)
        for match in reversed(list(search)):
            # temp_file.write(match.group(0) + "\n")
            url_file = match.group(0)
            content_goal = (
                content_goal[: match.start()]
                + content_goal[match.start() : match.end()].replace(
                    old_site_name, newsite_name
                )
                + content_goal[match.end() :]
            )
            download_folder = os.path.abspath(
                image_folder + "/" + os.path.dirname(urlparse(match.group(0)).path)
            )
            _create_folder(download_folder)

            content_url = requests.get(url_file)
            filename_url = os.path.join(
                download_folder, os.path.basename(urlparse(match.group(0)).path)
            )
            print(filename_url)
            f = open(filename_url, "wb")
            f.write(content_url.content)
            f.close()
        goal_file.write(content_goal)
        source_file.close()
        goal_file.close()
        # temp_file.close()

    source_folder = _slash_trip(source_folder)
    image_folder = _slash_trip(image_folder)
    goal_folder = _slash_trip(goal_folder)
    file_name = "ebay-new.html"

    _create_folder(goal_folder)
    _create_folder(image_folder)
    _download_url_create_goal_files(file_name)


images_downloader(
    source_folder="/data/1",
    goal_folder="/data/2",
    image_folder="/data/img/",
    old_site_name="img.auctiva.com",
    newsite_name="test.com",
)
