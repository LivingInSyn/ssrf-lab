# IconList API
The IconList API is located at: `target.livinginsyn.com:8082/iconlist`

## GET 
Return a list of available icons
```
$ curl target.livinginsyn.com:8082/iconlist
{"icons": ["/icons-png/Thinkbox-Deadline_4x.png", "/icons-png/Elastic-Container-Service_Container3_light-bg_4x.png", "/icons-png/Compute_4x.png", "/icons-png/Elastic-Container-Service_light-bg_4x.png",...]}
```

# Icon API

**Please chose a unique `user_id` while testing, there is _zero_ protection from clobbering someone elses test**

## Location
The Icon API is located at:
```
target.livinginsyn.com:8082/icon
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
The Put request takes a single argument `icon_path` which is a path returned by the `iconlist` API

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
$ curl -XPUT target.livinginsyn.com:8082/icon/foobar -d "icon_path=/icons-png/Thinkbox-Deadline_4x.png"
{"user_id": "foobar", "image": "iVBOR...SuQmCC=="}
```
