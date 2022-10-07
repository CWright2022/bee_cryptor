import bee_cryptor


def test_make_index_list_basic():
    # setup
    expected = [7, 17, 8, 10, 6, 62, 5, 4, 93, 0, 60, 92, 69, 76, 76, 79]
    # invoke
    actual = bee_cryptor.make_index_list("'1(*&^%$} \|ello")
    # analyze
    assert expected == actual


def test_make_base_word_list_basic():
    # setup
    expected = ['Bee', 'Movie', 'Script', '-', 'Dialogue', 'Transcript', 'Voila!', 'Finally,', 'the', 'script', 'is', 'here', 'for', 'all', 'you', 'fans', 'of', 'Jerry', 'Seinfeld', 'animated', 'movie.', 'This', 'puppy', 'a', 'transcript', 'that', 'was', 'painstakingly', 'transcribed', 'using', 'screenplay', 'and/or', 'viewings', 'movie', 'to', 'get', 'dialogue.', 'I', 'know,', 'still', 'need', 'cast', 'names', 'in', 'there', 'and', 'jazz,', 'so', 'if', 'have', 'any', 'corrections,', 'feel', 'free', 'drop', 'me', 'line.', 'At', 'least', "you'll", 'some', 'quotes', '(or', 'even', 'monologue', 'or', 'two)', 'annoy', 'your', 'coworkers', 'with',
                'meantime,', 'right?', 'And', 'swing', 'on', 'back', "Drew's", 'Script-O-Rama', 'afterwards', '--', 'because', 'reading', 'good', 'noodle.', 'Better', 'than', 'Farmville,', 'anyway.', 'According', 'known', 'laws', 'aviation,', 'no', 'way', 'bee', 'should', 'be', 'able', 'fly.', 'Its', 'wings', 'are', 'too', 'small',
                'its', 'fat', 'little', 'body', 'off', 'ground.', 'The', 'bee,', 'course,', 'flies', 'anyway', 'bees', "don't", 'care', 'what', 'humans', 'think', 'impossible.', 'Yellow,', 'black.', 'Ooh,', 'black', 'yellow!', "Let's", 'shake', 'it', 'up', 'little.', 'Barry!', 'Breakfast', 'ready!', 'Ooming!', 'Hang', 'second.', 'Hello?', 'Barry?', 'Adam?', 'Oan', 'believe', 'this', 'happening?', "can't.", "I'll", 'pick', 'up.', 'Looking', 'sharp.', 'Use', 'stairs.', 'Your', 'father', 'paid', 'money', 'those.', 'Sorry.', "I'm", 'excited.',
                "Here's", 'graduate.', "We're", 'very', 'proud', 'you,', 'son.', 'A', 'perfect', 'report', 'card,', "B's.", 'Very', 'proud.', 'Ma!', 'got', 'thing', 'going', 'here.', 'You', 'lint', 'fuzz.', 'Ow!', "That's", 'me!', 'Wave', 'us!', "We'll", 'row', '118,000.', 'Bye!', 'Barry,', 'told', 'stop', 'flying', 'house!', 'Hey,', 'Adam.', 'Barry.', 'Is', 'fuzz', 'gel?', 'Special', 'day,', 'graduation.', 'Never', 'thought', "I'd", 'make', 'it.', 'Three', 'days', 'grade', 'school,']
    # invoke
    actual = bee_cryptor.make_base_word_list('test_script.txt')
    # analyze
    assert expected == actual

def test_encrypt_basic():
    # setup
    expected = "right? coworkers back back afterwards Bee two) And back back According Movie "
    # invoke
    actual = bee_cryptor.encrypt("hello billy!", "test_script.txt")
    # analyze
    assert expected == actual