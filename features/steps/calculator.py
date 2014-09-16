# steps for the calculator form

@When(u'I go to the tip calculator page')
def step_impl(context):
    # get the homepage
    context.browser.get('http://localhost:5000')

@Then(u'I will see the calculator form')
def step_impl(context):
    assert context.browser.title == 'Tip Calculator'

@When(u'I submit the form with a valid total and tip percentage')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    meal_cost = br.find_element_by_name('meal_cost')
    meal_cost.send_keys('30')
    tip_percentage = br.find_element_by_name('tip_percentage')
    tip_percentage.send_keys('20')
    br.find_element_by_id('submit').click()

@Then(u'I should see the results page')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('results')


