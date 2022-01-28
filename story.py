from dotenv import load_dotenv
import os
import openai


load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

def write_story(story_context):

    if story_context == None: # raise exception if story context is none
        raise Exception("You need to pass a story context")
  
    prompt_text = f'{story_context}'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.7,
      max_tokens=56,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
    )

    story = response['choices'][0]['text'] 

    print(story) 

    return str(story)
