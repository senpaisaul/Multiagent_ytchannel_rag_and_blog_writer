from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
import os
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME']='gpt-4-0125-preview'


##create a senior blog content researcher
blog_researcher = Agent(
    role='Blog Researcher from youtube videos',
    goal='get the relevant video content fot the topic{topic} from youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and GEN AI and providing suggestions"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

##create a Senior blog writer agent with YT tool

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "with a flair for simplifying complex concepts, you craft"
        "engaging narritives that captivate and educate, bringin new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)