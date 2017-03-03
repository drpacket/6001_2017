# ---------------------------------------------------------------------------- # 
# -------- *** MITx course 600.1x ** Online course on edx *** ---------------- #
# ------- Introduction to Computer Science and Programming using Python ------ #
# ------------------------ [Problem Set 5] ----------------------------------- #
# ---------------------------------------------------------------------------- #
# *** Problem Set 5 ***

# -- Problem 1 -- The Message Class --
# ---------------------------------------------------------------------------- #

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text
        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        shift_lower_values = lower_values[shift:] + lower_values[:shift]
        
        upper_keys = list(string.ascii_uppercase)                 
        upper_values = list(string.ascii_uppercase)
        upper_shift_values = upper_values[shift:] + upper_values[:shift]

        full_keys = lower_keys + upper_keys
        full_values = shift_lower_values + upper_shift_values

        self.shift_dict = dict(zip(full_keys, full_values))
        return self.shift_dict        
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)

# -- Problem 2 -- Plaintextmessage --
# ---------------------------------------------------------------------------- #

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.shift = shift
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        encrypting_dict_copy = self.encrypting_dict.copy()
        return encrypting_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)
        

# -- Problem 3 -- Cyphertextmessage -- !!! ERROR! -- CHECK FOR FURTHER BUGS !!!
# ---------------------------------------------------------------------------- #

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.
        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return
        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        word_counter = 0
        max_count = 0
        for i in range(26):
            for j in list(super(CiphertextMessage, self).apply_shift(i).split(' ')):
                if is_word(self.valid_words, j):
                    word_counter += 1
                if word_counter > max_count:
                    max_count = word_counter
                    shift_value = i
                    decrypted_msg = super(CiphertextMessage, self).apply_shift(i)
                        
        return (shift_value, decrypted_msg)

# -- Problem 4 -- Decrypt a story --
# ---------------------------------------------------------------------------- #

def decrypt_story():
    joke_code = CiphertextMessage(get_story_string())
    return joke_code.decrypt_message()
    



# *** EOF ***
# ---------------------------------------------------------------------------- #