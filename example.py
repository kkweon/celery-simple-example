from tasks import add


# Basic example
res = add.delay(5, 5)
print(res.get())

# Same
res = add.apply_async((5, 5))
print(res.get())


# Subprocess
signature = add.s(5, 5)
res = signature.apply_async()
# res = signature.delay()
print(res.get())


# Callback Example
res = add.apply_async((2, 2), link=add.s(8))
print(res.get())

# Chaining
from celery import chain
chaining = chain(add.s(2, 2), add.s(4), add.s(8)) # 2 + 2 + 4 + 8
res = chaining.delay()
print(res.get())

chaining = add.s(2,2) | add.s(4) | add.s(8)
res = chaining.delay()
print(res.get())


# Grouping (Parallel)
from celery import group
grouping = group([add.s(i, i) for i in range(100)])
res = grouping.delay()
print(res.get())

# Chunks (when iter large)
jobs = add.chunks(zip(range(10000), range(10000)), 10)
res = jobs.apply_async()
print(res.get())

# Chord
# it's called after all of tasks are done
from celery import chord
#res = chord((add.s(i, i) for i in range(10)), xsum.s())()
#print(res.get())

