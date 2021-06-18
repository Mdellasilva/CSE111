from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # Test the singular nouns.
    singular_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        noun = get_noun(1)

        # Verify that the word returned from get_noun is
        # one of the words in the singular_nouns list.
        assert noun in singular_nouns

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural nouns.
    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        noun = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert noun in plural_nouns

def test_get_verb():
    # Test the past tense verbs.
    past_tense_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        verb = get_verb(1 or 2, "past")

        # Verify that the word returned from get_verb is
        # one of the words in the past_tense_verbs list.
        assert verb in past_tense_verbs

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the singular present tense verbs.
    singular_present_tense_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        verb = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the singular_present_tense_verbs list.
        assert verb in singular_present_tense_verbs

        # Test the plural present tense verbs.
    plural_present_tense_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        verb = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the plural_present_tense_verbs list.
        assert verb in plural_present_tense_verbs

        # Test the future tense verbs.
    future_tense_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(4):
        verb = get_verb(1 or 2, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future_tense_verbs list.
        assert verb in future_tense_verbs

def test_get_preposition():
    # Test the prepositions.
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        preposition = get_preposition()

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert preposition in prepositions

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

def test_get_prepostional_phrase():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    singular_determiners = ["the", "one"]

    plural_determiners = ["some", "many"]

    singular_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]

    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    for _ in range(4):

        prepositional_phrase_list = get_prepositional_phrase(1).split(" ")
        
        assert prepositional_phrase_list[0] in prepositions

        if prepositional_phrase_list[1] in singular_determiners:
            assert prepositional_phrase_list[1] in singular_determiners
        elif prepositional_phrase_list[1] in plural_determiners:
            assert prepositional_phrase_list[1] in plural_determiners
        else:
            assert 1 == 0
        #The "else" is used in the case that the determiner is not located in either the singular_determiners list or the plural_determiners list.

        if prepositional_phrase_list[2] in singular_nouns:
            assert prepositional_phrase_list[2] in singular_nouns
        elif prepositional_phrase_list[2] in plural_nouns:
            assert prepositional_phrase_list[2] in plural_nouns
        else:
            assert 1 == 0

    for _ in range(4):
        prepositional_phrase_list = get_prepositional_phrase(0).split(" ")
        
        assert prepositional_phrase_list[0] in prepositions

        if prepositional_phrase_list[1] in singular_determiners:
            assert prepositional_phrase_list[1] in singular_determiners
        elif prepositional_phrase_list[1] in plural_determiners:
            assert prepositional_phrase_list[1] in plural_determiners
        else:
            assert 1 == 0
        #The "else" is used in the case that the determiner is not located in either the singular_determiners list or the plural_determiners list.

        if prepositional_phrase_list[2] in singular_nouns:
            assert prepositional_phrase_list[2] in singular_nouns
        elif prepositional_phrase_list[2] in plural_nouns:
            assert prepositional_phrase_list[2] in plural_nouns
        else:
            assert 1 == 0

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])