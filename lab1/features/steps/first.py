from behave import *

use_step_matcher("re")

@given("I have two strings first and second")
def step_impl(context):
    context.first = 'Hello '
    context.second = 'World!'

@when("I concatenate two strings")
def step_impl(context):
    context.concat = context.first + context.second

@then("I print the result")
def step_impl(context):
    print("result is:",context.concat)