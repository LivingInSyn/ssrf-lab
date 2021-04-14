# The Target
The target is at:

target.livinginsyn.com:8082

## Icons Location
Valid icons can be found at: livinginsyn.com/icons-png

# The API
## GET Requests
target.livinginsyn.com:8082/icon/<string: user_id>

### Sample
```shell
➜  ~ curl target.livinginsyn.com:8082/icon/1
{"user_id": "1", "icon_path": "/icons-png/ad.png"}
```

## PUT Requests
target.livinginsyn.com:8082/icon/<string: user_id>

### Payload
The payload have an argument named `icon_path` which is a relative path to `target.livinginsyn.com:8082` and points at an image.

### Return Value
This API returns an object in the form:
```json
{
    "user_id": "<string>",
    "image": "<icon base64 encoded>"
}
```

### Example
```shell
➜  ~ curl -XPUT localhost/icon/1 -d "icon_path=/icons-png/ad.png"
{"user_id": "1", "image": "iVBORw0KGgoA...QmCC"}
```