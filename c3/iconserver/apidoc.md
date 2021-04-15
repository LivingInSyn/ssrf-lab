# Icon API

**Please chose a unique `user_id` while testing, there is _no_ protection from clobbering someone elses test**

## Location
The Icon Api is located at:
```
target.livinginsyn.com:8082/icon
```

## Icon Path
Paths used in `PUT` requests should be relative to `livinginsyn.com`. Icons can be found at: 
```
livinginsyn.com/icons-png
```

## GET
GET requests take the form:
```
target.livinginsyn.com:8082/icon/<user_id: string>
```
### Return Value
```json
{
    "user_id": "<user_id>", 
    "icon_path": "<icon path>"
}
```

### Example
```shell
$ curl target.livinginsyn.com:8082/icon/foobar
{"user_id": "foobar", "icon_path": "/icons-png/ad.png"}
```
## PUT
PUT requests `upserts` a new user ID. Requests take the form:
```
target.livinginsyn.com:8082/icon/<user_id: string>
```

### Request Arguments
The Put request takes a single argument `icon_path` which is a path relative to `livinginsyn.com`

### Return Value
This API returns the user_id and the contents of the file at `icon_path` base64 encoded
```json
{
    "user_id": "<string>",
    "image": "<icon base64 encoded>"
}
```

### Example
```shell
$ curl -XPUT target.livinginsyn.com:8082/icon/foobar -d "icon_path=/icons-png/ad.png"
{"user_id": "foobar", "image": "iVBOR...SuQmCC=="}
```
