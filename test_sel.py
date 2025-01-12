from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path='C:\\Users\\USER PC\\aaa\\chromedriver.exe')

    driver.get('https://www.cricbuzz.com')



#@pytest.mark.dependency()
def test_sum(setup,driver):
    

    print(driver.title)
    yield
    driver.close
#@pytest.mark.dependency(depends=['test_sum','test_op6'])

def test_ope6(setup):
    assert 'cricbuzz'
