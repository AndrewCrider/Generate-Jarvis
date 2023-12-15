from elevenlabs import set_api_key, generate, play, Voice, VoiceSettings
import user_config

## TODO: Make sure to update the example_user_config.py file and save it as user_config
set_api_key(user_config.one11_key)

def getPersonalityVoice(voice_id, text):
    audio = generate(
        text=text,
        voice=voice_id,
        model="eleven_multilingual_v2",
    )
    
    return audio

## Testing for class
#getPersonalityVoice("Eq7d3S8Qw8wQD5JNck7B", "Hello Andrew, what's up?")
