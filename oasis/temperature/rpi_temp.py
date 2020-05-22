import subprocess
import re


def check_cpu_temperature():
    raw_output = subprocess.check_output(
        ["/opt/vc/bin/vcgencmd", "measure_temp"]
    ).decode()
    output_matching = re.search("temp=([\d\.]+)'C", raw_output)
    return float(output_matching.group(1))
