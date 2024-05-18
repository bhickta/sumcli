from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from .static_types import WordTags
import pyperclip

class Document:
    def __init__(self) -> None:
        self.set_allowed_word_tags()
        self.set_fillers()
        self.post_init()

    def set_allowed_word_tags(self):
        self.allowed_word_tags = []
        for tags in [
            WordTags.NOUN.value,
            WordTags.VERB.value,
        ]:
            self.allowed_word_tags.extend(tags)

    def set_fillers(self):
        self.filler_words = set(stopwords.words('english'))

    def post_init(self):
        self.set_text()
        self.process_text()

    def set_text(self):
        self.input_text = pyperclip.paste()

    def process_text(self):
        self.process_newline()
        self.tokenize()
        self.tag_words()
        self.summarize()

    def process_newline(self):
        lines = self.input_text.splitlines()
        self.input_lines = [line for line in lines if line.strip()]

    def tokenize(self):
        self.tokenized_lines = []
        for line in self.input_lines:
            tokens = word_tokenize(line)
            self.tokenized_lines.append(tokens)

    def tag_words(self):
        self.tagged_words_lines = []
        for line in self.tokenized_lines:
            tagged_line = pos_tag(line)
            self.tagged_words_lines.append(tagged_line)

    def summarize(self):
        self.summary_lines = []
        for tagged_line in self.tagged_words_lines:
            line = []
            for word, tag in tagged_line:
                if tag in self.allowed_word_tags and word.lower() not in self.filler_words:
                    line.append(word)
            self.summary_lines.append(" ".join(line))
        self.summary = "\n".join(self.summary_lines)