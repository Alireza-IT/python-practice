point = {"x": 1, "y": 2}
# or use dict fucntion like tuple () or list ()
point = dict(x=1, y=2)

print(point["x"])  # index is name of key

if "a" in point:
    print(point["x"])


print(point.get("a"))
print(point.get("a", 0))  # second argument is default value

del point["x"]
print(point)

# loop over dict

for key in point:
    print(key, point[key])
for x in point.item():
    print(x)
