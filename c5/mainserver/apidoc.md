# Does that URL return JSON?
This API helps you answer that question! All you have to do is send a post request to the `json` API!

## Example
```shell
$ curl -XPOST target.livinginsyn.com:8083/json -d "url=https://api.ipify.org?format=json"
{
    "status": "success",
    "message": "That url returns JSON",
    "content": {
        "ip": "70.172.130.234"
    }
}
```

## Example (failure)
```shell
$ curl -XPOST localhost:8080/json -d "url=https://www.google.com"
{
    "status": "failure",
    "message": "That url doesnt return JSON"
}
```

## Notes:
All `url`'s passed to the API must be `http://` or `https://`