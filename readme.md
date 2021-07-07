# Video Game Tagging

## Description

In this project, I will be using NLP to predict the tags of steam games.

I will use the [Steam API](https://steamcommunity.com/dev) to get training data and [SteamSpy](https://steamspy.com/tag/) to get a list of all the tags available.
In order to interpret the input data, I will use tokenizers and bag of words to create input data for LDA. After performing Topic Modeling, I will manually label
the topics with corresponding tags, and check with existing tags to see if there is a good match.

Finally, I will use the best model to predict tags for new inputs.
