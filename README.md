# falconlogger
Wrapper on Python's logger package for consistent use in my projects

## Installation

```
python -m pip install git+https://github.com/falconlogger.git
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| LOG_FORMAT | If present, specifies the format that log messages will take. Othewise a default is provided based on the presense or absence of STARTED_BY_SYSTEMD | Time, Name, Level, Message |
| LOG_LEVEL | One of the following values: DEBUG, INFO, WARNING, ERROR, CRITICAL | INFO |
| STARTED_BY_SYSTEMD | The presence of this environment variable triggers the use of a simpler log format string. | (no default) |

## Author

Thomas J. Daley, J.D. is an active, board-certified family law litigation attorney practicing primarily in Collin County, Texas, and software developer. My Texas-based family law practice is limited to divorce, child custody, child support, enforcment, and modification suits. [Web Site](www.thomasjdaley.com) * [Law Firm](www.koonsfuller.com/attorneys/tom-daley)