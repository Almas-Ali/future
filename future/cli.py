import argparse
import wikipedia
import pyttsx3
import os

os.environ['audio'] = 'enable'

print(os.environ['audio'])

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)
engine.setProperty('rate', 150)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def wiki(query: str = None):
    wikipedia.set_lang('en')
    summary = wikipedia.summary(query, sentences=2)

    return summary


def main():
    '''Main CLI function of this project Future.'''
    parser = argparse.ArgumentParser()

    parser.add_argument('--wiki-search', '-ws', help='search on wikipedia.')
    parser.add_argument('--audio-enable', '-ae',
                        help='enable audio to get also audio output.', action='store_true')
    parser.add_argument('--audio-disable', '-ad',
                        help='disable audio to not get audio output.', action='store_true')

    args = parser.parse_args()

    if args.wiki_search:
        print(wiki(args.wiki_search))

    elif args.audio_enable:
        with open('audio.conf', 'r') as audio:
            # audio.write('enable')
            print(audio.read())
        print('audio enabled')
        os.environ('audio', 'enable')

    elif args.audio_disable:
        print('audio disabled')

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
