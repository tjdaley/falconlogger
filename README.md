# falconlogger
Wrapper on Python's logger package for consistent use in my projects

<p align="center">
    <a href="https://github.com/tjdaley/falconlogger/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/tjdaley/falconlogger"></a>
    <a href="https://github.com/tjdaleyfalconlogger/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/tjdaley/falconlogger"></a>
    <a href="https://github.com/tjdaley/falconlogger/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/tjdaley/falconlogger"><a>
    <img alt="Stage: Development" src="https://img.shields.io/badge/stage-Development-orange">
</p>
<p align="center">
    <a href="#purpose">Purpose</a> &bull;
    <a href="#installation">Installation</a> &bull;
    <a href="#author">Author</a>
</p>

## Purpose

The purpose of this package is to make it easy for me to use Python's ```logger``` package consistently in my projects. I want the message formats to be the same and for the same environment variables to have the same use for all my applications.

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

**NOTE**: Don't put the ```STARTED_BY_SYSTEMD``` variable in your .env file. Instead, add the following line to your systemd service file:

```
Environment=STARTED_BY_SYSTEMD=True
```

By doing it this way, the environment variable will only be detected when your application is being run under Systemd and will adjust the log format accordingly.

## Author

Thomas J. Daley, J.D. is an active, board-certified family law litigation attorney practicing primarily in Collin County, Texas, and software developer. My Texas-based family law practice is limited to divorce, child custody, child support, enforcment, and modification suits. [Web Site](www.thomasjdaley.com) * [Law Firm](www.koonsfuller.com/attorneys/tom-daley)