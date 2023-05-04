from simple_spinner.spinner import Spinner
import time

if __name__ == '__main__':
    # use `start()` / `end()` method
    spinner = Spinner()
    spinner.start(desc='test')
    time.sleep(3)
    spinner.stop()
    
    # use `with` reserved word
    with Spinner(desc='test'):
        time.sleep(3)