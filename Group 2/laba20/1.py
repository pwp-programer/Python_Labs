from urllib.parse import urlparse
value = urlparse("https://github.com/pwp-programer/Python_Labs")
print(value.hostname, value.netloc, value.query, value.username, value.encode, value.params, value.path)
