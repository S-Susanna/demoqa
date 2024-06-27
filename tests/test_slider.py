from pages.slider import Slider


def test_slider(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slider1.exist()
    assert slider.inp.exist()

    while not slider.inp.get_dom_attribute('value') == '50':
        slider.slider1.send_keys(Keys.ARROW_RIGHT)

        assert slider.inp.get_dom_attribute('value') == '50'