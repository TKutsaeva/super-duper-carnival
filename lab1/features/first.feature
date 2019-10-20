# -- FILE: features/first.feature
Feature: My first behave feature

  Scenario: Concat two strings
    Given I have two strings first and second
    When I concatenate two strings
    Then I print the result