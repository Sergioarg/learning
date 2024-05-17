# Q/A

## AWS

1. What is the purpose of an EC2 security group?

- Control incoming and outgoing network flows

<!-- Question 24 -->
24. What is the recommended way to grant to an EC2 machine a read-only access to a
specific file located in an S3 bucket?

- Create an IAM instance profile and use the predefined "AmazonS3ReadOnlyAccess" policy.

25. After you enabled billing access on your AWS account, how can you grant access te
billing data to specific IAM users or groups explicitely?

- You need to create and attach a Customer Managed Policy to the specific user or group

## React

12. What's the name of the objects that are used to send data payloads to redux stores
in order to update them?

- actions

27. For the AWS IAM policy displayed below, please select the appropriate condition and
resource that will allow a user to start/stop/reboot all instances in the Staging
Environment in the US N.Virginia region.

```bash
    Condition : "ec2:ResourceTag/Environment": "Staging"
    Resource : "arn:aws:ec2:us-east-1:123456789012:instance/*"
```

20. Reducers React

- Reducers should not be the place to make API calls.
- Reducers should be pure functions that take the previous state and an action, and return the next state.

?. What is the difference between a class component and a functional component in React?
- Child components are re-rendered when props change
- It is possible to define default props inside a child component
- Props are passed from parent component to child

## Django

16. Consider the following variable in `settings.py`:

```python
    CACHES = {
        "default": env.cache("DEFAULT_CACHE_URL"),
        "pipeline": env.cache("PIPELINE_CACHE_URL"),
    }
```
You created this statement in `utils.py`:

```python
from django.core.cache import caches
# Need to import the settings here ...
default = settings.CACHES.get("default")
    if default:
        cache.set("default_url", default)
pipeline = settings.CACHES.get("pipeline")
    if CACHES["pipeline"]:
        cache.set("pipeline_url", pipeline)
```

How can you import the `settings.CACHES` variable from `settings.py`?

```python
from django.conf import settings
```

17. Consider the following view:

```python
from django.http import HttpResponse

def index(request):
    output = "Welcome!"
```

How would you mark the output message as a translation string so that the system knows it can be translated?
```python
output = _("Welcome!")
```

18. In the following model, how to make the name field optional?

```python
from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

# Answer
# ------> Add blank = True to the field
```
Question:

19. Consider the following model: Answer

```python
Person.objects.filter(role='A')
Person.actors.all()
```

20. Consider the following models:

```python
class Actor():
    pass

class Movie():
    pass

# Answer
m1.actors.add(a1, a2)
```
21. Considering the following model:

Solution:

```python
def __repr__(self):
    return "<" + self.__class__.__name__ + ": " + self.name + ", " + self.folder + ">"
```

22. Considering the following model:

Answer:

```python
@property
@admin.display(ordering='full_name')
def full_name(self):
    return self.first_name + ' ' + self.last_name
```
