import os

from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 提示模版
from prompt_template import system_template_text, user_template_text
from xiaohongshu_model import Xiaohongshu


# 定义函数
def generate_xiaohongshu(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ('system',system_template_text),
        ('user',user_template_text)
    ])
    # 搞定模型
    model = ChatOpenAI(model = 'gpt-4o-mini',
                       api_key= openai_api_key,
                       base_url='https://free.v36.cm/v1')
    # 规范输出(解析器)
    out_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    # 定义链
    chain = prompt | model | out_parser
    result = chain.invoke({
        'parser_instructions':out_parser.get_format_instructions(),
        'theme':theme
    })
    return result
