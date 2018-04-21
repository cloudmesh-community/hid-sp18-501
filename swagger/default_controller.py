import connexion
import six

from swagger_server.models.cpu import CPU  # noqa: E501
from swagger_server.models.disk import DISK  # noqa: E501
from swagger_server.models.memory import MEMORY  # noqa: E501
from swagger_server import util
import os, platform, subprocess, re, psutil

def get_cpu_info():
    platformdata = {
       "Architecture": platform.architecture(),
       "Machine TYpe": platform.machine(),
       "Processor Name": platform.processor(),
       "Name": platform.system(),
       "Values": platform.uname()
    }
    return (platformdata)

def get_disk_count_info():
    countdata = {
       "Read Count": disk_io_counters().read_count,
       "Write Count": disk_io_counters().write_count,
    }
    return (countdata)

def get_memory_info():
    memorydata = {
       "Active Memory": psutil.virtual_memory().active,
       "Inactive Memory": psutil.virtual_memory().inactive,
       "Cached Memory Used": psutil.virtual_memory().cached
    }
    return (memorydata)

def cpu_get():  # noqa: E501
    return get_cpu_info()


def disk_get():  # noqa: E501
    return get_disk_count_info()


def memory_get():  # noqa: E501
    return get_memory_info()

