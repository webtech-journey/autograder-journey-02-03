def test_responsiveness():
    # Check if media queries are used in the CSS for responsiveness
    with open('styles.css', 'r',encoding="utf-8") as f:
        css_content = f.read()
        assert '@media' in css_content, "No media queries found for responsiveness."

def test_creative_design():
    # Check for any creative design elements (e.g., animations, hover effects)
    with open('styles.css', 'r',encoding="utf-8") as f:
        css_content = f.read()
        assert 'animation' in css_content or 'transition' in css_content, "No creative design elements found."
