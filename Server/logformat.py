import logging
def formatlog():
    logging.basicConfig(filename='Server/log.log',filemode='w',format='%(name)s - %(levelname)s - %(message)s')
    return
