#! /usr/bin/env python
"""A module for authenticating against and communicating with selected
parts of the Lumo API.
"""
import logging
import requests
import re
import time
import pandas as pd
import datetime
import dateutil
import os
from bs4 import BeautifulSoup
from itertools import compress
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from functools import wraps

log = logging.getLogger(__name__)

# reduce logging noise from requests library
logging.getLogger("requests").setLevel(logging.ERROR)
LUMO_LOGIN_URL = 'https://my.lumobodytech.com/login'
"""The LUMO Login URL"""

def require_session(client_function):
    """Decorator that is used to annotate :class:`LumoClient`
    methods that need an authenticated session before being called.
    """
    @wraps(client_function)
    def check_session(*args, **kwargs):
        client_object = args[0]
        if not client_object.session:
            raise Exception("Attempt to use LumoClient without being connected. Call connect() before first use.'")
        return client_function(*args, **kwargs)
    return check_session

def list_activities(username_input, password_input):
    """Return dataframe of all lumo activities
    :returns: A dataframe of all lumo_activites and applicible meta_data.
    :rtype: tuples of (int, datetime)
    """

    LUMO_URL = "https://my.lumobodytech.com/login?next=%2Findex"

    alt_session = requests.Session()
    # Retrieve the CSRF token first
    r = alt_session.get(LUMO_URL)  # sets cookie
    soup = BeautifulSoup(r.content, 'lxml')
    csrftoken = soup.find('input', {'name': 'csrf_token'})['value']
    form_data = {
        "login": username_input,
        "password": password_input,
        'csrf_token': csrftoken,
        "embed": "false"
    }
    response = alt_session.post(LUMO_URL, data=form_data)
    if re.search('Invalid user or password', response.text):
        alt_session.close()
        raise Exception('Invalid username or password provided')
    else:
        run_data = alt_session.post('https://my.lumobodytech.com/my-runs').json()
        run_data = run_data['message']
        run_data = pd.DataFrame(run_data)
        run_data = run_data[run_data.delete_flag!=1]

        if run_data.shape[0]<1:
            log.warning('No Lumo Run sessions')
        else:
            utc = run_data.date_timestamp.values
            dates_utc = [datetime.datetime.utcfromtimestamp(element) for element in utc]
            dates_utc = [element.replace(tzinfo=dateutil.tz.tzutc()) for element in dates_utc]
            mask = [d > datetime.datetime(1970,1,1).replace(tzinfo=dateutil.tz.tzutc()) for d in dates_utc]
            dates_utc = list(compress(dates_utc, mask))
            run_data = run_data[mask]
            dates = [int(str(d.astimezone(dateutil.tz.tzlocal()).date()).replace("-", "")) for d in dates_utc]
            activity_ids = run_data.activity_id.values
            run_data_export = pd.DataFrame(
                {'run_date': dates, 'activity_id': activity_ids, 'bounce': run_data.bounce.values,
                 'breaking': run_data.braking.values, 'cadence': run_data.cadence.values,
                 'drop': run_data['drop'].values, 'gct': run_data.gct.values,
                 'rotation': run_data.rotation.values, 'tilt': run_data.tilt.values,
                 'total_time': run_data.total_time.values, 'rpe': run_data.rpe.values,
                 'description': run_data.description.values})
            alt_session.close()
            return (run_data_export)


def login(username, password, filedir):

    DRIVER_LOCATION = './chrome_driver/chromedriver.exe'
    options = chromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('--no-sandbox')
    prefs = {"download.default_directory": filedir}
    options.add_experimental_option("prefs", prefs)
    session = webdriver.Chrome(chrome_options=options, executable_path=DRIVER_LOCATION)

    session.get(LUMO_LOGIN_URL)

    login_field = session.find_element_by_id("login")
    login_field.clear()
    login_field.send_keys(username)
    pwd_field = session.find_element_by_id('password')
    pwd_field.clear()
    pwd_field.send_keys(password)

    sign_in_button = session.find_element_by_xpath("//input[@value='Sign in'][@type='submit']")
    sign_in_button.click()

    log.info('Logged in')

    if re.search('Invalid user or password', session.page_source):
        log.error("DISCONNECTING")
        disconnect(session)
        raise Exception('Invalid username or password provided')

    try:
        myElem = WebDriverWait(session, 5).until(EC.presence_of_element_located((By.ID, 'table-my-runs-body')))
        log.info("Page is ready!")
    except TimeoutException:
        log.error("Timeout on load...")

    return session



def download_session(username, password, activity_id, filedir, filename):
    session = login(username, password, filedir)
    ccs = "[data-activity_id = '" + str(activity_id) + "']"
    details_button = WebDriverWait(session, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ccs)))
    details_button.click()
    log.info('Downloading activty {}'.format(activity_id))
    get_csv = WebDriverWait(session, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-csv")))
    get_csv.click()

    if any(fname.endswith('.crdownload') for fname in os.listdir(filedir)):
        time.sleep(2)
    elif any(fname.endswith('.tmp') for fname in os.listdir(filedir)):
        time.sleep(2)
    else:
        log.info('Activity {0} complete!'.format(activity_id))

    if filename is not None:
        orig_filename = r'lumorun' + '_' + activity_id + '.csv'
        orig_filename = filedir+r'/'+orig_filename
        orig_filename = orig_filename
        new_filename = filedir+r'/'+filename

        os.rename(orig_filename, new_filename)

    disconnect(session)

def disconnect(session):
    if session:
        session.quit()
        log.info('Disconnected')







