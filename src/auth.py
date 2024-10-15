import logging
logging.getLogger().setLevel(logging.INFO)

import os
AUTH_KEY = os.getenv('AUTH_KEY')


def authorized(body):
    try:

        if not body.get('x-authorization'):
            logging.info(f"Unauthorized: No x-authorization key")
            return False
        
        if body.get('x-authorization') != AUTH_KEY:
            logging.info(f"Unauthorized: Invalid x-authorization key")
            return False
        
        return True


    except Exception as e:
        logging.error(f"Error in authorized: {e}")
        return False