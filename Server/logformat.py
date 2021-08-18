import logging
def formatlog():
    logging.basicConfig(filename='Server/log.log',filemode='w',format='%(name)s - %(levelname)s - %(message)s')
    return

def logwarn():
    logging.error("Connection Error......")
    return
def logSuccess():
    logging.info('Connection Successful......')
    return

def succRet():
    logging.info("Post Request Successeded, 200 .....")

def failRet():
    logging.error('Post Request Failed......')