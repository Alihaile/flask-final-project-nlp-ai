import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection:
    def test_emotion_detector(self):
        res_joy = emotion_detector("I am glad this happened")
        res_anger = emotion_detector("I am really mad about this")
        res_disgust = emotion_detector("I feel disgusted just hearing about this")
        res_sad = emotion_detector("I am so sad about this")
        res_fear = emotion_detector("I am really afraid that this will happen")

        self.assertEqual(res_joy['joy'], 'joy')
        self.assertEqual(res_anger['anger'], 'anger')
        self.assertEqual(res_disgust['disgust'], 'disgust')
        self.assertEqual(res_sad['sadness'], 'sadness')
        self.assertEqual(res_fear['fear'], 'fear')

unittest.main()