<img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Twelve_Labours_Altemps_Inv8642.jpg" height="300px"/>

# Simple solution it's the best solution!

My application has 2 main modules:

1) server
    Done on flask. This is simple validation server which allow to enter your data.
    By click Submit button you can validate your data and format related to task.
    Server has error message if you enter incorrect data like (letters, spaces, symbols etc)

2) automation framework
    Automation framework has few layours:
        1) Driver initialization
            I've make this layour very simple - just initialize browser in test module.
            Usually for corporate application I use next architecture:

            DriverHandler class - this class responsible on creating driver instance. By static factory pattern
            I decide how to create instance. Browser/device type I'm passing by command lines or by parameters in testing framework.
            All the same functionality is located in Driver class which os parent class of ChromeDriver and FirefoxDriver(for exmple).
            If we have some different behavior for different browser we overriding methods in their classes.

            Page structure - usually I create some BasePage where I initialize all needed methods as (click, swipe, sendkeys etc)
            In this application BasePage is Element class. All another classes are extends from this class and can use parent class methods.

            Simple page has four secrion:
                a) locators (in case of Java I'm using @FindBy, @FindAll, @FindBys annotations to initialize elements.
                b) getters for each locator.
                c) functional logic - all logic which we can do with elements on current page.
                d) business logic - logic which leads to next page.

            We can have some different scenarion on Chrome or Firefox. I'm using reflection approach to handle this problem.
            Simple create method in utils package that have module and function name parameters.
            In page code I just have something like this

            basic_method():
                call_method_from_util()


            basic_method_firefox()
                firefox_implementation_code

            basic_method_chrome()
                            chrome_implementation_code

             This approach allows me easy and simple handle different behaviors in different browsers.



## How to start application

**NOTE: Please run all comands from /heracles folder**

All code is deployed to http://fedak.space:5000/ you can use this endpoint to test application.
Simple install all requirement packages

```python
pip3 install requirements.txt
```

Download chrome and chromedriver from https://chromedriver.storage.googleapis.com/index.html related to your version of Chrome.
Pass chrome driver in the root of project.

And run
```shell
python3 -m pytest --capture=no test_money_formatter/
```

You can setup server in your local machine
Download the project

Run
```python
python3 money_formatting.py
```

Your server should start on http://localhost:5000/

And run
```shell
python3 -m pytest --capture=no test_money_formatter/ --environment=http://localhost:5000/
```

--environment parameter it's base url by default base url is http://fedak.space:5000/


## Our evaluation criteria:

- Q: How did your structure your code? (*eg: is it structured in a testable way?*)
- A: The code is easy to maintain and easy to test. Testing framework is easy to grow as a corporate framework.
- Q: What did you test? (*eg: functionality, performance, etc.*) at which level? (*eg: unit, integration, UI, etc.*)
- A: I've tested just functionality. Unit testing it's developers area. I'm powerfull in web, mobile and api testing (all ways of testing for 98% applications).
- Q: Which testing technique did you use? why?
- A: Boundary value and Equivalence partitioning - the best technique for this task.
- Q: We also care a little about the functionality itself.
- A: Functionality is a little bit pass acceptance criteria for testing task.
