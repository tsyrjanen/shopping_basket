# At first PYTHONPATH should be correct.
export PYTHONPATH=../src:$PYTHONPATH

# You can run one test case, for example
# python -m unittest discover -p test_basket_functions.py
# or
# nosetests --nocapture test_basket_functions.py
# or
# nosetests --with-xunit --with-coverage --cover-branches --cover-inclusive --cover-erase --cover-xml --cover-html test_basket_functions.py

# Or run all test cases
export UNITTEST_CONFIG=$PWD"/config.py"
nosetests --with-xunit --with-coverage --cover-branches --cover-inclusive --cover-erase --cover-xml --cover-html $@
#or
#nosetests --nocapture  $@
#mystatus=$?
#exit $mystatus
