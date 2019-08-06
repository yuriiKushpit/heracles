def pytest_addoption(parser):
    # Add environment option for setting up url try command line
    parser.addoption("--environment", action="store", default="http://fedak.space:5000/")


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.environment
    if 'environment' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("environment", [option_value])