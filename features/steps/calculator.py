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

# calculate the correct tip amount is displayed in the results page

@When(u'I enter $50 as the total meal cost')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    meal_cost = br.find_element_by_name('meal_cost')
    meal_cost.send_keys('50')
    #assert meal_cost.text == '50'

@When(u'I enter 20% as the tip percentage')
def step_impl(context):
    br = context.browser
    tip_percentage = br.find_element_by_name('tip_percentage')
    tip_percentage.send_keys('20')
    #assert tip_percentage.text == '20'

@When(u'I submit the form')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('submit').click()

@Then(u'I should see $10 dollars as the tip in the results page')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('results')
    # assert that the amount 10 is displayed in results
    tip = br.find_element_by_id('tip_amount')
    assert tip.text in "10"



