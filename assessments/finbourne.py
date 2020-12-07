# Split Messages
# You have a long piece of text, and you want to send it to your friend as a series of SMS messages. 
# Your text consists of English letters (uppercase and lowercase) and spaces. 
# The text doesn't contain any leading spaces at the beginning or trailing spaces at the end. 
# There are no two consecutive spaces in the text. One proper SMS can contain at most K characters. 
# If the text is longer, it needs to be split into parts. Each part should be sent in a separate message 
# that fulfills the maximum length requirement. Text may not be split within words. The order of the words 
# and the messages can't change, so that we can later concatenate the resulting messages to retrieve the original text. 
# Spaces at the start and end of all messages are removed, and thus are not accounted for in the overall message length.

# The goal is to count the number of SMS messages needed to accommodate the whole text, keeping the length of each message 
# less than or equal to K. The total number of SMS messages must be kept to a minimum, however; it would not be acceptable, 
# for example, to take the wasteful approach of programmatically sending one SMS for each word in the original text!

# Write a function: public func solution(_ S: String, _ K: Int) -> Int that, given a string S representing the text that 
# needs to be split and an integer K that is equal to the maximum possible message length, returns the number of SMS messages needed.

# For instance, given string S="SMS messages are really short" and K = 12, your function should return 3. You could split this 
# text into proper messages as follows: "SMS" "messages are" "really short"

# If it's impossible to split text into proper SMS messages, your function should return −1. Assume that: K is an integer 
# within the range [1..500]; S is a non-empty string containing at most 500 characters: only letters and spaces, there 
# are no spaces at the beginning and at the end of S; also there can't be two or more consecutive spaces in S.

def solution(S:str, K:int) -> int:

    # input validation
    if K < 1 or  K > 500 or len(S) > 500:
        return -1
    
    if len(S) <= K:
        return 1
    
    message_count = 0   # could also keep a list of the messages and return its length, but not required
    tokens = S.split()
    current_message = ""
    
    for token in tokens:
        
        # we can't send this token in a SMS without splitting it, so we can't send this message
        if len(token) > K:
            return -1
        
        # this token contains non-letter characters
        # if not token.isalpha():
        #     return -1
        
        # print("Token: {}, current_message: {}, len: {}".format(token, current_message, len(current_message)))
        
        # I have capacity for a space, so add the next token and a space to the current message
        if len(current_message + token) <= K-1:
            current_message += token + " "
            
        # I only have capacity for the token in this message
        elif len(current_message + token) <= K:
            current_message += token
            
        # No more capacity, must start a new message
        else:
            message_count += 1
            current_message = token + " "
            
    # if the last token did not fit in the previous message, send it on its own
    if len(current_message.strip()) != 0:
        message_count += 1
        
    # print("Final messages: {}".format(message_count))
    return message_count
            
if __name__ == "__main__":
    assert solution("SMS messages are really short", 10) == 4
    assert solution("SMS messages are really short", 12) == 3
    assert solution("SMS messages are really short", 3) == -1
    assert solution("SMS messages are really short", 8) == 5
    assert solution("Test main mess eat", 4) == 4
    assert solution("This is quite a verbose message you are trying to send through text", 20) == 4
    assert solution("Lorem ipsum dolor sit amet", 50) == 1
    assert solution("Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit amet", 50) == -1
    assert solution("Lorem ipsum dolor sit amet", 510) == -1
    assert solution("Lorem ipsum dolor sit amet", 0) == -1
    assert solution("I don't liken't apostro", 7) == 3