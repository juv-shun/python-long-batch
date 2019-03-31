import logging
import signal
import time
from typing import Callable, Optional

logger = logging.getLogger('long-batch')


class RunnerStatus():
    def __init__(self) -> None:
        # implement
        pass

    def is_finished(self) -> bool:
        # implement
        return False

    def update(self) -> None:
        # implement
        pass


class Runner():
    def __init__(self, status: Optional[RunnerStatus] = None) -> None:
        signal.signal(signal.SIGINT, self._signal_stop)
        signal.signal(signal.SIGTERM, self._signal_stop)
        self.stopped = False
        self.status = status

    def run(self, func: Callable[[Optional[RunnerStatus]], None], interval: int = 0) -> None:
        while not self.stopped:
            func(self.status)

            if self.status:
                if self.status.is_finished():
                    logger.info('all jobs finished')
                    self.stopped = True
                else:
                    self.status.update()

            if not self.stopped:
                time.sleep(interval)

        logger.info('Successfully stopped')

    def _signal_stop(self, signal, handler) -> None:
        logger.info('stop signal received.')
        self.stopped = True
