'''
Emotion Detection Unit Test Coordination
'''
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_glad_statement(self):
        '''
        Test for Joy
        '''
        result = emotion_detector("I am glad this happened.")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_mad_statement(self):
        '''
        Test for Anger
        '''
        result = emotion_detector("I am really mad about this.")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgusted_statement(self):
        '''
        Test for Disgust
        '''
        result = emotion_detector("I feel disgusted just hearing about this.")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sad_statement(self):
        '''
        Test for Sadness
        '''
        result = emotion_detector("I am so sad about this.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_afraid_statement(self):
        '''
        Test for Fear
        '''
        result = emotion_detector("I am really afraid that this will happen.")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
