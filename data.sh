# mongoexport --uri="mongodb+srv://dev:cMWQKwzXoyNnUvCX@cluster0.pxlzcve.mongodb.net/report?retryWrites=true&w=majority"  -c=dailies -q='{ "park": {"$in": ["shdr", "usb"]} }' -o dailies.json
# mongoexport --uri="mongodb+srv://dev:cMWQKwzXoyNnUvCX@cluster0.pxlzcve.mongodb.net/report?retryWrites=true&w=majority"  -c=attractions -q='{ "park": {"$in": ["shdr", "usb"]} }' -o attractions.json

# mongoexport --uri="mongodb://localhost:27017/report"  -c=dailies -q='{ "park": {"$in": ["shdr", "usb"]} }' -o dailies.json
# mongoexport --uri="mongodb://localhost:27017/report"  -c=attractions -q='{ "park": {"$in": ["shdr", "usb"]} }' -o attractions.json

mongoexport --uri="mongodb://localhost:27017/report"  -c=dailies -q='{ "park": {"$in": ["shdr", "usb"]} }' -o dailies.json
mongoexport --uri="mongodb://localhost:27017/report"  -c=attractions -q='{ "park": {"$in": ["shdr", "usb"]} }' -o attractions.json