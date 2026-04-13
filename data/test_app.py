import ssl

# Bypass the Mac SSL certificate verification error
ssl._create_default_https_context = ssl._create_unverified_context

import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

from app import app

# ... (the rest of your test code stays exactly the same below)
def test_header_is_present(dash_duo):
    # Start the app in a testing environment
    dash_duo.start_server(app)
    
    # Wait for the H1 header to load and verify its text
    dash_duo.wait_for_element("h1", timeout=10)
    header_text = dash_duo.find_element("h1").text
    assert header_text == "Soul Foods: Pink Morsel Sales", "Header text does not match"

def test_visualization_is_present(dash_duo):
    dash_duo.start_server(app)
    
    # Wait for the graph container to load using its ID
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    
    # Assert that the element actually exists on the page
    assert dash_duo.find_element("#sales-line-chart") is not None, "Line chart is missing"

def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    
    # Wait for the radio buttons to load using their ID
    dash_duo.wait_for_element("#region-filter", timeout=10)
    
    # Assert that the region picker exists
    assert dash_duo.find_element("#region-filter") is not None, "Region picker is missing"