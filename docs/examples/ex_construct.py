import time
from pydantic import BaseModel

class Model(BaseModel):
    a: int
    b: str

# Validate the model at instantiation
m = Model(a=5, b="dog")
print(m)
try:
    Model(a=5, b=6)
except ValidationError as e:
    print(e)

# Instantiate the model without validation
c = Model.construct(a=5, b="dog")
print(c)
c = Model.construct(a=5, b=6)
print(c)
