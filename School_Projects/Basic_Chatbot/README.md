# Jared-Hwee-Chatbot
Config files for my GitHub profile.
Chatbot program
*In the book "The Most Human Human: What Talking with Computers Teaches Us About What It Means to Be Alive", Brian Christian briefly discussed ELIZA: "It was the first computer chat program, written in 1964 by Joseph Weizenbaum at MIT. Its conversational style was modeled after the Rogerian (client-centered) psychotherapy technique (which treats the client as an equal partner in figuring out their own feelings, sources of problems and solutions). ELIZA extracts key words from the user's own language, and pose their statements back to them. ("I am unhappy..." "Do you think coming here will help you not to be unhappy?"; "I want to/ need to...." "What would it mean to you if you did that?"). If in doubt, it might fall back on some generic phrases like "Please go on." or "Tell me more".) A rather simple program with virtually no memory, no processing power and a few hundred lines of code, ELIZA evoked a stunning response. Many of the people who first talked to ELIZA believed it was a real person talking to them and reported having had a meaningful therapeutic experience. Although its original creator was horrified by this reaction and terminated the ELIZA project, ELIZA continued to become widely known among programmers and academics. Many modern chat bots are programmed after ELIZA."*

*You can try having a conversation with ELIZA through this link, or many other links on the internet.* http://manifestation.com/neurotoys/eliza.php3/

Using what you have learned in class, write a simplified version of ELIZA.

Requirements for the program:
- Have pre-programed responses to clients' input (One idea is to do something like the sample exercise listed below)
- Your program should first introduce its name, provide some greetings, ask for user's name and ask what they want to discuss today. Then it should give responses to users' input (using conditionals, see sample exercise below for a general idea)
- Your program should also have a description at the beginning letting user know that if they want to stop the conversation at any point, type "quit" and your program should have an ending message and terminate at that point.
- have code for ending/starting each session, and save all clients input and the system's responses in each session.
- ask whether user is administrator or client
- have password validation for the administrator

- When an administrator uses the program, they can view the following information if they wish:
    - how many sessions have been carried out with clients
    - display all the client's input in each session (identified by number)
    - average length of the client's input
    - the most frequently used word/phrase by the user
    - the most frequently displayed feedback by the program

- Your program should have a description letting user know that if they want to stop the conversation, type "quit" and your program should have an ending message and terminate at that point.
- Your program should first introduce its name, provide some greetings, ask for user's name and ask what they want to discuss today. Then it should give responses to users' input based on the following simple rules:
- when user's input includes the word "mother", print "Tell me more about your mother"
- when user's input includes the word "father", print "Tell me more about your father"
- when user's input includes the word "I" and the word "think", print "Why do you think that way?" or "Do you really think so?" or "I see."
- when user's input includes the word "I" and the word "feel", print "Why do you feel that way?" or "How often do you feel that way?"
- when user's input includes the word "I" and the words "want to" or the word "I" and "need to", print "What would it mean to you if you did that?"
- when user's input includes the word "you", print "We are here to talk about you, not me."
- and for all other cases different from the cases above, print "Please elaborate." or "Please tell me more" or "Go on."
