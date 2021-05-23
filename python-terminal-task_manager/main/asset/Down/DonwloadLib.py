import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import os

def progress_bar(response,buffer_size,file_size,filename):
    progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            f.write(data)
            progress.update(len(data))

def download_file(link):
    if requests.get(link).status_code==200:
        buffer_size = 1024
        response = requests.get(link, stream=True)
        file_size = int(response.headers.get("Content-Length", 0))
        filename = link.split("/")[-1]
        progress_bar(response,buffer_size,file_size,filename)
        return "Success"
    else:
        return "[red]site not found "+"[/]"

                                            


                        
def js(url):
    if requests.get(url).status_code==200:
        session = requests.Session()
        # set the User-agent as a regular browser
        session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        html = session.get(url).content
        soup = bs(html, "html.parser")
        script_files = []
        for script in soup.find_all("script"):
            if script.attrs.get("src"):
                # if the tag has the attribute 'src'
                script_url = urljoin(url, script.attrs.get("src"))
                script_files.append(script_url)
        with open("javascript_files.txt", "w") as f:
            for element in script_files:
                f.write(element+"\n")
        return "Success"
    else:
        return "[red]site not found "+"[/]"


def css(url):
    if requests.get(url).status_code==200:
        session = requests.Session()
        # set the User-agent as a regular browser
        session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        html = session.get(url).content
        soup = bs(html, "html.parser")
        css_files = []
        for css in soup.find_all("link"):
            if css.attrs.get("href"):
                # if the link tag has the 'href' attribute
                css_url = urljoin(url, css.attrs.get("href"))
                css_files.append(css_url)
        with open("css.txt","w") as f:
            for element in css_files:
                f.write(element+"\n")
        return "Success"
    else:
        return "[red]site not found "+"[/]"
    


def image(url):
    if requests.get(url).status_code==200:
        def is_valid(url):
            parsed = urlparse(url)
            return bool(parsed.netloc) and bool(parsed.scheme)
        def get_all_images(url):
            """
            Returns all image URLs on a single `url`
            """
            soup = bs(requests.get(url).content, "html.parser")
            urls = []
            for img in tqdm(soup.find_all("img"), "Extracting images"):
                img_url = img.attrs.get("src")
                if not img_url:
                    # if img does not contain src attribute, just skip
                    continue
                # make the URL absolute by joining domain with the URL that is just extracted
                img_url = urljoin(url, img_url)
                # remove URLs like '/hsts-pixel.gif?c=3.2.5'
                try:
                    pos = img_url.index("?")
                    img_url = img_url[:pos]
                except ValueError:
                    pass
                # finally, if the url is valid
                if is_valid(img_url):
                    urls.append(img_url)
            return urls
        def download(url):
    
            response = requests.get(url, stream=True)

            # get the total file size
            file_size = int(response.headers.get("Content-Length", 0))

            # get the file name
            filename = os.path.join(os.getcwd(), url.split("/")[-1])
            print(filename)

            # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
            progress_bar(response,file_size,filename)
        imgs = get_all_images(url)
        for img in imgs:
            download(img)
        return "Success"

    else:
         return "[red]site not found "+"[/]"
