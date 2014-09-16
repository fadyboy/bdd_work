# step for the google feature file

@when(u'I go to the home page')
def step_impl(context):
    context.browser.get('http://www.google.co.uk')

@then(u'I should see that the title is "Google"')
def step_impl(context):
    assert context.browser.title  == "Google"

