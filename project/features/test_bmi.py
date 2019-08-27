from project.pages.bmi import BmiPage


def test_body_mass_index_metric(browser):
    bmi_page = BmiPage(browser)
    # bmi_page.open('')
    bmi_page.select_metric_tab()
    bmi_page.fill_form('32', 'male', '172', '60')
    actual_result = bmi_page.get_result()
    assert actual_result == 'BMI = 20.3 kg/m2   (Normal)'
