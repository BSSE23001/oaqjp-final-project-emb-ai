from EmotionDetection import emotion_detector


def test_emotion_detection():
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    for text, expected in test_cases:
        result = emotion_detector(text)
        assert result["dominant_emotion"] == expected, \
            f"Failed for: {text}. Expected {expected}, got {result['dominant_emotion']}"

    print("All test cases passed successfully!")


if __name__ == "__main__":
    test_emotion_detection()