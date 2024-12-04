# Moesif Django with Datadata dd-trace, Example

Django is a web application framework that many developers use to serve APIs.

[Moesif](https://www.moesif.com) is an API analytics and monitoring platform. [moesifdjango](https://github.com/Moesif/moesifdjango)
is a middleware that makes integration with Moesif easy for Django based applications.

This is an example of django application with Moesif integrated. This example is based
on the quick start [tutorials of Django](https://docs.djangoproject.com/en/1.11/intro/) and [Django rest framework](http://www.django-rest-framework.org/#quickstart).

## Data Dog configuration

In this example. dd trace uses a console writer so that all the datadog captured data is printed to console. But feel free to modify. In `manage.py`:

```python
from ddtrace import patch_all, tracer
from custom_writer import ConsoleWriter

patch_all()
# Set the custom writer to log traces to the console for easier debugging
# but you can use any writer you want after verify writing to console works.
tracer.configure(writer=ConsoleWriter())

```


## Key files

moesifdjango's [github readme](https://github.com/Moesif/moesifdjango) already documented
the steps for setup Moesif Django. But here is the key file where the Moesif integration is added:

- `mysite/settings.py` added Moesif middleware related settings.

## How to run this example with WSGI

1. Setup [virtual env](https://docs.python.org/3.10/library/venv.html) if needed `python -m venv ENV`. Start the virtual env by `source ENV/bin/activate`

2. Install packages:
* `pip install -r requirements.txt`

3. Be sure to edit the `mysite/setting.py` to add your Moesif application id.

  ```python
  MOESIF_MIDDLEWARE = {
      'APPLICATION_ID': 'Your Moesif Collector Application Id',
  }
  ```

Your Moesif Collector Application Id can be found in the [_Moesif Portal_](https://www.moesif.com/).
After signing up for a Moesif account, your Moesif Application Id will be displayed during the onboarding steps.

You can always find your Moesif Collector Application Id at any time by logging
into the [_Moesif Portal_](https://www.moesif.com/), click on the bottom left user profile,
and then clicking _API Keys_.

4. Run the service:

```bash
python manage.py runserver
```

**Note** : If you get `OperationalError` with Exception Value: `no such table`, that means the schema has not been generated in database yet.

please run the following command line to resolve
```bash
python manage.py migrate
```

5. See `urls.py` for some urls that you can hit the server with
(e.g. `http://localhost:8000/api/todos`), and the data
should be captured in the corresponding Moesif account of the application id.

```bash
curl --request GET \
  --url http://127.0.0.1:8000/api/todos/ \
  --header 'User-Agent: insomnia/10.2.0'
```

```bash
curl --request POST \
  --url http://127.0.0.1:8000/api/todos/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.2.0' \
  --data ' {"title": "buy stuff", "description": "apples, oranges", "completed": false}'
```

