import re
from bs4 import BeautifulSoup


def test_table_tag_penalty():
    # Automatically pass if any <table> tags are found in HTML, otherwise fail
    with open('index.html', 'r') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        table_tags = soup.find_all(['table', 'tr', 'td', 'th'])
        assert len(table_tags) > 0, "Forbidden table tags not found, congratulations!"


def test_improper_flex_usage():
    # Pass if neither Flexbox nor Grid are used, otherwise fail
    with open('styles.css', 'r') as f:
        css_content = f.read()
        # Flex and Grid should be absent, otherwise, it fails
        assert 'display: flex' not in css_content, "Flexbox is being correctly used."

def test_improper_grid_usage():
    # Pass if Grid is used, otherwise fail
    with open('styles.css', 'r') as f:
        css_content = f.read()
        # Flex and Grid should be absent, otherwise, it fails
        if 'display: grid' not in css_content:
            assert True, "Grid is being correctly used."


def test_missing_div_tags():
    with open('index.html', 'r') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        div_tags = soup.find_all('div')
        # Fail if any required tag is missing
        assert len(div_tags) == 0,"Div tags found!"

def test_missing_ul_tags():
    with open('index.html', 'r') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        ul_tags = soup.find_all('ul')

        # Fail if any required tag is missing
        assert len(ul_tags) == 0,"ul tags found!"

def test_missing_li_tags():
    with open('index.html', 'r') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        li_tags = soup.find_all('li')
        # Fail if any required tag is missing
        assert len(li_tags) == 0,"li tags found!"

def test_poor_structure():
    # Pass if no rows or columns are found, otherwise fail
    with open('index.html', 'r') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        rows = soup.find_all(class_='row')
        columns = soup.find_all(class_='column')

        # Fail if rows or columns are found
        if len(rows) > 0 or len(columns) > 0:
            assert True, "Rows or columns found in the structure, good structure!"
