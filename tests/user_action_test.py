#
# from app.services import user_action_service
# # import pytest
# # import asyncio
# async def test_create_user_action():
#     result=await user_action_service.create_user_action({
#               "id": 0,
#               "user_id": 0,
#               "type": "revenue",
#               "amount": 4000,
#               "datetime": "2024-05-20T15:38:07.719Z"
#             })
#     new_user_action = {
#         "id": 5,
#         "user_id": 0,
#         "type": "revenue",
#         "amount": 4000,
#         "datetime": "2024-05-20T15:38:07.719Z"
#     }
#     assert result==new_user_action
#
#      # assert  user_action_service.create_user_action({
#      #     "id": 0,
#      #     "user_id": 999,
#      #     "type": "revenue",
#      #     "amount": 4000,
#      #     "datetime": "2024-05-20T15:38:07.719Z"
#      # }) == {
#      #            "id": 5,
#      #            "user_id": 0,
#      #            "type": "revenue",
#      #            "amount": 4000,
#      #            "datetime": "2024-05-20T15:38:07.719Z"
#      #        }
#      #
#      #
# async def test_get_user_action_by_user_id():
#  result=await user_action_service.get_user_action_by_user_id(0,0)
#  user_action = {
#      "id": 0,
#      "user_id": 0,
#      "type": "revenue",
#      "amount": 0,
#      "datetime": "2024-05-16T23:14:11.626+00:00"
#  }
#  assert  result==user_action