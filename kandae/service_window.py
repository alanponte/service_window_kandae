from typing import List

from dataclasses import dataclass

from kandae.kandae import smallest_sum_subarr


@dataclass(frozen=True)
class ServiceWindow:
    start_time: int
    service_completion_time: int
    end_time: int


def find_open_windows(
        service_time: int,
        service_bay_windows: List[ServiceWindow]
) -> List[int]:
    """Given a list of service windows for a bay, return all start times
    while could be used to occupy the service time."""
    smallest_subarray_meta = smallest_sum_subarr(arr=service_bay_windows)
    smallest_service_time = smallest_subarray_meta[0]
    start = smallest_subarray_meta[0]
    end = smallest_subarray_meta[1]
    # We can fit the service.
    if service_time > smallest_service_time:

    return [window.start_time for window in service_bay_windows[smallest_subarray_meta[0]: smallest_subarray_meta[1]]]
