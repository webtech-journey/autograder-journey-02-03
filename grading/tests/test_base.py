from bs4 import BeautifulSoup
import os

def test_html_file_present():
    assert os.path.exists('index.html'), "HTML file is missing!"

def test_css_file_present():
    assert os.path.exists('styles.css'), "CSS file is missing!"

def test_div_usage():
    with open('index.html', 'r') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        div_tags = soup.find_all('div')
        assert len(div_tags) > 0, "No <div> tag used in HTML!"

def test_ul_li_usage():
    with open('index.html', 'r') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        ul_tags = soup.find_all('ul')
        li_tags = soup.find_all('li')
        assert len(ul_tags) > 0, "No <ul> tag used in HTML!"
        assert len(li_tags) > 0, "No <li> tag used in HTML!"
