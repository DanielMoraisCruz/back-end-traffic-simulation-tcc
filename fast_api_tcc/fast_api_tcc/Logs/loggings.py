from logging import (
    DEBUG,
    basicConfig,
    critical,
    debug,
    error,
    getLogger,
    info,
    warning,
)

asctime = '%(asctime)s'
name = '%(name)s'
levelname = '%(levelname)s'
message = '%(message)s'
line = '%(lineno)d'

basicConfig(
    level=DEBUG,
    filename='./fast_api_tcc/Logs/log.txt',
    filemode='a',
    encoding='utf-8',
    format=f'{asctime}\t{name}\t{line}\t{levelname}\t{message}',
)

logger = getLogger('fast_api_tcc')
logger.setLevel(DEBUG)

debug('Logging configured')
info('Logging configured')
warning('Logging configured')
error('Logging configured')
critical('Logging configured')
