import time
import datetime
import speedtest


def timestamp():
    """
    :return: string timestamp: YYYY-MM-DD-hh-mm
    """
    t = time.localtime()
    d = datetime.datetime.now()

    return {'time_stamp_str': time.strftime('%Y-%m-%d_%H-%M-%S', t), 'datetime_object': d}


class TimeStampObject:
    def __init__(self):
        self.time = time.localtime()
        self.datetime_object = datetime.datetime.now()
        self.time_stamp_str = time.strftime('%Y-%m-%d_%H-%M-%S', self.time)


class DataPoint:
    def __init__(self, value):
        self.time_stamp_object = TimeStampObject()
        self.value = value


class UploadDataPoint(DataPoint):
    def __init__(self, value):
        super().__init__(value)


class DownloadDataPoint(DataPoint):
    def __init__(self, value):
        super().__init__(value)


class PingDataPoint(DataPoint):
    def __init__(self, value):
        super().__init__(value)


if __name__ == '__main__':
    upload_data_point_list = []
    download_data_point_list = []
    ping_data_point_list = []

    # ifconfig -> own data object
    # ip route list -> own data object
    # ip neigh -> own data object

    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    results_dict = s.results.dict()
