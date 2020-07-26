import os

import logging

from retry import retry

from runner import Runner, RunnerStatus

INTERVAL: int = int(os.getenv('INTERVAL', 1))
LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
logger = logging.getLogger('long-batch', LOG_LEVEL)


@retry(tries=3, delay=5, backoff=2, logger=logger)
def execute(status: RunnerStatus) -> None:
    pass


if __name__ == '__main__':
    status = RunnerStatus()
    Runner(status).run(execute, INTERVAL)
