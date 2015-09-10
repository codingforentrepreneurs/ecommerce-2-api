## eCommerce 2 API Guide


### Create a RESTful API
A REST API is needed to Connect a Django project to other clients. We will be using the our pre-exsisting Django Project [eCommerce 2](https://github.com/codingforentrepreneurs/ecommerce-2) to build our REST API off of. 

Examples of other clients that might need your API:

- Native Mobile Applications: 
		- iOS
		- Andriod 
		- Windows Mobile
		- Phonegap (with a mix of a javascript framework)

- Desktop platforms:
		- Mac OS X
		- Windows
		- Linux

- Front-end (client side) Frameworks:
		- Angular.js
		- Ember.js
		- Backbone.js

- Whatever comes next

**Package Docs**: [Django Rest Framework](http://www.django-rest-framework.org/)
**Quick Installation**: 

- `pip install djangorestframework`

- Add `'rest_framework'` to `INSTALLED_APPS` in your Django Settings.

- Run `django-admin migrate`

[Installation Docs](http://www.django-rest-framework.org/#installation)

***

### Use JSON Web Tokens

JSON Web Tokens allow for Authentication in API-based requests. It allows authentication to be simple, secure, and in compliance.

**Installation**: `pip install djangorestframework-jwt` 

**Package Docs**: [Django REST framework JWT](http://getblimp.github.io/django-rest-framework-jwt/)

***


### Implement CORS for other Clients

Enabling CORS will allow your web application to connect to an external client or website. Learn more about [CORS on Wikipedia](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing).

**Package Docs**: [Django CORS headers](https://github.com/ottoyiu/django-cors-headers)
**Quick Installation**:

- `pip install django-cors-headers`

- Add `'corsheaders'` to `INSTALLED_APPS` in your Django settings

- Add/Update the following to your Django Settings:

```
MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
)
```
>  The `...` above represents other possible pre-existing MIDDLEWARE_CLASSES. You just need to ensure `'corsheaders.middleware.CorsMiddleware',` is above `'django.middleware.common.CommonMiddleware',`

```
CORS_ORIGIN_WHITELIST = (
        #'*', # for all domains; good for local testing.
        'yourdomain.com' for your domain
    )
```
> `CORS_ORIGIN_WHITELIST` is a list of origin hostnames that are authorized to make a cross-site HTTP request. 

Also consider adding:
```
CORS_URLS_REGEX = r'^/api/.*$' 
```
> The `CORS_URLS_REGEX` configuration setting is a regular expression that will enable the URL pattern that matches the one you set in combination to your `CORS_ORIGIN_WHITELIST` so, in this case, we have enable only `yourdomain.com/api/` for cross-origin requests.

Read more of many [configuration options here](https://github.com/ottoyiu/django-cors-headers#configuration) including `CORS_ALLOW_METHODS` for overriding the default HTTP methods allowed. 












