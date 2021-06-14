def generate_truelayer_auth_uri():
    TRUELAYER_BASE = 'https://auth.truelayer-sandbox.com'
    TRUELAYER_RESPONSE_TYPE = 'code'
    TRUELAYER_CLIENT_ID = 'sandbox-consequence-fd977d'
    TRUELAYER_SCOPE = 'info accounts balance cards transactions direct_debits standing_orders offline_access'
    TRUELAYER_REDIRECT_URI = 'http://localhost:8000/callback'
    TRUELAYER_PROVIDERS = 'uk-ob-all uk-oauth-all uk-cs-mock'
    # https://auth.truelayer-sandbox.com/?response_type=code&client_id=sandbox-consequence-fd977d&scope=info%20accounts%20balance%20cards%20transactions%20direct_debits%20standing_orders%20offline_access&redirect_uri=http://localhost:8000/callback&providers=uk-ob-all%20uk-oauth-all%20uk-cs-mock
    return f"{TRUELAYER_BASE}/?response_type={TRUELAYER_RESPONSE_TYPE}&client_id={TRUELAYER_CLIENT_ID}&scope={TRUELAYER_SCOPE}&redirect_uri={TRUELAYER_REDIRECT_URI}&providers={TRUELAYER_PROVIDERS}"
