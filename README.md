# ConnectPyse
ConnectWise (Manage) REST API client written in Python 3.x

ConnectWise RESTful API Client
------------------------------

Following the layout style of the official SDKs from CW team. Classes and their API counter part classes are under
their appropriate sections. Import the API class(es) you want to leverage and the model classes are imported with them.

## Setup
1. Update the your_api.json file with your API key details

## Usage
1. Import the sections you'll be using
2. Create an object from API Class
3. Leverage member methods to access features

### For example to get a Member's office phone number you would::

    >>> from connectpyse.system import members_api
    >>> members_api = MembersAPI()
    >>> a_member = members_api.get_member_by_id(123)
    >>> print(a_member.officePhone)
