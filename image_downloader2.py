import os
import re
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter
from chardet.universaldetector import UniversalDetector

# import lxml


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


# Additional function for task #1
def div_has_style_background_image(tag):
    return tag.name == "div" and tag.has_attr("style")


def next_tag_after_tag(current_tag, next_tag_name="label", tag_str=""):
    name_starting_tag = current_tag.name
    need_to_next = True
    while need_to_next:
        current_tag = current_tag.nextSibling
        if current_tag is None:
            need_to_next = False
        elif current_tag.name == name_starting_tag:
            current_tag = None
            need_to_next = False
        elif current_tag.name == next_tag_name:
            if tag_str == "":
                need_to_next = False
            else:
                if current_tag.string != tag_str:
                    current_tag = None
                    need_to_next = False
                else:
                    need_to_next = False
    return current_tag


# Beautiful Soup sorts the attributes. To turn this off, you can subclass the Formatter.attributes() method, which
# controls which attributes are output and in what order.
class UnsortedAttributes(HTMLFormatter):
    def attributes(self, tag):
        for k, v in tag.attrs.items():
            yield k, v


class ImageDownloader:
    def __init__(
        self,
        source_folder,
        goal_folder,
        image_folder,
        new_site_name,
        old_site_name="img.auctiva.com",
        list_ext=None,
    ):
        # Activating class variables
        self.source_folder = source_folder
        self.goal_folder = goal_folder
        self.image_folder = image_folder
        self.new_site_name = new_site_name
        self.old_site_name = old_site_name
        self.id = 1
        self.p_id = 1
        self.pic = 1
        self.pic_display_flex = 1
        self.margin_top = 0
        self.list_ext = (
            ["jpg", "jpeg", "gif", "png", "bmp", "svg"]
            if list_ext is None
            else list_ext
        )
        # Regular expressions to search for URLs
        self.pattern = compile_regex(self.list_ext, self.old_site_name)
        # Create missing downloaded images and goal folders
        create_folder(self.goal_folder)
        create_folder(self.image_folder)
        # Search and processing of all html resource files in the resource folder
        for name in os.listdir(self.source_folder):
            if os.path.isfile(os.path.abspath(os.path.join(self.source_folder, name))):
                # Opening / creating source and goal html files
                goal_file = open(os.path.join(self.goal_folder, name), "w")
                coding_detector = UniversalDetector()
                with open(os.path.join(self.source_folder, name), "rb") as source_file:
                    for line in source_file:
                        coding_detector.feed(line)
                        if coding_detector.done:
                            break
                    coding_detector.close()
                # print(coding_detector.result["encoding"])  # to delete
                source_file = open(
                    os.path.join(self.source_folder, name),
                    "r",
                    encoding=coding_detector.result["encoding"],
                )
                # Reading source html file
                self.content = source_file.read()
                # Change in html file before download images
                self.change_http_https()  # Task #4
                # Create BeautifulSoup object
                self.soup = BeautifulSoup(
                    self.content, "html.parser"
                )  # html.parser or lxml
                # STAGES #0
                self.background_img_to_result()  # Task #1
                self.shipping_policy()  # Task #2
                self.feedback_policy()  # Task #3
                self.replace_div_t_switch()  # Task #6
                self.replace_div_p_switch_1()  # Task #7-8
                self.replace_div_p_switch_2()  # Task #9-10
                self.replace_div_p_switch_3()  # Task #11-12
                self.replace_checkbox_label_img()  # Task #13
                self.replace_div_display_flex()  # Task #14-15 and 17
                self.div_our_store_section()  # Task #16
                self.div_payment_policy_section()  # Task #18
                self.div_shipping_policy()  # Task #18
                self.div_return_policy()  # Task #18
                self.div_feedback_policy()  # Task #18
                self.last_div_in_main()  # Task #18
                self.first_div_in_main()  # Task #19
                self.insert_tag_style()  # Task #20
                # STAGES #1
                # Parse and download images with using BeautifulSoup
                # self.parse_and_download_images_by_regex()  # STAGES #1
                # self.parse_and_download_images_bs4() # STAGES #1
                # Save content from BeautifulSoup
                self.content = self.soup.prettify(formatter=UnsortedAttributes())
                # Saving and closing source and goal html files
                goal_file.write(self.content)
                source_file.close()
                goal_file.close()

    # STAGES #1
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
                + self.content[match.start() : match.end()].replace(
                    self.old_site_name, self.new_site_name
                )
                + self.content[match.end() :]
            )

    # Parsing, download and changed links of file with using BeautifulSoup
    def parse_and_download_images_bs4(self):
        # Handle tags img, download images from site and change links
        for image in self.soup.find_all("img"):
            if self.old_site_name in image["src"]:
                self.image_download_from_url(image["src"])
                image["src"] = str(image["src"]).replace(
                    self.old_site_name, self.new_site_name
                )
                # Can be deleted
                print(image["src"])

    # STAGES #0

    # Task #1. Replace all similar cases
    def background_img_to_result(self):
        for tag_div in self.soup.find_all(div_has_style_background_image):
            if "background-image" in tag_div["style"]:
                tag_div["class"] = "img-result"
                tag_div["style"] = (
                    str(tag_div["style"]).replace(
                        "background-image:url", "background-image: url"
                    )
                    + ";"
                )

    def create_tag(self, el, name, txt, attrs=None):
        tag = self.soup.new_tag(name)
        if attrs:
            tag.attrs = attrs
        if txt != "":
            tag.string = txt
        el.append(tag)
        return tag

    # Task #2. Shipping policy
    def shipping_policy(self):
        elem = self.soup.find(name="section", attrs={"id": "content4"})
        if elem:
            elem.p.decompose()
            tag = self.create_tag(
                elem,
                "p",
                "We make every effort to process your orders quickly. Our standard "
                "shipping method is ",
            )
            self.create_tag(
                tag,
                "strong",
                "Registered Airmail requiring recipient’s signature "
                "upon the delivery.",
            )
            tag = self.create_tag(
                elem, "p", "All orders are usually dispatched within "
            )
            self.create_tag(tag, "strong", "1-2 business days.")
            tag = self.create_tag(
                elem,
                "p",
                "Once your order has been dispatched, an estimated delivery time "
                "will be subject to the delivery service but depending on location "
                "it is about ",
            )
            self.create_tag(tag, "strong", "14-20 business days.")
            self.create_tag(
                elem,
                "p",
                "Delivery times are estimates and commence from the date of shipping, rather "
                "than the date of order. Please note that the delivery of international orders "
                "may take longer than expected due to customs or other issues.",
            )
            self.create_tag(
                elem,
                "p",
                "Our shipping method comes with tracking and your tracking number will be "
                "provided once your order has been posted.",
            )
            tag = self.create_tag(
                elem,
                "p",
                "If you have any questions about the delivery and shipment or "
                "your order, please contact us at any time via ",
            )
            tag_p = tag
            tag = self.create_tag(tag, "strong", "")
            self.create_tag(
                tag,
                "a",
                "eBay contact form",
                {
                    "target": "_blank",
                    "href": "https://contact.ebay.com/ws/eBayISAPI.dll?FindAnswers&requested=lyapko_applicators",
                },
            )
            tag_p.append(".")

    # Task #3. Feedback policy
    def feedback_policy(self):
        elem = self.soup.find(name="section", attrs={"id": "content6"})
        if elem:
            for el in elem.find_all("p"):
                if "NEGATIVE FEEDBACK" in el.string:
                    el.string = (
                        "Please e-mail us before leaving negative feedback, or open any dispute on eBay. "
                        "We will do our best to solve the issue for you."
                    )

    # Task #4. Change http to https
    def change_http_https(self):
        self.content = self.content.replace("http:", "https:")

    # Task #6. Replace div - radio - t_switch
    def type_id_number(self, type_switch):
        number_id = self.id if type_switch == "t_switch" else self.p_id
        elem_id = ("" if type_switch == "t_switch" else "p_") + "id" + str(number_id)
        # print(elem_id)
        return elem_id

    def replace_div_input_label(self, name_switch="t_switch"):
        for tag_div in self.soup.find_all(name="div"):
            for tag_input in tag_div.find_all(
                name="input",
                attrs={"type": "radio", "name": name_switch, "checked": ""},
                recursive=False,
            ):
                checked = "checked" in tag_input.attrs
                tag_label = next_tag_after_tag(tag_input)
                tag_div.attrs = {
                    "class": ("" if name_switch == "t_switch" else "sub-") + "slider"
                }
                tag_input.attrs = {"type": "radio", "name": name_switch}
                if checked:
                    tag_input["checked"] = "checked"
                tag_label.attrs = (
                    {}
                    if name_switch != "t_switch"
                    else {
                        "class": "head-label",
                        "style": "margin-top: {0}px;".format(self.margin_top),
                    }
                )
                tag_input["id"] = tag_label["for"] = self.type_id_number(name_switch)
                if name_switch == "t_switch":
                    self.id += 1
                    self.margin_top += 140
                else:
                    self.p_id += 1

    def replace_div_t_switch(self):
        self.replace_div_input_label()

    # Task #7-8. Replace div - radio - p_switch_1
    def replace_div_p_switch_1(self):
        self.replace_div_input_label(name_switch="p_switch_1")

    # Task #9-10. Replace div - radio - p_switch_2
    def replace_div_p_switch_2(self):
        self.replace_div_input_label(name_switch="p_switch_2")

    # Task #11-12. Replace div - radio - p_switch_3
    def replace_div_p_switch_3(self):
        self.replace_div_input_label(name_switch="p_switch_3")

    # Task #13. Replace checkbox - label - image
    def replace_checkbox_label_img(self):
        for tag_input in self.soup.find_all(name="input", attrs={"type": "checkbox"}):
            tag_label = next_tag_after_tag(tag_input)
            if tag_label:
                tag_img_in_label = tag_label.find(name="img")
                if tag_img_in_label:
                    if tag_img_in_label["src"]:
                        name_pic = "pic-" + str(self.pic)
                        tag_input.attrs = {"type": "checkbox", "id": name_pic}
                        tag_label.attrs = {"for": name_pic, "class": "lightbox"}
                        self.pic += 1

    # Task #14. Replace display-flex
    def replace_div_display_flex(self):
        for tag_div in self.soup.find_all(name="div", attrs={"style": "display:flex"}):
            tag_div.attrs = {
                "style": "display: flex; flex-wrap: wrap; justify-content: center;"
            }
            self.replace_grid_item_link_gallery(tag_div_flex=tag_div)  # Task #15
            self.replace_div_class_link_store(tag_div_flex=tag_div)  # Task #17

    # Task #15. Replace grid-item link-gallery
    def replace_grid_item_link_gallery(self, tag_div_flex):
        for tag_label in tag_div_flex.find_all(name="label"):
            for tag_div in tag_label.find_all(name="div"):
                for _ in tag_div.find_all(name="p"):
                    pic_name = "pic_" + str(self.pic_display_flex)
                    tag_label.attrs = {"for": pic_name, "class": "grid-item"}
                    tag_div.attrs = {"class": "link-gallery"}

    # Task #16. Div-Div Our Store to Section
    def div_to_section(self, name_section="Our Store", num_section="2"):
        for tag_div in self.soup.find_all("div", text="", attrs={}, recursive=True):
            if tag_div.attrs == {} and len(tag_div.contents) == 0:
                tag_h2 = next_tag_after_tag(
                    tag_div, next_tag_name="h2", tag_str=name_section
                )
                if tag_h2 is not None:
                    tag_div.name = "section"
                    tag_div.attrs = {"id": "content" + num_section}
                    self.insert_tags_after_divdiv_to_section(tag_div)

    def insert_tags_after_divdiv_to_section(self, tag):
        current_tag = tag.nextSibling
        tag_div = self.create_tag(
            el=tag, name="div", txt="", attrs={"class": "block-title"}
        )
        tag.append(tag_div)
        while not (
            current_tag.name == "div"
            and current_tag.attrs == {}
            and len(current_tag.contents) == 0
        ):
            next_tag = current_tag.nextSibling
            extract_tag = current_tag.extract()
            tag.append(extract_tag)
            if next_tag is None:
                break
            else:
                current_tag = next_tag

    def div_our_store_section(self):
        self.div_to_section(name_section="Our Store", num_section="2")

    # Task #17. Replace class link-store
    def replace_div_class_link_store(self, tag_div_flex):
        for tag_div in tag_div_flex.find_all(name="div", recursive=False):
            for _ in tag_div.find_all(name="p", recursive=False):
                _ = self.id
                tag_div.attrs = {"class": "link-store"}

    # Task #18. Replace payment policy
    def div_payment_policy_section(self):
        self.div_to_section(name_section="Payment Policy", num_section="3")
        for tag_section in self.soup.find_all(name="section", attrs={"id": "content3"}):
            for tag_strong in tag_section.find_all(name="strong"):
                if (
                    tag_strong.contents[0].find("For PayPal payments please go to")
                    != -1
                ):
                    tag_strong.string = (
                        "For PayPal payments please go to www.PayPal.com"
                    )

    # Task #18. Replace shipping policy
    def div_shipping_policy(self):
        self.div_to_section(name_section="Shipping Policy", num_section="4")

    # Task #18. Replace return policy
    def div_return_policy(self):
        self.div_to_section(name_section="Return Policy", num_section="5")

    # Task #18. Replace feedback policy
    def div_feedback_policy(self):
        self.div_to_section(name_section="Feedback Policy", num_section="6")

    # Task #18. Last div in main tag
    def last_div_in_main(self):
        tag_html = self.soup.find(name="html")
        if tag_html:
            tag_html.unwrap()
        tag_main = self.soup.find(name="body")
        if tag_main:
            tag_main.name = "main"
            tags_div = tag_main.find_all("div", text="", attrs={}, recursive=False)
            tags_div[len(tags_div) - 1].attrs = {"class": "bgr-top"}

    # Task #19. First div in main tag
    def first_div_in_main(self):
        tag_main = self.soup.find(name="main")
        if tag_main:
            tags_div = tag_main.find_all("div", text="", attrs={}, recursive=False)
            tags_div[0].attrs = {"class": "bgr-top"}
            tags_div[1].attrs = {"id": "wrapper"}

    # Task #20. Add to the beginning of the file
    def insert_tag_style(self):
        style_file = open(os.path.join("templates", "style.html"), "r")
        style_content = style_file.read()
        new_style_bs = BeautifulSoup(
            style_content, "html.parser"
        )  # html.parser or lxml
        old_style = self.soup.find(name="style")
        if old_style:
            old_style.replace_with(new_style_bs)


# Initializing custom values for parsing
image_downloader = ImageDownloader(
    source_folder="data/1/",
    goal_folder="data/2/",
    image_folder="data/img",
    old_site_name="img.auctiva.com",
    new_site_name="test.com",
    list_ext=["jpg", "jpeg", "gif", "png", "bmp", "svg"],
)
