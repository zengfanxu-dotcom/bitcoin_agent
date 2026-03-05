from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from create_product_manager import create_product_manager
from create_engineer import create_engineer
from create_code_reviewer import create_code_reviewer
from create_user_proxy import create_user_proxy


def create_team_chat(model_client):
    product_manager = create_product_manager(model_client)
    engineer = create_engineer(model_client)
    code_reviewer = create_code_reviewer(model_client)
    user_proxy = create_user_proxy(model_client)

    return RoundRobinGroupChat(
        participants=[
            product_manager,
            engineer,
            code_reviewer,
            user_proxy
        ],
        termination_condition=TextMentionTermination("TERMINATE"),
        max_turns=20,
    )
