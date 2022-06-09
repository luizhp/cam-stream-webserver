import logging


class util(object):

    @classmethod
    def get_logger(cls, logger_name, create_file=False):

        # create logger for prd_ci
        log = logging.getLogger(logger_name)
        log.setLevel(level=logging.INFO)

        # create formatter and add it to the handlers
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if create_file:
            # create file handler for logger.
            fh = logging.FileHandler('app.log')
            fh.setLevel(level=logging.DEBUG)
            fh.setFormatter(formatter)
        # reate console handler for logger.
        ch = logging.StreamHandler()
        ch.setLevel(level=logging.DEBUG)
        ch.setFormatter(formatter)

        # add handlers to logger.
        if create_file:
            log.addHandler(fh)

        log.addHandler(ch)
        return log
