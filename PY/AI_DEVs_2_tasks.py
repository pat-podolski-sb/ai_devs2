from API_task_01.api_API_task_helloapi import api_test_task_01
from API_task_02.API_task_blogger_02 import api_test_task_02
from API_task_03.API_task_moderation_03 import api_test_task_03
from API_task_04.API_task_liar_04 import api_test_task_04
from API_task_04.API_task_liar_alternative_04 import api_test_task_alternative_04
from API_task_05.API_task_inprompt_05 import api_test_inprompt_05

from utils import calculateTokensInOpenaiInput

# 01 API task 
# api_test_task_01('helloapi')
# api_test_task_02('blogger')
# api_test_task_03('moderation')
# api_test_task_04('liar')
# api_test_task_alternative_04('liar')
# calculateTokensInOpenaiInput('What is the capital of Argentina?')
api_test_inprompt_05('inprompt')
