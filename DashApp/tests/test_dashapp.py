from dash import __version__, Dash

"""
    TO-DO:
    -Pytest works fine with the command 'poetry run pytest'
    -However, pytest cannot recognize the dashapp module,
     likely messed this up with the project structure, needs reviewing.
"""

import dashapp.app as app
import pytest

@pytest.fixture
def dash_duo(browser):
    with dash_duo.Duo(app=app, browser=browser) as duo:
        yield duo
        
def test_layout(dash_duo):
    header_text = dash_duo.find_element('.H1').text
    assert header_text == 'Flexibility Dispatches'
    
    data_table = dash_duo.find_element('table')
    assert data_table is not None

def test_histogram_update(dash_duo):
    pass