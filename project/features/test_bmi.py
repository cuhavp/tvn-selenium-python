from project.pages.bmi import BmiPage
import pytest

test_data = [
    ('32', 'male', '172', '60', 'BMI = 20.3 kg/m2   (Normal)')
]


@pytest.mark.parametrize("age,gender,height,weight,expected", test_data)
def test_body_mass_index_metric(browser, age, gender, height, weight, expected):
    bmi_page = BmiPage(browser)
    # on(BmiPage).
    # bmi_page.open('')
    bmi_page.select_metric_tab()
    bmi_page.fill_form(age, gender, height, weight)
    actual_result = bmi_page.get_result()
    assert actual_result == expected
