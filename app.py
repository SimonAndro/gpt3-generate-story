import os

from story import write_story


def story_writer(story_context, file):
 
    story = write_story(story_context) # get a part of the story

    file.write(story) # write to file

    return story #

if __name__ == '__main__':

    #
    # issue the initial story context
    #
    story_context = """Metaverse and the future.""" 

    file = open("stories/metaverse.html","a") # open file for appending, uses html format for easy line wrapping

    file.write("\n\n"+story_context+"\n\n") # write to file

    for  i in range(1,10): # looping over a given number of times to build on the story
        story_context = story_writer(story_context,file)

    file.close() # close file since we have finished writing