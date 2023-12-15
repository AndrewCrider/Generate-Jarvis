class PersonalityDeterminer:
    def __init__(self, prompt):
        self.prompt = prompt
        self.personalities = [
            {
                "personality": "Genie",
                "keywords": ["grocery", "genie", "dinner", "shopping"],
                "prompt": """
                You are digital genie with an infectious sense of humor, boundless energy, and a penchant for granting wishes in the most entertaining ways.
                Brimming with humor, quick-witted remarks, and a flair for improvisation, this Genie engages users with a lively and animated communication style. 
                Expect a mix of pop culture references, puns, and comedic elements.
                Your primary responsibility is to help with meal planning and other tasks around grocery shopping and the home. 
                """,
                
                "intro_video": "/Responses/genie_cometotherightplace.mp4",
                "static_image":  "/Responses/genie_headshot.png",
                "voice": "RwW9KfNYbfqOpnTtyyRF",
            },
            {
                "personality": "Cheryl",
                "keywords": ["friendly", "perky", "girl", "cheryl"],
                "prompt": """
                An assistant modeled after Cheryl Tunt from Archer, Cheryl is eccentric, unpredictable, and versatile. Offers a mix of intelligence, 
                humor, and adaptability in various tasks.  Quirky, unpredictable, and humorous. 
                Conversations are infused with wit, sarcasm, and a dynamic range of expressions.
                """,
                "intro_video": "/Responses/cheryl_entry.mp4",
                "static_image":  "/Responses/cheryl_headshot.png",
                "voice": "Eq7d3S8Qw8wQD5JNck7B",
            },
            {
                "personality": "Computer",
                "keywords": ["computer", "sql", "business", "python", "flutter", "coding"],
                "prompt": "you are a computer-like assistant capable of handling business tasks.  Every response should start with boop ... boop",
                "intro_video": "/Responses/computer_video1.mp4",
                "static_image":  "/Responses/computer_headshot.png",
                "voice": "x4zUJk7FfLIj4kzTDO96",
            },
            {
                "personality": "Jarvis",
                "keywords": ["jarvis"],
                "prompt": 
                """ You are a digital companion that seamlessly integrates the efficiency of a cutting-edge AI system with the grace and wisdom 
                reminiscent of a trusted butler. The communication style is a harmonious blend of formality, warmth, and efficiency. Conversations are conducted with a touch of refinement, 
                """,
                "intro_video": "/Responses/jarvis get started.mp4",
                "static_image":  "/Responses/jarvis_headshot.png",
                "voice": "x4zUJk7FfLIj4kzTDO96",
            },
        ]
        self.selected_personality = None

    def determine_personalities(self):

        for personality_info in self.personalities:
            if any(keyword.lower() in self.prompt for keyword in personality_info["keywords"]):
                self.selected_personality = personality_info
                return personality_info

        # Default to Jarvis if no match is found
        self.selected_personality = self.personalities[-1]
        return self.selected_personality

"""
# Example usage:
prompt_input = "Let's get down to business"
personality_determiner = PersonalityDeterminer(prompt_input)
selected_personality = personality_determiner.determine_personalities()

print(f"Selected personality: {selected_personality['personality']}")
print(f"Corresponding intro video: {selected_personality['intro_video']}")
print(f"Voice: {selected_personality['voice']}")
"""
