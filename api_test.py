import requests
import json
from ast import literal_eval

class GeoTabUser(object):

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def database(self):
        return self.__database

    @property
    def credentials(self):
        return self.__credentials

    @credentials.setter
    def credentials(self, credentials):
        self.__credentials = credentials

    @username.setter
    def username(self, username):
        self.__username = username

    @password.setter
    def password(self, password):
        self.__password = password

    @database.setter
    def database(self, database):
        self.__database = database


    def __init__(self, username, password, database=None):
        self.__username = username
        self.__password = password
        self.__database = database
        self.__credentials = None

class GeoTabApi(object):
    @classmethod
    def request(Class,url,params=None):
        result = requests.get(url,params=params)
        return literal_eval(result.text)

class GeoTabSDK(object):
    def __init__(self, url):
        self.url = url

    def get_version(self):
        return GeoTabApi.request(self.make_url('GetVersion'))

    def authenticate(self, user):
        data = {'userName':user.username, 'password':user.password}
        result = GeoTabApi.request(self.make_url('Authenticate'), params=data)
        user.credentials= json.dumps(result['result']['credentials'])
        return result

    def get_road_max_speeds(self, user):
        data = {'credentials':user.credentials}
        return GeoTabApi.request(self.make_url('GetRoadMaxSpeeds'), params=data)

    def get_system_time_utc(self, user):
        data = {'credentials':user.credentials}
        return GeoTabApi.request(self.make_url('GetSystemTimeUtc'),params=data)

    def make_url(self, method_name):
        return self.url + GeoTabSDK.end_point() + method_name

    @classmethod
    def end_point(Class):
        return '/apiv1/'



if '__main__' == __name__:
    api = GeoTabSDK('https://my16.geotab.com')
    print(api.get_version())
    user = GeoTabUser(username='okuno.ryo.411@gmail.com',password='geotab2015');
    print(api.authenticate(user))
    print(api.get_road_max_speeds(user))
    print(api.get_system_time_utc(user))
