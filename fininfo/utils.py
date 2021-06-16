import datetime
import json

from config.settings import TRUELAYER_AUTH_BASE, TRUELAYER_RESPONSE_TYPE, TRUELAYER_CLIENT_ID, TRUELAYER_SCOPE, \
    TRUELAYER_REDIRECT_URI, TRUELAYER_PROVIDERS, BASE_DIR


def generate_truelayer_auth_uri():
    # https://auth.truelayer-sandbox.com/?response_type=code&client_id=sandbox-consequence-fd977d&scope=info%20accounts%20balance%20cards%20transactions%20direct_debits%20standing_orders%20offline_access&redirect_uri=http://localhost:8000/callback&providers=uk-ob-all%20uk-oauth-all%20uk-cs-mock
    return f"{TRUELAYER_AUTH_BASE}/?response_type={TRUELAYER_RESPONSE_TYPE}&client_id={TRUELAYER_CLIENT_ID}&scope={TRUELAYER_SCOPE}&redirect_uri={TRUELAYER_REDIRECT_URI}&providers={TRUELAYER_PROVIDERS}"


def write_log(file_name, log_obj):
    log_file = open(BASE_DIR + f"/log/{file_name}.txt", "a")
    now = datetime.datetime.now()
    log_obj['time_now'] = now.strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(json.dumps(log_obj) + '\n')
    log_file.close()
