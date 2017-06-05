import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug('Use debug for detailed information, typically of interest only'
             'when diagnosing problems.')
logger.info('Use info for confirmation that things are working as expected.')
logger.warning('Use warining as an indication that something unexpected'
               'happened, or indicative of some problem in the near future'
               'The software is still working as expected.')
logger.error('Use error for more serious problems, when the software has not '
             'been able to perform some function.')
logger.critical('Use critical for a serious error, indicating that the program'
                'itself may be unable to continue running.')
