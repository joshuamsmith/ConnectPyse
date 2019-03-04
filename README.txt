# ConnectPyse
ConnectWise (Manage) REST API client written in Python 3.x
The original project was created by Joshua M. Smith.  This forked version was started by Mark Ciecior.

ConnectWise RESTful API Client
-----------------------

Following the layout style of the official SDKs from CW team. Classes and their API counter part classes are under
their appropriate sections. Import the API class(es) you want to leverage and the model classes are imported with them.

## Setup
1. Copy your_api.json to new my_api.json file and update with your API key details

## Usage
1. Import the sections you'll be using
2. Create an object from API Class
3. Leverage member methods to access features

### For example to get a Member's office phone number you would:

    >>> from connectpyse.system import members_api
    >>> m = members_api.MembersAPI()
    >>> a_member = m.get_member_by_id(123)
    >>> print(a_member.officePhone)
    
### For example to find the name of all activities related to a particular opportunity you would:

    >>> from connectpyse.sales import activity_api
    >>> myAct = activity_api.ActivityAPI()
    >>> myAct.conditions = 'opportunity/id=1250'
    >>> allActivities = myAct.get_activities()
    >>> for oneAct in allActivities:
    >>>   print(oneAct.name)
