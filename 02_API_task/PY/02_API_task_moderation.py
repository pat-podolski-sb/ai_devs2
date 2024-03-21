from pprint import pprint
from ai_devs2_utils import get_token_from_api, get_task_from_api, send_answer_to_api


# Get TOKEN moderation
tokenObject = get_token_from_api('moderation')
pprint('TOKEN FROM get_token_from_api METHOD:')
pprint(tokenObject.get('token'))


# Get TASK 
taskObject = get_task_from_api(tokenObject.get('token'))
pprint('TASK FROM get_task_from_api METHOD:')
pprint(taskObject)

# # Send ANSWER
# answerObject = send_answer_to_api(tokenObject.get('token'), taskObject.get('cookie'))
# pprint('ANSWER FROM send_answer_to_api METHOD:')
# pprint(answerObject)
