from datetime import datetime, timedelta

from typing import List, Optional, Tuple

from dataclasses import dataclass

from kandae.kandae import smallest_sum_subarr, smallestSubArrayLen


DEFAULT_SERVICE_BUFFER_MINUTES = 0
DEFAULT_SERVICE_WINDOW_LENGTH_MINUTES = 30


class GenerateServiceWindowException(Exception):
    def __init__(self, message, cause: Optional[Exception] = None):
        self._message = message
        self._cause = cause
        super(GenerateServiceWindowException, self).__init__()

    @property
    def message(self):
        return self._message

    @property
    def cause(self):
        return self._cause


@dataclass(frozen=True)
class ServiceWindow:
    start_time: int
    service_completion_time: int
    end_time: int


def find_open_windows(
        service_time: int,
        service_bay_start_times: List[int]
) -> List[ServiceWindow]:
    """Given a list of service windows for a bay, return all start times
    while could be used to occupy the service time.

    :param service_time: Total length of service time.
    :param service_bay_start_times: Sorted list of service bay start times, represented by an integer epoch value.
                                    e.g. A list containing [1718663400, 1718667000],
                                    which corresponds to [10:30, 11:30] implies that a service can be performed
                                    from `10:30 - 11:00`, and `11:30 - 12:00`. However, a service cannot be performed
                                    between `11:00 - 11:30`, since there is no `11:00` start time in the list.
    """
    smallest_subarray_meta: Tuple[int, int] = smallestSubArrayLen(
        target=service_time,
        nums=service_bay_start_times
    )
    start = smallest_subarray_meta[0]
    end = smallest_subarray_meta[1]
    if (start, end) == (-1, -1):
        raise GenerateServiceWindowException(
            message=f'No valid contiguous subarray found for service time: {service_time}'
        )

    windows = []
    for start_time in service_bay_start_times[start: end]:
        service_completion_time: int = int((datetime.utcfromtimestamp(start_time) + timedelta(minutes=service_time)).timestamp())
        window_end_time: int = int((datetime.utcfromtimestamp(service_completion_time) + timedelta(minutes=DEFAULT_SERVICE_BUFFER_MINUTES)).timestamp())
        windows.append(ServiceWindow(
            start_time=start_time,
            service_completion_time=service_completion_time,
            end_time=window_end_time
        ))

    return windows
