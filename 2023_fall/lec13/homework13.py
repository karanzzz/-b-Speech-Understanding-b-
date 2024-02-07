import bs4
import gtts

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    soup = bs4.BeautifulSoup(text, "html.parser")
    stories = []
    
    # Extracting story titles and teasers
    for story in soup.find_all(class_='story-text'):
        title = story.find(class_='title').text.strip()
        teaser = story.find(class_='teaser').text.strip() if story.find(class_='teaser') else ""
        stories.append((title, teaser))
    
    return stories
    
def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    if n < 0 or n >= len(stories):
        raise ValueError("Invalid story index")
    
    # Selecting the nth story
    story = stories[n]
    
    # Synthesizing audio for the story title and teaser
    title_audio = gtts.gTTS(text=story[0], lang='en')
    teaser_audio = gtts.gTTS(text=story[1], lang='en')
    
    # Saving audio to file
    title_audio.save(filename)
    teaser_audio.save(filename, append=True)
