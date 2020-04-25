# **class** _pygame_.**Rect**

pygame object for storing rectangular coordinates.

- `Rect(left, top, width, height) -> Rect`
- `Rect((left, top), (width, height)) -> Rect`
- `Rect(object) -> Rect`

Takes x, y coordinates of top left corner and width and height.
Takes two tuples (x, y) and (width, height), or takes another rect object/attribute.

>Pygame uses Rect objects to store and manipulate rectangular areas. A Rect can be created from a combination of left, top, width, and height values. Rects can also be created from python objects that are already a Rect or have an attribute named “rect”.

## Attributes:

- `x` -> left (x-coordinate)
- `y` -> top (y-coordinate)


- `top` -> top `(y-coordinate)`
- `left` -> left `(x-coordinate)`
- `bottom` -> bottom `(y + height)`
- `right` -> right `(x + width)`


- `topleft` -> `(left, top)`
- `bottomleft` -> `(left, bottom)`
- `topright` -> `(right, top)`
- `bottomright` -> `(right, bottom)`


- `midtop` -> `(centerx, top)`
- `midleft` -> `(left, centery)`
- `midbottom` -> `(centerx, bottom)`
- `midright` -> `(right, centery)`


- `center` -> `(centerx, centery)`
- `centerx` -> x-coordinate center of rectangle (x + (width / 2))
- `centery` -> y-coordinate center of rectangle (y + (height / 2))


- `size` -> `(width, height)`
- `width` -> horizontal length (on x-coordinate)
- `height` -> vertical length (on y-coordinate)


- `w` -> short for `width`
- `h` -> short for `height`

## Methods:

### `copy()`

copy the rectangle

`copy() -> Rect`

Returns a new rectangle having the same position and size as the original.

New in pygame 1.9

### `move()`

moves the rectangle

`move(x, y) -> Rect`

Returns a new rectangle that is moved by the given offset. The x and y arguments can be any integer value, positive or negative.

### `move_ip()`

moves the rectangle, in place.

`move_ip(x, y) -> None`

Same as the Rect.move() method, but operates in place.

### `inflate()`

grow or shrink the rectangle size

`inflate(x, y) -> Rect`

Returns a new rectangle with the size changed by the given offset. The rectangle remains centered around its current center. Negative values will shrink the rectangle.

### `inflate_ip()`

grow or shrink the rectangle size, in place

`inflate_ip(x, y) -> None`

Same as the Rect.inflate() method, but operates in place.

### `clamp()`

moves the rectangle inside another

`clamp(Rect) -> Rect`

Returns a new rectangle that is moved to be completely inside the argument Rect. If the rectangle is too large to fit inside, it is centered inside the argument Rect, but its size is not changed.

### `clamp_ip()`

moves the rectangle inside another, in place

`clamp_ip(Rect) -> None`

Same as the Rect.clamp() method, but operates in place.

### `clip()`

crops a rectangle inside another

`clip(Rect) -> Rect`

Returns a new rectangle that is cropped to be completely inside the argument Rect. If the two rectangles do not overlap to begin with, a Rect with 0 size is returned.

### `union()`

joins two rectangles into one

`union(Rect) -> Rect`

Returns a new rectangle that completely covers the area of the two provided rectangles. There may be area
inside the new Rect that is not covered by the originals.

### `union_ip()`
`
joins two rectangles into one, in place.

`union_ip(Rect) -> None`

Same as the Rect.union() method, but operates in place.

### `unionall()`

the union of many rectangles.

`unionall(Rect_sequence) -> Rect`

Returns the union of one rectangle with a sequence of many rectangles.

### ` unionall_ip()`

the union of many rectangles, in place.

`unionall_ip(Rect_sequence) -> None`

The same as the Rect.unionall() method, but operates in place.

### `fit()`

resize and move a rectangle with aspect ratio

`fit(Rect) -> Rect`

Returns a new rectangle that is moved and resized to fit another. The aspect ratio of the original Rect is preserved, so the new rectangle may be smaller than the target in either width or height.

### `normalize()`

correct negative sizes

`normalize() -> None`

This will flip the width or height of a rectangle if it has a negative size. The rectangle will remain in the same place, with only the sides swapped.

### `contains()`

test if one rectangle is inside another.

`contains(Rect) -> bool`

Returns true when the argument is completely inside the Rect.

### `collidepoint()`

test if a point is inside a rectangle.

- `collidepoint(x, y) -> bool`
- `collidepoint((x,y)) -> bool`

Returns true if the given point is inside the rectangle. A point along the right or bottom edge is not considered to be inside the rectangle.

### `colliderect()`

test if two rectangles overlap.

`colliderect(Rect) -> bool`

Returns true if any portion of either rectangle overlap (except the top+bottom or left+right edges).

### `collidelist()`

test if one rectangle in a list intersects.

`collidelist(list) -> index`

Test whether the rectangle collides with any in a sequence of rectangles. The index of the first collision found is returned. If no collisions are found an index of -1 is returned.

### `collidelistall()`

test if all rectangles in a list intersect

`collidelistall(list) -> indices`

Returns a list of all the indices that contain rectangles that collide with the Rect. If no intersecting rectangles are found, an empty list is returned.

### `collidedict()`

test if one rectangle in a dictionary intersects

`collidedict(dict) -> (key, value)`

Returns the key and value of the first dictionary value that collides with the Rect. If no collisions are found, None is returned.

>**Rect objects are not hashable and cannot be used as keys in a dictionary, only as values.**

### `collidedictall()`

test if all rectangles in a dictionary intersect.

`collidedictall(dict) -> [(key, value), ...]`

Returns a list of all the key and value pairs that intersect with the Rect. If no collisions are found an empty dictionary is returned.

>**Rect objects are not hashable and cannot be used as keys in a dictionary, only as values.**
