from ..models import User
from rest_framework import status


def userProfile(data):
    pid = data.get('uid')
    user_profile_object = User.objects.filter(uid=pid).first()
    result = {}
    if user_profile_object:
        result['name'] = user_profile_object.name
        result['address'] = user_profile_object.address
        result['phone'] = user_profile_object.phone
        result['email'] = user_profile_object.email
        result['result'] = 'SUCCESS'
        result['status'] = status.HTTP_200_OK
    else:
        result = {'result': 'USER_NOT_FOUND', 'status': status.HTTP_400_BAD_REQUEST}
    return result


def update_user_profile(user_uid, name, phone, address):
    user_obj = User.objects.filter(uid=user_uid).first()
    if user_obj:
        user_obj.name = name
        user_obj.phone = phone
        user_obj.address = address
        user_obj.save()
        result = {"result": "USER_DATA_SUCCESSFULLY_UPDATED", "status": status.HTTP_200_OK}
    else:
        result = {"result": "USER_NOT_FOUND", "status": status.HTTP_200_OK}
    return result


def change_user_password(user_uid, previous_password, new_password):
    print(user_uid)
    user_obj = User.objects.filter(uid=user_uid).first()
    if user_obj and user_obj.password == previous_password:
        user_obj.password = new_password
        user_obj.save()
        result = {'result': "PASSWORD_CHANGED_SUCCESSFULLY", "status": status.HTTP_200_OK}
    else:
        result = {'result': "USER_NOT_FOUND", "status": status.HTTP_200_OK}
    return result
